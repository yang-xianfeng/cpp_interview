## 1.linux网络设置 基础命令
打开终端 ( terminal)  :  `Ctrl` +  `Alt` + `T`
`Ctrl` +  `C`  中止程序
```c
ping www.baidu.com  // 能否连接百度
ping 192.168.x.x    // ping inet 路由器
ping 127.0.0.1      // 环回地址，看本机网络环境是否有问题
```
桥接模式 与 NAT模式：
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648561877568-37c12e82-8184-4380-96fb-961e5f7e3d22.png)

## 2.Linux基础
### 2.1 Linux架构图
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648562745041-379efab1-0f5d-4bf6-afe3-9544f8ee0f17.png)
Linux的系统可以分成哪几层结构，分别有什么功能？
kernel：

- 管理硬件资源 CPU、内存、外部设备
- 文件管理 、内存管理、进程调度、网络通信、硬件驱动
- 为上层应用软件提供运行环境；

系统调用：内核对上层应用程序提供的接口；
库函数：对系统调用进行包装，方便程序使用；
shell：命令解析器，本质上是一个程序，解析命令，执行命令和 脚本（命令的集合）.

### 2.2 Linux基础命令
#### 2.1 `man`:
`d(down)`        向下移动半页
`u(up)`            向上移动半页
`f(forward)`  向下移动整页
`p(previous)`向上移动整页
`q(quit)`        退出
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648563311850-593b1b34-3e7c-4b4e-8dea-daf80e35a9fa.png)

#### 2.1.2 查看内核信息
`uname`:
`kernel name` ` 网络节点名字` `kernel realse` `kernel version` `hardware name` `processor`  ` 硬件平台`  `操作系统`

#### 2.1.3 查看发行版本
`cat /etc/issue`:
`发行版本` `version` `LTS - Long Time Support`

### 2.2 用户子系统：`root `   ` sudoers`     ` usr`
#### 2.2.1 查看发行版本
`cat /etc/passwd`:
`username` `password` `user id` `group` `comments(注释字段)` `用户所属home下的目录` `默认shell程序`

#### 2.2.2 添加用户
`useradd`: creat a new user or update default new user information
```c
$ sudo useradd test
test:x:1001:1001::/home/test : /bin/sh
//                默认不会自动创建home目录
//              			    默认的shell是sh
```
```c
$ sudo useradd -m -s /bin/bash test
//             -m创建home目录
//                    指定bash为默认的shell
```

#### 2.2.3. 删除用户
`userdel`:delete a user account and related files
```c
$ sudo userdel test
$ sudo userdel --remove test
               // -r 删除home目录和邮箱
```

#### 2.2.4 切换用户
`su`: change user ID or become superuser
退出切换
`exit`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648564760865-1110a989-fbed-49b2-898b-5560bce7a4dc.png)

#### 2.2.5 修改密码：
`passwd`: change user password
```c
$ sudo passwd test
```

### 2.3 文件子系统
虚拟文件系统 ( VFS ) : 树形
每一个进程都有一个属性叫作 当前工作目录。
shell 也是一个进程，它有自己的当前工作目录。
`pwd` : print name of current/working directory
`cd` : change the working directory
```c
cd /  切换到根目录
cd ~  切换到该用户的家目录
cd .  切换到当前目录
cd .. 切换到上一级目录
cd -  回到上一次的目录,存在 env(查看环境变量) 中
cd    绝对路径/相对路径 移动到指定目录中
```

bin(binary) :      	     可执行程序
dev(device) :                设备文件
home :			     普通用户家目录的根目录
root :			     root用户的家目录
sbin ( system binary ):  系统相关的可执行程序
var ( variable ):	     经常发生的文件，比如日志文件
etc :				     配置文件
lib :				     库文件
proc ( process ) :	     进程映射文件
 2.3.1 创建文件夹
`mk` : make directories
```c
mkdir dir1		//
mkdir dir2 dir3 //
mkdir -v		// -v verbose print a message for each
```

####  2.3.1 创建文件夹
`mkdir` : make directories
```c
mkdir dir1		//
mkdir dir2 dir3 //
mkdir -v  // -v verbose // print a message for each
```
####  2.3.2 创建文件夹
`rmdir` : make directories
```c
rmdir dir1		//
rmdir dir2 dir3 //
rmdir -v // -v verbose //output a diagnostic for each
```
#### 2.3.3 查询文件/列表文件
`ls` : list directory contents
```c
ls -a // -a all // don't ignore entries starting with
   -l // -l list // use a long listing format
      // chmod  u+x
   -i // with -l  -inode // print the index number of each file
   -h // with -l  -human-readable
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648621799283-e6bef915-c794-4b07-b0cd-0e54c441029c.png)![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648621831914-6257e920-1f1a-4366-a26a-dd682ba60271.png)
`d` : directory
`-`: file
`l` : Symbolic Link ( 符号链接，软链接）
`c` : 字符设备 (键盘 )
`b` : 块设备 ( 硬盘 )
`p` : 管道文件 ( 进程之间互相通信 )
`s` : 套接字文件 （网络通信）

chmod ：  `user`    `group`    `others`
`r `: read     `w` :  write    `x` :  execute     `-`  : 没有对应的权限

**通配符**：
*可以匹配任意多个字符（包括0个字符）
？可以匹配任意一个字符
[ charactes] 匹配集合内的任意一个字符   i.e. [abc]
[ !charactes] 匹配集合外的任意一个字符  i.e. [!abc]
类：[0-9] 数字    [a-z] 小写字母    [A-Z a-z] 字母

#### 2.3.4 复制文件（夹）
`cp` : copy files and directory
```c
cp file dir     // 把文件复制到对应的目录下
cp file file2   // 把文件复制到另外一个文件中，如果不存在，创建;存在,则覆盖
   -i           //-i interactive // prompt before overwrite
   -v           //-v verboes 显示每个的信息
cp -r dir1 dir2 // -r  recursively递归复制子文件夹
                // 如果dir2不存在，则会创建dir2，并复制进去
                // 如果dir2存在，则会将dir1目录及子文件 复制进dir1

   -u           // -u update  更新不存在的文件或最新的文件
```

#### 2.3.5 移动文件（夹）
`mv` :  move(rename) file
mv file1 file2 :
把file1 移动到 file2 ，如果文件不存在，则创建文件;如果存在,则覆盖文件。
mv file1 dir :
把file1 移动到 dir ，如果dir存在，将file1 移动到 dir中。
mv dir1 dir2 :
如果dir2存在，则将dir1移动到 dir2中
如果dir2不存在，创建dir2目录，并将dir1的内容“移动”到dir2中  同级则重命名.
```c
mv name1.txt name2.txt          // rename

mv name1.txt dir2/name1.txt     // overwrite
mv -i name1.txt dir2/name1.txt  // -i interactive

   -v							// -v verboes

   -u							// -u update

```

**注意： cp  需要修改磁盘，并且修改文件索引**
   ** mv  只需要修改虚拟文件索引**

#### 2.3.6 删除文件（夹）
`rm` ： remove files
```c
rm -i    // !!!多用提示
   -f    // -f force
   -i -f // 没有提示
   -rv   // -r recursively -v verboes
```
注意：
平时不要使用root
删除之前，要确定要删除的选项 （如果使用了通配符，先 `ls`查看文件）
添加 `-i` 参数

#### 2.3.7 链接
`ln` :  make links between files
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648775811175-5a0831f9-4759-475f-a23a-e52825a15e5f.png)
inode :
在Linux系统中，内核为**每一个新创建的文件 (硬链接 hard link 不会创建 新的 inode）**分配一个inode，每个文件都有一个惟一的inode号，我们可以将inode简单理解成一个指针，它永远指向本文件的具体存储位置。文件大小、属主属组、创建时间(ctime)、修改时间(mtime)、数据所在block号等文件属性保存在inode里。
在访问文件时，inode被复制到内存，从而实现文件的快速访问。系统是通过inode来定位每一个文件。
data block存放文件的数据信息。

硬链接（hard link）
硬链接实际上是一个指针，指向源文件的**inode**，系统并不为它重新分配inode。硬连接不会建产新的inode，硬连接不管有多少个，都指向的是同一个inode节点，只是新建一个hard link会把结点连接数增加，只要结点的连接数不是0，文件就一直存在，不管你删除的是源文件还是连接的文件。只要有一个存在，文件就存在（其实就是引用计数的概念)。当你修改源文件或者任何一个硬链接文件的时候，同一文件都会做同步的修改。
hard link 文件有着相同的inode号及data block,删除一个硬链接并不影响其他有相同inode号的文件。

软链接（soft link）
软链接最直观的解释：该文件的内容是源文件的**路径**指针，通过该链接可以访问到源文件。
symbolic link 与hard link不同，**一个独立文件**（拥有属于自己的、独立的、与源文件inode无关的inode,及data block中存放的内容是指向另一个文件的路径），symbolic link是普通的文件，有自己的文件属性及权限。
删除symbolic link并不影响源文件，但如果源文件被删除，则相对应的symbolic link被称为死链接(dangling link)，若被指向路径的文件重新创建，dangling link可以恢复为正常的软链接。可以类比Windows上快捷方式。

硬链接（hard link） 和 软链接（soft link）区别
1. 软链接和源文件操作权限不一样；硬链接与源文件操作权限完全一致。
2. 软链接可以跨文件系统(分区）；由于inode的限制以及文件系统的可卸载性，硬连接不容许跨文件系统。
3. 软连接可以对一个不存在的文件名进行连接；硬链接不可以。
4. 软连接可以对目录进行连接；硬链接不可以。
[
](https://blog.csdn.net/yasaken/article/details/7292186)
```c
//  -symbonic 符号链接，软链接   类似C语言的指针，windows 的快捷方式
ln -s . /b.txt link_sym 			// -symbonic 符号链接，软链接
ln -s  /home/he/dir/b.txt link_sym1 // -symbonic 符号链接，软链接
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648708341146-1da1c5be-1112-4aaa-bb2e-b46a18230090.png)
如果想在一个目录中添加或者删除目录项，需要获取该目录的 写权限
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648708346594-8e348fd5-7af4-4e1b-910d-a99bdf42ae90.png)

#### 2.3.8 文件查找
`locate` : find files by name.  自己维护一个数据库

`which` : locate  a command( 可执行程序 )

***`find`*** : search for files in a directory hierarchy.
格式 :  find 目录 查找方式 具体参数
-name
-type
-user/group id
-size
-empty
-perm

**通配符**：
*可以匹配任意多个字符（包括0个字符）
？可以匹配任意一个字符
[ charactes] 匹配集合内的任意一个字符   i.e. [abc]
[ !charactes] 匹配集合外的任意一个字符  i.e. [!abc]
类：[0-9] 数字    [a-z] 小写字母    [A-Z a-z] 字母

```c
// 1. -name
find dir -name pattern  // from dir find pattern
find / -name "stdio.h"

         -a 	 // -and
         -o		 // -or
         !	 	 // 逻辑取反

// 2. -type
        -type
               b // block (buffered) special
               c // character (unbuffered) special
               d // directory
               p // name pipe (FIFO)
               f // regular file
               l // symbonic link;
               s // socket
find .  -type  f 				  // rugular file 普通文件
find .  -type  l 				  // symbonic link
find .  -name "*soft*" -a -type l // 可以多个条件组合查找

// 3. 根据用户和组查找
           -user
           -uid
           -group
           -gid
find /home -user test

// 4. -size   // rounding up && default b = 512B
              b // default  512byte
              c // for bytes
              w // for two-bytes
              k // for  kibibytes (KiB : 1024 bytes)
              M // for  Mebibytes (MiB : 1024 * 1024 bytes)
              G // for  Gibibytes (GiB : 1024 * 1024 * 1024 bytes)
find ~ -size 6688c  // precise find size of 6688B
find ~ -size +4K    // + more than size
find ~ -size -4K  	// - less than size
find ~ -size 0c  	// exclude empty dir
// the size of empty dir is 4096B,查找空目录使用 -empty
// 5. -empty
find . -empty    	// find empty dir

// 6. permossion
find . -perm 664  	// rw- rw- r--
find . -perm -u=x   // find file with x permission

// command compose
// -exec 再执行其他命令
// {}  以**行**为单位 存储前面命令的结果 使用
find /usr/include/ -name "stdio.h" -exec ls -l {} \;
```

#### 2.3.9 组合命令  // command compose
```c
mkdir dir3; cd dir3		//
```

#### 2.3.10 权限命令
`chmod` : change file mode bits
```c
// 文字设定法
chmod [ugoa] [+=-] [rwx] file/dir	// user group others all
chome u=rw,g=rw,o=r a.txt  		    //compose

// ***数字设定法***
chmod 三位八进制数字 file/dir
chmod 664 a.txt 				// rw- rw- r--
```

#### 2.3.11 文件掩码
`umask` 文件（默认是0666）或目录（默认0777）
user : `umask` : 0002  创建文件夹时，默认权限**777 & (~umask)**
root : `umask` : 0022  创建普通文件时，默认权限**666**
```c
 umask 四位数字 // 临时改变权限，会被还原
```

#### 2.3.12 查看文件内容
`touch` 、 `echo` 、 `cat` 、 `vim`: 创建文件的命令

`cat` :  concatenate files and print on the standard output
把标准输入的内容输出到标准输出中
 如果cat的命令行中没有参数，它就会从标准输入中读取数据，并将其送到标准输出

   文件描述符（非负整数）
`stdin`     标准输入          键盘          0
`stdout`   标准输出          显示器       1
`stderr`   标准错误输出   显示器       2

重定向：
`>`  :   标准输出重定向 （先清除）
`<`  :   标准输入重定向 （先清除）
`2>` :  标准错误重定向
`>>` :  标准输出重定向 （追加）
`<<` :  表示以什么结束

```c
cat > a.txt
...
...
...
    Ctrl + C  /  Ctrl + D // 中止
```

#### 2.3.13 `echo`
`echo` :   display a line of text
```c
$ echo

$ echo "h"
h
$ echo "hello" > a.txt

```

#### 2.3.14 `head`
`head` :  output the first part of files
```c
head a.txt		  // 默认10行，随机
head -n 10 a.txt  // 指定显示开头10行
```

#### 2.3.15 `tail`
`tail` :  output the last part of files
```c
tail b.txt 		    // 默认10行，随机
tail -n 20 b.txt	// 指定显示开头10行
```

#### 2.3.16 `more & less` : 单页浏览
 `more` - file perusal filter for crt viewing
`less`- opposite of more
```c
less c.txt
f	// forward
b	// backward
q	// quit
```

#### 2.3.17 文件的其他操作
`sort` : sort lines of text files
把文件的内容读入到内存，然后以**行**的单位对内存中的数据进排序，最后把排序后的结果输出到`stdout`

`uniq`: report or omit repeated lines  （连续重复的行）
```c
-c  // --count  // prefix lines by the numberof occurences
-i  // --ignore-case 忽略大小写
-d  // --repeated  // only print duplicate lines, one for each group
```

**管道  |**  ： 把 sort 命令的输出重定向到管道，把 uniq 命令的输入重定向到管道
```c
sort a.txt | uniq
```
**管道  |   + xargs  ！！！**
**     -exec**

`file`  :  determine file type.   // 查看一个文件具体参数

`wc`   :  word count  // printt newline, word, and byte counts for each files
```c
-m 		// --chars  // print the character counts
-l 		// --lines  // print the newlines counts
-w 		// --words  // print the word counts
```

#### 2.3.18 *****搜索文件*****
`grep`  :  grep,egrep, fgrep, rgrep    print lines matching a pattern
  grep  ——  global search regular expression(RE) and print out the line

**regex : **
基本单位： 字符， 转义序列，**. **，  [abc],   (expr)  // **. **匹配除'\n'外的任意一个字符  (expr)另一个正则表达式
基本操作： 对基本单位进行的操作
连接：  "ab "   "[abc]x"     "[^abc]x"     ".txt"   "\.txt"
重复：
+ 重复最少一次 （ ≥1 ）
？重复0次 或者一次（ =0或者 =1 ）
*重复任意次数 （ ≥0 ）   " .*" // 匹配所有字符
{m}重复m次
{m,n}最少重复m次，最多重复n次
{m,  }最少重复m次
{   ,n}最多重复n次
指定基本单位出现的位置：
  ^ 行首     $ 行尾
 \< 词首    \>词尾
```c
-E  // --extended-regexp
-i  // --ignore-case  // 忽略大小写
-n  // --line-number  // 输出前加上匹配到的串的行号

grep -nE "\<t[^ ]e\>" a.txt  // t*e word

find linux-5.16.12/ -name "*.c" | xargs grep -nE "int main \(" // include "int main("  .c
```

#### 2.3.19
`alias` : define or diplay  aliases
```c
alias  h=history
```

#### 2.3.20
`history`
```c
history | tail -n 20 > history.txt
```

#### 2.3.21 查看磁盘
`df` : report file system disk space usage
disk full
```c
df -h // --human-read
```
`du` : estimate file space usage
disk used
```c
du -h 		// --human-read
du -h -d 0 	// --max-depth 0 // current dir
du -h -d 1 	// --max-depth 1 // sub dir

```

#### 2.3.21
`tar` : an archiving utility
tar ( 主选项 +辅选项 ）  目标文件名    源文件 或 目录
 主选项( ! 只能选择其中一个 )
```c
// 主选项( ! 只能选择其中一个 )
c  // --creat
r  // --append
x  // --extract  // 解压
// 辅选项
f	// 指定文件名称
v	// --verbose
z	// gzip算法压缩和解压缩
```

#### 2.3.22 远程拷贝 ( scp   -  secure copy)
使用的是 ssh 协议 , 安全协议
```c
scp src dest //
    // src 本地路径 : 绝对路径 / 相对路径
    // dest user_name@IP:dest_path

```

## 3. git
[**Git 工作区、暂存区和版本库**](https://www.runoob.com/git/git-workspace-index-repo.html)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648863259050-e2dba05b-5a36-4589-94d7-75e7b279cbc6.png)
```c
git clone

// Ctrl + X  // resolve the conflict
git init	// creat .git dir
git add .	// add all into stage/index
git status	// check files uploaded status
git pull	//
git push	//
```

# 4.  vim

change mode :
 	`insert mode`
  [esc]              ^|    i,I ,o,O,a,A
 `command mode`
V 、Ctrl+ V	^|	[esc]
 	`vusialmode`

`command mode`:
long command :  以`:`开头，以`Enter`结尾  i.e. :wq[Enter]
short command :  直接输入的字符  i.e.   i   [insert]

## 4.1 基本操作
### 4.1.1 命令模式
** 光标移动：**
** 左   下  上   右**
** h     j     k     l**

翻页：
Ctrl + B     （ backward ）	上一页
Ctrl + F     （ forward ）   	下一页
Ctrl + U     （ up ）		上半页
Ctrl + D     （ down ）		下半页

[n]-						往上n行
[n]+						往下n行
**[n]G   /  :[n]				转到第n行**

**gg				文件开始**
**GG				文件末尾**

H				页首第一行的行首
L				页尾最后一行的行首

**^				行首**
**$				行尾**

**w    next word 	下一个单词**
**b     back word	上一个单词**

### 4.2 删除字符
在命令模式下编辑文本：  删除 （ 剪切 ）
X 				删除单个字符
U          Undo 		撤销（恢复）
dd      			删除一整行
[n]dd  / d[n]d  	从光标所在行 删除n行
: x,y d			删除x行到y行
d^				删除到行首
d$				删除到行尾
dw				删除从光标处到下一个单词的开头
[n]dw  /  d[n]w   	删除n个单词
d2)				删除到 )
d2"				删除到 "

粘贴文本
P				paste
Ctrl + r  			recovery

拷贝：
yy				拷贝一行
[n]yy  / y[n]y  		拷贝n行
: x,y y			拷贝x行到y行
yw				复制一个单词
[n]yw  /  y[n]w   	复制n个单词

查找和替换
查找  :/regex
n 	下一个匹配项
N 	上一个匹配项
替换  :s/regex /substitute / 选项
默认只会替换光标所在行的第一个匹配项
g (globally) 替换光标所在行的所有匹配项

: x,ys/regex/substitute/g	替换x行到y行的所有匹配项
: %s/regex/substitute/g		替换全文的所有匹配项

### 4.1.2 编辑模式（插入模式） —— 所见即所得
命令模式    ----- i I a A o O ---->  插入模式
i  	在光标前面插入
I 	在行首插入
a	在光标后插入
A	在行尾插入
o	在下一行插入
O 	在上一行插入

### 4.1.3 视图模式（Visual） —— 选择范围
行优先 		     V
列选择   		Ctrl + V
选择以后  :   y  -  拷贝 	  d  -  删除

批量注释

- 将光标移动到要注释的第一行
- Ctrl + V 进入列选模式
- 输入`I`
- 输入 `//`
- [Esc]

批量删除  :

- 将光标移动到要删除注释的第一行
- 按ctrl v 进入竖选模式
- 选中所有注释符号
- 按d
- 按esc

全文代码对齐 ： gg=G

## 4.2对文件操作
:w  		保存    ( Ctrl + s  僵死)   Ctrl + q 退出
:q 		没更改，直接退出
:q!		不保存修改，退出
:wq		保存修改，退出

## 4.3窗口
### 4.3.1 上下窗口
:**new** filename
:split  filename
:sp   filename

Crtl + w  +  w 切换窗口

退出：
:q 		关闭光标所在窗口
:qa		关闭所有窗口

### 4.3.2 左右窗口：
**:vnew (vertical new)   filename**
**:vsplitc ** filename
**:vsp  ** filename

### 4.3.3 多标签窗口：
**：tabnew  filename**
**gt		下一个**
**gT**		**上一个**

:q 		关闭光标所在窗口
:qa		关闭所有窗口

特别提示：在浏览本教程时，不要强行记忆。记住一点：在使用中学习。
特别提示：切记您要在使用中学习，而不是在记忆中学习。

| **快捷键** | **功能** |
| --- | --- |
| h、j、k、l | 左、下、上、右 |
| <ESC> | 进入命令模式 |
| :q! <回车> | 丢弃改动，退出编辑器 |
| x | 删除光标所在位置的字符 |
| i | 插入文本 |
| A | 在行尾插入文本 |
| wq | 保存文件并退出 |
| dw | 从光标处删除至一个单词的末尾 |
| d$ | 从当前光标删除到行 |
| w | 从当前光标当前位置直到下一个单词起始处，不包括它的第一个字符 |
| e | 从当前光标当前位置直到单词末尾，包括最后一个字符 |
| $ | 从当前光标当前位置直到当前行末 |
| d number(数字) motion | 在组合中动作之前插入一个数字以 删除更多 |
| dd | 可以删除整一个当前行 |
| u | 撤消最后执行的命令 |
| U | 撤消对整行的修 |
| dw | 从当前光标删除至下一个单词 |
| d$ | 从当前光标删除至当前行末尾 |
| 0 | 移动光标到行首 |
| CTRL-R | 欲撤消以前的撤消命令，恢复以前的操作结果 |
| p | 将最后一次删除的内容置入光标之后 |
| r 和一个字符 | 替换光标所在位置的字 |
| ce | 改变文本直到一个单词的末尾 |
| CTRL-G | 显示当前编辑文件中当前光标所在行位置以及文件状态信 |
| G | 直接跳转到文件中的某一指定行 |
| 输入 / 加上一个字符串 | 在当前文件中查找该字符串 |
| n | 查找同上一次的字符串，只需要按 n 键 |
| N | 向相反方向查找同上一次的字符串 |
| ? 代替 / | 逆向查找字符 |
| CTRL-O | 回到您之前的位置 |
| CTRL-I | 跳转到较新的位置 |
| % | 查找配对的括号 )、]、} |
| :s/old/new/g | 替换 old 为 new |
| :#,#s/old/new/g | 其中 #,# 代表的是替换操作的若干行中首尾两行的行号。 |
| :%s/old/new/g | 则是替换整个文件中的每个匹配串 |
| :%s/old/new/gc | 会找到整个文件中的每个匹配串，并且对每个匹配串提示是否进行替换 |
| 输入 :! 然后紧接着输入一个外部命令 | 可以执行该外部命令 |
| :w FILENAME | 将对文件的改动保存到文件中 |
| v motion :w FILENAME | 保存文件的部分内容 |
| :r FILENAME | 提取磁盘文件 FILENAME 并将其插入到当前文件的光标位置后面 |
| :r !ls | 读取 ls 命令的输出，并把它放置在光标下面 |
| o | 在光标的下方打开新的一行并进入插入模式 |
| O | 在光标 _上方_ 打开新的一行 |
| a | 在光标之后插入文本 |
| R | 可连续替换多个字符 |
| y,p | y 复制文本，使用 p 粘贴文本 |
| :set ic | 忽略大小写 |
| :set noic | 禁用忽略大小写 |
| set hls is | 匹配项的高亮显示 |
| :nohlsearch | 移除匹配项的高亮显示 |
| :help | 帮助 |
| :edit ~/.vimrc | 编辑 vimrc 文件 |
|  |  |

## 4.4 vim设置
~/.vimrc   ( running command     vim启动时会读取这个文件,并执行里面的命令 )

## 4.5 vimtutor
