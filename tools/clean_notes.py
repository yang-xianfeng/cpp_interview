#!/usr/bin/env python3
"""Clone and clean Yuque-exported markdown notes inside cpp_interview.

Features:
- Copy a source notes folder into a separate cleaned folder.
- Remove redundant frontend-export markup such as `<br />` and Yuque anchor tags.
- Strip the long fragment after common remote image links such as `*.png#...`.
- Keep markdown tables readable instead of breaking rows while removing `<br />`.
- Optionally download remote images into a local assets directory.

By default this script uses only Python's standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

IMAGE_PATTERN = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<url>https?://[^)\s]+)\)")
BR_PATTERN = re.compile(r"<br\s*/?>", flags=re.IGNORECASE)
YUQUE_ANCHOR_PATTERN = re.compile(r"<a\s+name=\"[^\"]+\"></a>\s*", flags=re.IGNORECASE)
FENCE_PATTERN = re.compile(r"(^```.*?$.*?^```[ \t]*$)", flags=re.MULTILINE | re.DOTALL)
EMPTY_HEADING_PATTERN = re.compile(r"^[ \t]{0,3}#{1,6}[ \t]*$")
INLINE_FENCE_PATTERN = re.compile(r"([^\n])```([A-Za-z0-9_+-]+)")
CONSECUTIVE_FENCE_PATTERN = re.compile(r"``````([A-Za-z0-9_+-]+)")
COMMON_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"}
PROJECT_ROOT = Path(__file__).resolve().parent.parent


@dataclass
class ImageRecord:
    alt: str
    original_url: str
    sanitized_url: str
    rewritten_url: str
    status: str = "pending"
    error: str = ""


class NotesCleaner:
    def __init__(
        self,
        source_dir: Path,
        output_dir: Path,
        assets_dirname: str,
        download_images: bool,
        timeout: int = 20,
    ) -> None:
        self.source_dir = source_dir
        self.output_dir = output_dir
        self.assets_dirname = assets_dirname
        self.download_images = download_images
        self.timeout = timeout
        self.assets_dir = self.output_dir / self.assets_dirname
        self.report: Dict[str, object] = {
            "source_dir": str(source_dir),
            "output_dir": str(output_dir),
            "download_images": download_images,
            "files": {},
            "summary": {
                "markdown_files": 0,
                "br_tags_replaced": 0,
                "yuque_anchors_removed": 0,
                "image_urls_sanitized": 0,
                "images_downloaded": 0,
            },
        }

    def clone_tree(self) -> None:
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        shutil.copytree(self.source_dir, self.output_dir)
        if self.download_images:
            self.assets_dir.mkdir(parents=True, exist_ok=True)

    def run(self) -> None:
        self.clone_tree()
        for md_path in sorted(self.output_dir.glob("*.md")):
            self.report["summary"]["markdown_files"] += 1
            self._process_markdown_file(md_path)
        self._write_report()

    def _process_markdown_file(self, md_path: Path) -> None:
        original = md_path.read_text(encoding="utf-8")
        cleaned_text, br_count, anchor_count = self._normalize_markup(original)
        records = self._collect_and_prepare_images(md_path, cleaned_text)
        updated = self._rewrite_image_urls(cleaned_text, records)
        updated = self._compact_whitespace(updated)
        md_path.write_text(updated, encoding="utf-8")

        file_report = {
            "br_tags_replaced": br_count,
            "yuque_anchors_removed": anchor_count,
            "images": [
                {
                    "original_url": record.original_url,
                    "sanitized_url": record.sanitized_url,
                    "rewritten_url": record.rewritten_url,
                    "status": record.status,
                    "error": record.error,
                }
                for record in records
            ],
        }
        self.report["files"][md_path.name] = file_report
        self.report["summary"]["br_tags_replaced"] += br_count
        self.report["summary"]["yuque_anchors_removed"] += anchor_count

    def _normalize_markup(self, text: str) -> Tuple[str, int, int]:
        text = self._normalize_inline_fences(text)
        parts = FENCE_PATTERN.split(text)
        br_total = 0
        anchor_total = 0
        for idx, part in enumerate(parts):
            if idx % 2 == 1:
                continue
            count = len(BR_PATTERN.findall(part))
            br_total += count
            part = self._normalize_br_markup(part)
            anchor_count = len(YUQUE_ANCHOR_PATTERN.findall(part))
            anchor_total += anchor_count
            part = YUQUE_ANCHOR_PATTERN.sub("", part)
            part = part.replace("\xa0", " ")
            part = self._remove_empty_headings(part)
            part = re.sub(r"[ \t]+\n", "\n", part)
            parts[idx] = part
        return "".join(parts), br_total, anchor_total

    def _normalize_br_markup(self, text: str) -> str:
        lines: List[str] = []
        for line in text.splitlines():
            if not BR_PATTERN.search(line):
                lines.append(line)
                continue

            if self._looks_like_table_row(line):
                lines.append(self._normalize_table_breaks(line))
                continue

            lines.extend(BR_PATTERN.sub("\n", line).splitlines())
        normalized = "\n".join(lines)
        if text.endswith("\n"):
            normalized += "\n"
        return normalized

    def _looks_like_table_row(self, line: str) -> bool:
        stripped = line.strip()
        return stripped.count("|") >= 2 and stripped.startswith("|")

    def _normalize_table_breaks(self, line: str) -> str:
        cells = line.split("|")
        for idx in range(1, len(cells) - 1):
            cell = BR_PATTERN.sub(" / ", cells[idx])
            cell = re.sub(r"(?:\s*/\s*){2,}", " / ", cell)
            cell = re.sub(r"^(?:\s*/\s*)+", "", cell.strip())
            cell = re.sub(r"(?:\s*/\s*)+$", "", cell)
            cells[idx] = f" {cell} " if cell else " "
        return "|".join(cells).rstrip()

    def _remove_empty_headings(self, text: str) -> str:
        lines = [line for line in text.splitlines() if not EMPTY_HEADING_PATTERN.match(line)]
        normalized = "\n".join(lines)
        if text.endswith("\n"):
            normalized += "\n"
        return normalized

    def _normalize_inline_fences(self, text: str) -> str:
        text = CONSECUTIVE_FENCE_PATTERN.sub("```\n```\\1", text)
        return INLINE_FENCE_PATTERN.sub(r"\1\n```\2", text)

    def _collect_and_prepare_images(self, md_path: Path, text: str) -> List[ImageRecord]:
        records: List[ImageRecord] = []
        matches = list(IMAGE_PATTERN.finditer(text))
        if not matches:
            return records

        md_assets_dir: Optional[Path] = None
        if self.download_images:
            stem = md_path.stem
            safe_stem = self._slugify(stem)
            md_assets_dir = self.assets_dir / safe_stem
            md_assets_dir.mkdir(parents=True, exist_ok=True)

        for index, match in enumerate(matches, start=1):
            alt = match.group("alt").strip()
            original_url = match.group("url")
            sanitized_url = self._sanitize_image_url(original_url)
            record = ImageRecord(
                alt=alt,
                original_url=original_url,
                sanitized_url=sanitized_url,
                rewritten_url=sanitized_url,
            )

            if self.download_images and md_assets_dir is not None:
                ext = Path(urlsplit(sanitized_url).path).suffix.lower() or ".png"
                if ext not in COMMON_IMAGE_EXTENSIONS:
                    ext = ".png"
                digest = hashlib.sha1(sanitized_url.encode("utf-8")).hexdigest()[:10]
                image_name = f"{index:03d}_{digest}{ext}"
                local_path = md_assets_dir / image_name
                local_relpath = local_path.relative_to(self.output_dir).as_posix()
                record.rewritten_url = local_relpath

                try:
                    if not local_path.exists():
                        self._download_image(sanitized_url, local_path)
                    self.report["summary"]["images_downloaded"] += 1
                    record.status = "downloaded"
                except Exception as exc:  # pragma: no cover - network/runtime dependent
                    record.status = "failed"
                    record.error = str(exc)
            elif sanitized_url != original_url:
                record.status = "sanitized"
            else:
                record.status = "unchanged"

            records.append(record)
        return records

    def _download_image(self, url: str, local_path: Path) -> None:
        request = Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; CppNotesCleaner/1.0)",
            },
        )
        with urlopen(request, timeout=self.timeout) as response:
            local_path.write_bytes(response.read())

    def _rewrite_image_urls(self, text: str, records: Sequence[ImageRecord]) -> str:
        if not records:
            return text

        mapping = {record.original_url: record.rewritten_url for record in records}

        def replacer(match: re.Match[str]) -> str:
            alt = match.group("alt")
            url = match.group("url")
            new_url = mapping.get(url)
            if new_url is None:
                return match.group(0)
            if new_url != url:
                self.report["summary"]["image_urls_sanitized"] += 1
            return f"![{alt}]({new_url})"

        return IMAGE_PATTERN.sub(replacer, text)

    def _compact_whitespace(self, text: str) -> str:
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        return text.strip() + "\n"

    def _sanitize_image_url(self, url: str) -> str:
        parts = urlsplit(url)
        path = parts.path
        ext = Path(path).suffix.lower()
        if ext in COMMON_IMAGE_EXTENSIONS:
            return urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, ""))
        return urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, parts.fragment))

    def _slugify(self, value: str) -> str:
        value = re.sub(r"\s+", "_", value.strip())
        value = re.sub(r"[^\w\-.]+", "_", value, flags=re.UNICODE)
        return value or "notes"

    def _write_report(self) -> None:
        report_path = self.output_dir / "cleaning_report.json"
        report_path.write_text(
            json.dumps(self.report, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clone and clean Yuque-exported markdown notes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """\
            Examples:
              python3 tools/clean_notes.py
              python3 tools/clean_notes.py --output-dir notes/cleaned
              python3 tools/clean_notes.py --download-images
            """
        ),
    )
    parser.add_argument(
        "--source-dir",
        default="notes/source",
        help="Source notes directory. Default: %(default)s",
    )
    parser.add_argument(
        "--output-dir",
        default="notes/cleaned",
        help="Cleaned copy directory. Default: %(default)s",
    )
    parser.add_argument(
        "--assets-dirname",
        default="_assets",
        help="Local assets directory inside the cleaned copy.",
    )
    parser.add_argument(
        "--download-images",
        action="store_true",
        help="Download remote images and rewrite links to local assets.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    source_dir = Path(args.source_dir)
    output_dir = Path(args.output_dir)

    if not source_dir.is_absolute():
        source_dir = (PROJECT_ROOT / source_dir).resolve()
    else:
        source_dir = source_dir.resolve()

    if not output_dir.is_absolute():
        output_dir = (PROJECT_ROOT / output_dir).resolve()
    else:
        output_dir = output_dir.resolve()

    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}", file=sys.stderr)
        return 1

    cleaner = NotesCleaner(
        source_dir=source_dir,
        output_dir=output_dir,
        assets_dirname=args.assets_dirname,
        download_images=args.download_images,
    )
    cleaner.run()
    print(f"Cleaned notes written to: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
