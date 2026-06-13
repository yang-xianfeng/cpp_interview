$ man man
  下表显示了手册的 章节 号及其包含的手册页类型。

       1   可执行程序或 shell 命令
      ** 2   系统调用(内核提供的函数)**
**       3   库调用(程序库中的函数)**
       4   特殊文件(通常位于 /dev)
       5   File formats and conventions, e.g. /etc/passwd
       6   游戏
 **      7   杂项(包括宏包和规范，如 man(7)，groff(7))**
       8   系统管理命令(通常只针对 root 用户)

名字 - 声明 - 细节 - 返回值
1.阅读名字
2.看声明和返回值

   - 头文件
   - 指针类型的参数
      - const：该函数不会修改指向的内容  传入参数
      - 无const：	会修改			  传入传出参数

惯用法：先定义变量，然后取地址&给被调函数

   - 指针类型的返回值：主调函数是否释放内存
      - fopen：
      - malloc、realloc、calloc：
   - 返回值不实现具体功能，只有来处理错误。

3.细节 按需查看
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649296696418-7563d774-f3f6-4d51-8231-f5c8c1abc960.png)
# 1. 文件
狭义：存储在外部存储介质上的数据集合
广义：读取速度慢、存储容量大、可以持久存储

文件类型： 普通文件、目录文件、链接文件、 字符设备文件、块设备文件、 管道文件、  socket

自定义头文件
宏定义
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <stdbool.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <dirent.h>
#include <pwd.h>
#include <grp.h>
#include <time.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/select.h>
#include <sys/time.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>
#include <sys/msg.h>
#include <signal.h>
#include <pthread.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <netdb.h>
#include <sys/epoll.h>
#include <sys/uio.h>
#include <sys/sendfile.h>

// splice()
#define _GNU_SOURCE /* See feature_test_macros(7) */

// error check
#define ARGS_CHECK(argc, num)                 \
    {                                         \
        if (argc != num)                      \
        {                                     \
            fprintf(stderr, "args error!\n"); \
            return -1;                        \
        }                                     \
    }
#define ERROR_CHECK(ret, num, msg) \
    {                              \
        if (ret == num)            \
        {                          \
            perror(msg);           \
            return -1;             \
        }                          \
    }
#define THREAD_ERROR_CHECK(ret, msg)                        \
    {                                                       \
        if (ret != 0)                                       \
        {                                                   \
            fprintf(stderr, "%s:%s\n", msg, strerror(ret)); \
        }                                                   \
    }

```
### 1.1 日志系统
"a"  	  // append 只写追加，默认从文件结尾写入
"a+"  // 读写追加     读入时ptr会到文件开始，写入时ptr跳到文件的末尾
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649229715377-dbfd944d-0602-452b-a0c1-b25802304fcc.png)

### 1.2 修改文件权限 chmod  0777（八进制）
#include <sys/stat.h> // linux下才有
#include <sys/types.h>
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    //./chmod 777 dir1
    ARGS_CHECK(argc,3);
    //chmod(argv[2],argv[1]);
    mode_t mode;
    sscanf(argv[1], "%o",&mode);
    int ret = chmod(argv[2],mode);
    ERROR_CHECK(ret,-1,"chmod");
}
```

### 1.3 getcwd  -  get current working directory
#include <unistd.h>  // 继承自Unix
char *getcwd(char *buf, size_t size);
```c
#include <myhead.h>
int main(){
    //char buf[1024] = {0};
    //char * ret = getcwd(buf,sizeof(buf));
    //ERROR_CHECK(ret,NULL,"getcwd");
    //printf("ret = %p, ret = %s\n", ret, ret);
    //printf("buf = %p, buf = %s\n", buf, buf);

    // getcwd(NULL,0) 系统自动分配堆空间
    printf("cwd = %s\n", getcwd(NULL,0));//不free的话会内存泄漏
}
```

buf不为空，直接返回buf
buf为空，返回一个堆空间的指针
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649232881084-1882801a-c184-4731-9398-69aa976727ed.png)

### 1.4 chdir  -  change working directory
#include <unistd.h>

int chdir(const char *path);
int fchdir(int fd);
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    //./chdir dir1
    printf("before chdir, cwd = %s\n", getcwd(NULL,0));
    int ret = chdir(argv[1]);
    ERROR_CHECK(ret,-1,"chdir");
    printf("after chdir, cwd = %s\n", getcwd(NULL,0));
}
```
current working directory 是进程的属性
父进程
子进程

### 1.5rmdir mkdir
#include <sys/stat.h> // linux下才有
#include <sys/types.h>
所有创建文件的行为 都会受到`umask`的影响
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    int ret = mkdir(argv[1],0777);
    //所有创建文件的行为都会受到umask的影响
    ERROR_CHECK(ret,-1,"mkdir");
}
```

```c
#include <myhead.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    int ret = rmdir(argv[1]);
    ERROR_CHECK(ret,-1,"rmdir");
}
```

### 1.6 流 (stream)  用户在不了解结构的情况下访问所有数据
**C++  itearator**
目录在磁盘中，以**链表**的形式进行存储。
每一个**链表结点（目录项）**，存储了孩子的基本信息。

目录流：目录文件在内存中的缓冲区。
`opendir`：open a directory
#include <sys/types.h>
#include <dirent.h>
DIR *opendir(const char *name);

`closedir`:  close a directory
#include <sys/types.h>
#include <dirent.h>
int closedir(DIR *dirp);

`readdir`: read a directory
#include <dirent.h>
struct dirent *readdir(DIR *dirp);
```c
struct dirent { // 可变数组
      ino_t          d_ino;       /* Inode number *///磁盘
      off_t          d_off;       /* Not an offset; see below */ // next ptr
      unsigned short d_reclen;    /* Length of this record */ // current node size
      unsigned char  d_type;      /* Type of file; not supported
                                     by all filesystem types */ // file type
      char           d_name[256]; /* Null-terminated filename */ // file name
};
```
struct dirent {
               ino_t          d_ino;       /* Inode number */
               off_t          d_off;       /* Not an offset; see below */
               unsigned short d_reclen;    /* Length of this record */
               unsigned char  d_type;      /* Type of file; not supported
                                              by all filesystem types */
               char           d_name[256]; /* Null-terminated filename */
           };
If the end of the directory stream is reached, NULL is returned and errno is not changed.  If an error occurs,  NULL is returned and errno is set appropriately.

**数据段 静态区 **：全局变量、结构体指针返回值
普通文件 type = 4       目录文件 type = 8

### 1.7 telldir & seekdir
```c
#include <43func.h>
int main(int argc, char *argv[]){
    // ./myLs dir
    ARGS_CHECK(argc,2);
    DIR *dirp = opendir(argv[1]);
    ERROR_CHECK(dirp,NULL,"opendir");
    struct dirent * pdirent;
    while((pdirent = readdir(dirp)) != NULL){
        printf("inode = %ld, reclen = %d, type = %d, name = %s\n",
            pdirent->d_ino,pdirent->d_reclen, pdirent->d_type, pdirent->d_name);
    }
    closedir(dirp);
}
```

`telldir`:  获取ptr的位置 loc
`seekdir`(   ,loc )
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    // ./myLs dir
    ARGS_CHECK(argc,2);
    DIR *dirp = opendir(argv[1]);
    ERROR_CHECK(dirp,NULL,"opendir");
    struct dirent * pdirent;
    long loc;
    while((pdirent = readdir(dirp)) != NULL){
        if(strcmp(pdirent->d_name,"file2") == 0){
            loc = telldir(dirp);
        }
        printf("inode = %ld, reclen = %d, type = %d, name = %s\n",
            pdirent->d_ino,pdirent->d_reclen, pdirent->d_type, pdirent->d_name);
    }
    puts("----------------------------------------------------");
    seekdir(dirp,loc);
    pdirent = readdir(dirp);
    printf("inode = %ld, reclen = %d, type = %d, name = %s\n",
        pdirent->d_ino,pdirent->d_reclen, pdirent->d_type, pdirent->d_name);
    closedir(dirp);
}
```

`rewinddir `
#include <sys/types.h>
#include <dirent.h>
void rewinddir(DIR *dirp);
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    // ./myLs dir
    ARGS_CHECK(argc,2);
    DIR *dirp = opendir(argv[1]);
    ERROR_CHECK(dirp,NULL,"opendir");
    struct dirent * pdirent;
    while((pdirent = readdir(dirp)) != NULL){
        printf("inode = %ld, reclen = %d, type = %d, name = %s\n",
            pdirent->d_ino,pdirent->d_reclen, pdirent->d_type, pdirent->d_name);
    }
    puts("----------------------------------------------------");
    rewinddir(dirp);
    pdirent = readdir(dirp);
    printf("inode = %ld, reclen = %d, type = %d, name = %s\n",
        pdirent->d_ino,pdirent->d_reclen, pdirent->d_type, pdirent->d_name);
    closedir(dirp);
}
```

### 1.8 stat
int stat (const char *pathname, struct stat *statbuf)
文件名和路径名**不对等**（**当前目录**下**才相同**）
被调函数通过 传入传出参数给主调函数传递信息
```c
struct stat {
    dev_t     st_dev;         /* ID of device containing file */
    ino_t     st_ino;         /* Inode number */
    mode_t    st_mode;        /* File type and mode */
    nlink_t   st_nlink;       /* Number of hard links */
    uid_t     st_uid;         /* User ID of owner */
    gid_t     st_gid;         /* Group ID of owner */
    dev_t     st_rdev;        /* Device ID (if special file) */
    off_t     st_size;        /* Total size, in bytes */
    blksize_t st_blksize;     /* Block size for filesystem I/O */
    blkcnt_t  st_blocks;      /* Number of 512B blocks allocated */

    /* Since Linux 2.6, the kernel supports nanosecond
     precision for the following timestamp fields.
     For the details before Linux 2.6, see NOTES. */

    struct timespec st_atim;  /* Time of last access */
    struct timespec st_mtim;  /* Time of last modification */
    struct timespec st_ctim;  /* Time of last status change */

    #define st_atime st_atim.tv_sec /* Backward compatibility */
    #define st_mtime st_mtim.tv_sec
    #define st_ctime st_ctim.tv_sec
};

$ file file1.name
-rwxrwxr-x  1     usr1	  usr1	  126	Apr 2 18:32  file1.name
st_mode st_nlink st_uid st_gid st_blksize st_mtime dirent_name
```
```c
printf("File type:                ");

    switch (sb.st_mode & S_IFMT) {
    case S_IFBLK:  printf("block device\n");       break; // b
    case S_IFCHR:  printf("character device\n");   break; // c
    case S_IFDIR:  printf("directory\n");          break; // a
    case S_IFIFO:  printf("FIFO/pipe\n");          break; // p
    case S_IFLNK:  printf("symlink\n");            break; // l
    case S_IFREG:  printf("regular file\n");       break; // -
    case S_IFSOCK: printf("socket\n");             break; // s
    default:       printf("unknown?\n");           break; // ?
}
```

`getpwuid`:
#include <sys/types.h>
#include <pwd.h>
struct passwd *getpwuid(uid_t uid);
```c
// cat /etc/passwd
struct passwd {
    char   *pw_name;       /* username */
    char   *pw_passwd;     /* user password */
    uid_t   pw_uid;        /* user ID */
    gid_t   pw_gid;        /* group ID */
    char   *pw_gecos;      /* user information */
    char   *pw_dir;        /* home directory */
    char   *pw_shell;      /* shell program */
};
```

`getgrgid`:
#include <sys/types.h>
#include <grp.h>
struct group *getgrgid(gid_t gid);
```c
// cat /etc/group
struct group {
    char   *gr_name;        /* group name */
    char   *gr_passwd;      /* group password */
    gid_t   gr_gid;         /* group ID */
    char  **gr_mem;         /* NULL-terminated array of pointers
                             to names of group members */
};
```

日历时间
#include <time.h>
char *ctime(const time_t *timep);			// 标准日历（固定格式）
struct tm *gmtime(const time_t *timep);	// 格林威治时间
struct tm *localtime(const time_t *timep);	// 本时区时间
```c
struct tm {
    int tm_sec;    /* Seconds (0-60) */
    int tm_min;    /* Minutes (0-59) */
    int tm_hour;   /* Hours (0-23) */
    int tm_mday;   /* Day of the month (1-31) */
    int tm_mon;    /* Month (0-11) */
    int tm_year;   /* Year - 1900 */
    int tm_wday;   /* Day of the week (0-6, Sunday = 0) */
    int tm_yday;   /* Day in the year (0-365, 1 Jan = 0) */
    int tm_isdst;  /* Daylight saving time */
};
```

自己实现 ls
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    // ./myLs dir
    ARGS_CHECK(argc,2);
    DIR *dirp = opendir(argv[1]);
    ERROR_CHECK(dirp,NULL,"opendir");
    struct dirent * pdirent;
    struct stat statbuf;
    int ret = chdir(argv[1]);
    ERROR_CHECK(ret,-1,"chdir");
    while((pdirent = readdir(dirp)) != NULL){
        ret = stat(pdirent->d_name,&statbuf);//文件名只有在当前目录下才是路径
        ERROR_CHECK(ret,-1,"stat");
        printf("%6o %ld %s %s %8ld %s %s\n",
            statbuf.st_mode,
            statbuf.st_nlink,
            getpwuid(statbuf.st_uid)->pw_name,
            getgrgid(statbuf.st_gid)->gr_name,
            statbuf.st_size,
            ctime(&statbuf.st_mtime),
            pdirent->d_name);
    }
    closedir(dirp);
}
```

#### 1.9 自己实现tree命令
深度优先遍历 （ 栈 / 递归 实现）
```c
#include <myhead.h>
int DFSprint(char *path, int width);
int main(int argc, char *argv[]){
    // ./mytree dir
    ARGS_CHECK(argc,2);
    // print root
    puts(argv[1]);
    // DFS
    DFSprint(argv[1],4);
}
int DFSprint(char *path, int width){
    DIR* dirp = opendir(path);
    ERROR_CHECK(dirp,NULL,"opendir");
    struct dirent *pdirent;
    char newPath[1024] = {0};
    while((pdirent = readdir(dirp)) != NULL){
        if(strcmp(pdirent->d_name,".") == 0 ||
            strcmp(pdirent->d_name,"..") == 0){
                continue;
            }
        printf("├");
        for(int i = 1; i < width; ++i){
            printf("─");
        }
        puts(pdirent->d_name);
        if(pdirent->d_type == DT_DIR){
            sprintf(newPath,"%s%s%s",path,"/",pdirent->d_name);
            //printf("newPath = %s\n", newPath);
            DFSprint(newPath,width+4);
        }
    }
}
```

#### 1.10 文件
内核 中的 文件 （文件流、用户态文件缓冲区） 需要通过
fopen/fclose/fread/fwrite等库函数，最终通过 系统调用 使用 内核态功能。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649315293566-47e8e89a-ba9f-41d7-a3cc-e535cd645deb.png)

不带用户态缓冲区的 文件流/ FILE
给用户使用的是**文件描述符(fd)**所在位置 文件指针数组 所存的地址，封装在内核里。
`stdin`0    	`stdout`1      `stderr`2   已用前三个文件描述符。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649315316429-61f94d54-3ccb-476d-b6cf-5e3b2eef6178.png)

### 1.11 `open`
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int open(const char *pathname, int flags);
int open(const char *pathname, int flags, mode_t mode);
return file_descriptor 					mode

flags  int  32bit

| 0 | 0 | ... | 0 | 1 | 0 | ... | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- |

**每一个属性的某些位为1，其余是0 **
多个独立属性共存，使用 `**|**`**(按位或)**

      掩码             含义
**O_RDONLY  	以只读的方式打开 **
**O_WRONLY  	以只写的方式打开 **
**O_RDWR 	以读写的方式打开 **
**//  必须三选一，三个彼此互斥 **
O_CREAT		如果文件不存在，则创建文件
  使用 int open(const char *pathname, int flags, mode_t mode);
O_EXCL		仅与O_CREAT连用，如果文件已存在，则open失败
O_TRUNC	如果文件存在，将文件的长度截至0**（清空文件内容）**
O_APPEND	已追加的方式打开文件，每次调用write时，文件指针自动先移到文件尾，用于 多进程写同一个文件的情况。
O_NONBLOCK/O_NDELAY 对管道、设备文件和socket使用，以非阻塞方式打开文件，无论有无数据读取 或等待，都会立即返回进程之中
O_SYNC 		同步打开文件，只有在数据被真正写入物理设备设备后才返回
~~O_ASYNC 	对管道、设备文件和socket使用，开启信号驱动IO。一旦可读或者可写发送信号 （过于复杂） ~~

```c
#include <myhead.h>
int main(int argc, char *argv[]){
    // ./open file1
    ARGS_CHECK(argc,2);
    int fd = open(argv[1], O_WRONLY);
    ERROR_CHECK(fd, -1, "open");
    printf("fd = %d\n", fd);
    close(fd);
}
```
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    // ./open file1
    ARGS_CHECK(argc,2);
    //创建文件的行为，总是会受到umask的影响
    int fd = open(argv[1], O_WRONLY|O_CREAT,0666);
    ERROR_CHECK(fd, -1, "open");
    printf("fd = %d\n", fd);
    close(fd);
}
```
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    // ./open file1
    ARGS_CHECK(argc,2);
    int fd = open(argv[1], O_WRONLY|O_CREAT|O_EXCL,0666);
    ERROR_CHECK(fd, -1, "open");
    printf("fd = %d\n", fd);
    close(fd);
}
```

**注：**
  `fopen` is opened as if by a call to `open`:
              │fopen() mode │ open() flags
              │     r      		│ O_RDONLY
              │     w     	        │ O_WRONLY | O_CREAT | O_TRUNC
              │     a    	        │ O_WRONLY | O_CREAT | O_APPEND
              │     r+ 	        │ O_RDWR
              │     w+	        │ O_RDWR | O_CREAT | O_TRUNC
              │     a+  	        │ O_RDWR | O_CREAT | O_APPEND

`read`
**read前**需要先**清空**缓存数组**buf**
ssize_t read(int fd, void *buf, size_t count);
  传入传出参数
count是应当申请内存的大小（字节上限）
文本文件：底层是ASCII的序列，以字符串形式读写
二进制文件： 底层是0/1序列
注意：怎么写就怎么读

read的返回值   ≤ count

- >0	成功读取的字符数
- =0	EOF
- =-1	报错
```c
#include <myhaed.h>
int main(int argc, char *argv[]){
    // ./open file1
    ARGS_CHECK(argc,2);
    int fd = open(argv[1], O_RDWR);
    ERROR_CHECK(fd, -1, "open");
    printf("fd = %d\n", fd);
    // str
    char buf[10] = {0};
    ssize_t ret = read(fd,buf,sizeof(buf));
    puts(buf);
    close(fd);
}
```
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    // ./open file1
    ARGS_CHECK(argc,2);
    int fd = open(argv[1], O_RDWR);
    ERROR_CHECK(fd, -1, "open");
    printf("fd = %d\n", fd);
    // binary
    int i;
    read(fd,&i,sizeof(i));
    printf("i = %d\n", i);
    close(fd);
}
```

`write`
**read前**需要先**清空**缓存数组**buf**
ssize_t write(int fd, const void *buf, size_t count);
  传入参数
count是应当申请内存的大小（字节上限）
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    // ./open file1
    ARGS_CHECK(argc,2);
    int fd = open(argv[1], O_RDWR);
    ERROR_CHECK(fd, -1, "open");
    printf("fd = %d\n", fd);
    // 这里如果是字符串，就是文本文件
    char buf[10] = "hello";
    write(fd,buf,strlen(buf));
    close(fd);
}
```
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    // ./open file1
    ARGS_CHECK(argc,2);
    int fd = open(argv[1], O_RDWR);
    ERROR_CHECK(fd, -1, "open");
    printf("fd = %d\n", fd);
    // binary
    int i = 10000000;
    write(fd,&i,sizeof(i));
    close(fd);
}
```

`cp`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649496065778-4b50ca11-0603-462c-8906-363f27dc133f.png)
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    //./cp src dst
    ARGS_CHECK(argc,3);
    int fdr = open(argv[1],O_RDONLY);
    ERROR_CHECK(fdr,-1,"open fdr");
    int fdw = open(argv[2],O_WRONLY|O_CREAT|O_TRUNC,0666);
    ERROR_CHECK(fdw,-1,"open fdw");
    char buf[4096] = {0};
    while(1){
        memset(buf,0,sizeof(buf));
        ssize_t ret = read(fdr,buf,sizeof(buf));
        if(ret == 0){
            break;
        }
        write(fdw,buf,ret);//第三个参数是ret，表示读多少写多少
    }
    close(fdr);
    close(fdw);
}
```

性能分析：
buf越大越好，减少状态切换带来的开销 **（4096）**
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649496325882-d1c95d72-32cb-440b-a6f5-422e6cf76cd4.png)
使用`fopen` `fread` `fwrite`文件系统
优势： 零碎的写入时只少量的系统调用
劣势：拷贝数据次数过多
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649496343389-b4455ffe-2828-45bf-b89c-ee74af7af77b.png)

#### 1.12 杂项
`ftruncate`： 创建一个固定大小的文件
```c
#include <myhead.h>
int main(int argc,char *argv[]){
    ARGS_CHECK(argc,2);
    int fd = open(argv[1], O_RDWR);
    ERROR_CHECK(fd,-1,"open");
    int ret = ftruncate(fd,40960);
    ERROR_CHECK(ret,-1,"ftruncate");
}
```
大 -> 小 		截断低位
小 -> 大 		低位补0 ( **文件空洞**  4096分配空间)

#### 1.13 内存映射 `mmap`
#include <sys/mman.h>
void *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset);
void *		return adress   (失败：MAP_FAILED)
void *add	NULL(分配在堆上）
size_t length	大小固定
int prot		PROT_READ/PROT_WRITE
int flags		属性（MAP_SHARED)
int fd		映射地址
off_t offset	0

int munmap(void *addr, size_t length);
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649511932357-b2c45bc6-6216-497a-b5ca-5a438b24e300.png)
在用户态空间分配一片空间，该内存直接和外设建立映射。
可以使用*/[ ]  `<=>` 读写文件。

限制：

- 文件大小固定（ftruncate）
- 只能是磁盘文件
- 建设映射之前先open

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649512278371-f2c6e44c-a785-410e-b562-d74dd1973730.png)
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    int fd = open(argv[1],O_RDWR);
    ERROR_CHECK(fd,-1,"open");
    int ret = ftruncate(fd,5);
    ERROR_CHECK(ret,-1,"ftruncate");
    char *p = (char *)mmap(NULL,5,PROT_READ|PROT_WRITE,MAP_SHARED,fd,0);
    ERROR_CHECK(p,MAP_FAILED,"mmap");
    for(int i = 0;i <5; ++i){
        printf("%c", p[i]);
    }
    printf("\n");
    p[0] = 'H';
    munmap(p,5);
}
```

`lseek`
off_t lseek (int fd, off_t offset, int whence)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649512777650-a28f5aaa-a3e4-482c-9a23-d6a76573549f.png)
```c
#include <43func.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    int fd = open(argv[1], O_RDWR);
    ERROR_CHECK(fd,-1,"open");
    lseek(fd,40960,SEEK_SET);
    write(fd,"1",1);
    close(fd);
}
```
**文件空洞**

#### 1.15 文件流的底层是使用了文件对象
以下展示混用，实际并没什么用（炫技而已）
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    FILE *fp = fopen(argv[1],"r+");
    ERROR_CHECK(fp,NULL,"fopen");
    printf("fileno = %d\n", fileno(fp));
    //int ret = write(3,"hello",5);//3是魔法数
    int ret = write(fp->_fileno,"hello",5); //代码即注释
    ERROR_CHECK(ret,-1,"write");
    fclose(fp);
}
```
fp->_fileno  不可随意操作，封装接口
int fileno(FILE *stream);
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    FILE *fp = fopen(argv[1],"r+");
    ERROR_CHECK(fp,NULL,"fopen");
    printf("fileno = %d\n", fileno(fp));
    //int ret = write(3,"hello",5);//3是魔法数
    //int ret = write(fp->_fileno,"hello",5); //代码即注释
    int ret = write(fileno(fp),"hello",5); //面向接口编程
    ERROR_CHECK(ret,-1,"write");
    fclose(fp);
}
```

#### 1.16 验证文件描述符
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649513750884-cf918922-e44c-4f3b-885e-a0120e1006d3.png)
printf  -> write( )
先close 1， 再open一个文件（该文件的fd是1）
再使用printf  -> write( 1 )， 则输出到该文件 （即重定向）
```c
#include <myhead.h>
int main(){
    printf("fd of stdin = %d\n", fileno(stdin));
    printf("fd of stdout = %d\n", fileno(stdout));
    printf("fd of stderr = %d\n", fileno(stderr));
    //write(1,"hello",5);
    write(STDOUT_FILENO,"hello",5);
}
```

修改文件描述符
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    printf("You can see me!\n");
    close(STDOUT_FILENO);
    int fd = open(argv[1], O_RDWR);
    ERROR_CHECK(fd, -1, "open");
    printf("fd = %d\n", fd);
}
```

文件描述符的复制

- 数值上不同
- 偏移量共享

int dup(int oldfd);  // 选择一个最小可用的文件描述符，和oldfd同指向
int dup2(int oldfd, int newfd);  // 将newfd和oldfd指向同一个文件对象
  （如果 newfd 已经有指向，就会自动close）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649513763929-750bdecb-5c8c-4361-a10b-522cb51e6564.png)
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    int oldfd = open(argv[1],O_RDWR);
    ERROR_CHECK(oldfd,-1,"open");
    printf("oldfd = %d\n", oldfd);
    int newfd = dup(oldfd);
    printf("newfd = %d\n", newfd);

    // 共享偏移量
    //write(oldfd,"hello",5);
    //write(newfd,"world",5);
    //close(oldfd);

    // 其中一个关闭 不影响其他 (引用计数 (C++智能指针))
    write(oldfd,"hello",5);
    close(oldfd);
    write(newfd,"world",5);
}
```

重定向
```c
#include <myhead.h>
int main(int argc, char *argv[]){
    printf("\n");
    ARGS_CHECK(argc,2);
    int oldfd = open(argv[1],O_RDWR);
    ERROR_CHECK(oldfd,-1,"open");
    close(STDOUT_FILENO);
    int newfd = dup(oldfd);
    printf("oldfd = %d\n", oldfd);
    printf("newfd = %d\n", newfd);
}
```

int dup2(int oldfd, int newfd);  // 将newfd和oldfd指向同一个文件对象
  （如果 newfd 已经有指向，就会自动close）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649516876979-3fb2d798-5ecf-48a1-a347-476285d32855.png)

1. dup2(1,5);
1. dup2(3,1);
1. dup2(5,1);
```c
#include <43func.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    int oldfd = open(argv[1],O_RDWR);
    ERROR_CHECK(oldfd,-1,"open");
    printf("You can see me!\n");
    int savefd = 5;
    dup2(STDOUT_FILENO,savefd);
    dup2(oldfd,STDOUT_FILENO);
    printf("You can't see me!\n");
    dup2(savefd,STDOUT_FILENO);
    printf("You can see me!\n");
}
```

#### 1.20 有名管道 ( named pipe / FIFO )
是进程间通信机制在文件系统的映射
传输方式：单工 / 半双工 / 全双工
`mkfifo` - make FIFOs ( named pipes )

用系统调用操作管道
open :  O_RDONLY 读端		  O_WRONLY 写端

```c
#include <43func.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    // open 会导致阻塞
    int fdr = open(argv[1], O_RDONLY);
    ERROR_CHECK(fdr,-1,"open");
    puts("pipe open!");
    char buf[10] = {0};
    read(fdr,buf,sizeof(buf));
    puts(buf);
    close(fdr);
}

#include <43func.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    int fdw = open(argv[1], O_WRONLY);
    ERROR_CHECK(fdw,-1,"open");
    puts("pipe open!");
    write(fdw,"hello",5);
    close(fdw);
}
```
当一个进程打开（ open ）了管道一端的时候，
如果对端未被打开，进程处于阻塞状态，直到对端被另一个进程打开。

#### #死锁 ( 循环等待)
```c
int main(int argc, char *argv[]){
    // .chat1 1.pipe 2.pipe
    ARGS_CHECK(argc,3);
    int fdr = open(argv[1], O_RDONLY);
    int fdw = open(argv[2], O_WRONLY);
    puts("pipe open!");
}

int main(int argc, char *argv[]){
    // .chat2 2.pipe 1.pipe
    ARGS_CHECK(argc,3);
    int fdr = open(argv[1], O_RDONLY);
    int fdw = open(argv[2], O_WRONLY);
    puts("pipe open!");
}
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649572394273-73204a03-2eef-4007-a7aa-898cf1abba51.png)
死锁 占用资源出现问题  （调整顺序 可以解决这类死锁）
```c
int main(int argc, char *argv[]){
    // .chat1 1.pipe 2.pipe
    ARGS_CHECK(argc,3);
    int fdr = open(argv[1], O_RDONLY);
    int fdw = open(argv[2], O_WRONLY);
    puts("pipe open!");
}

int main(int argc, char *argv[]){
    // .chat2 1.pipe 2.pipe
    ARGS_CHECK(argc,3);
    int fdw = open(argv[1], O_WRONLY);
    int fdr = open(argv[2], O_RDONLY);
    puts("pipe open!");
}
```

```c
int main(int argc, char *argv[]){
    // ./chat1 1.pipe 2.pipe
    ARGS_CHECK(argc,3);
    int fdr = open(argv[1], O_RDONLY);
    int fdw = open(argv[2], O_WRONLY);
    puts("pipe open");
    char buf[4096] = {0};
    while(1){
    memset(buf,0,sizeof(buf));
    read(fdr,buf,sizeof(buf));
    puts(buf);
    memset(buf,0,sizeof(buf));
    read(STDIN_FILENO,buf,sizeof(buf));
    write(fdw,buf,strlen(buf));
}

int main(int argc, char *argv[]){
    // .chat2 1.pipe 2.pipe
    ARGS_CHECK(argc,3);
    int fdw = open(argv[1], O_WRONLY);
    int fdr = open(argv[2], O_RDONLY);
    puts("pipe open!");
    char buf[4096] = {0};
    while(1){
    memset(buf,0,sizeof(buf));
    read(fdr,buf,sizeof(buf));
    puts(buf);
    memset(buf,0,sizeof(buf));
    read(STDIN_FILENO,buf,sizeof(buf));
    write(fdw,buf,strlen(buf));
}
```

`I/O`多路复用  ( `select` )
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
int select(int nfds, fd_set *readfds, fd_set *writefds,
                  fd_set *exceptfds, struct timeval *timeout);
void FD_CLR(int fd, fd_set *set);
int  FD_ISSET(int fd, fd_set *set);
void FD_SET(int fd, fd_set *set);
void FD_ZERO(fd_set *set);

select 使用流程 ( fd_set : 监听集合 )  :

1. 创建fd_set
1. 设置合适的监听 （ FD_ZERO 清空 ； FD_SET 加入监听）
1. 调用select函数，会让进程阻塞
1. 当监听的fd中，有任何一个就绪，则select就绪
1. 轮询所有监听的fd，是否就绪 FD_ISSET
```c
#include <43func.h>
int main(int argc, char *argv[]){
    // ./chat1 1.pipe 2.pipe
    ARGS_CHECK(argc,3);
    int fdr = open(argv[1], O_RDONLY);
    int fdw = open(argv[2], O_WRONLY);
    puts("pipe open");
    char buf[4096] = {0};
    fd_set rdset;
    while(1){
        FD_ZERO(&rdset);
        FD_SET(STDIN_FILENO,&rdset);
        FD_SET(fdr,&rdset);
        select(fdr+1,&rdset,NULL,NULL,NULL);
        if(FD_ISSET(fdr,&rdset)){
            puts("msg from pipe");
            memset(buf,0,sizeof(buf));
            read(fdr,buf,sizeof(buf));
            puts(buf);
        }
        if(FD_ISSET(STDIN_FILENO,&rdset)){
            puts("msg from stdin");
            memset(buf,0,sizeof(buf));
            read(STDIN_FILENO,buf,sizeof(buf));
            write(fdw,buf,strlen(buf));
        }
    }
}
```

int select(int nfds, fd_set *readfds, fd_set *writefds,
                  fd_set *exceptfds, struct timeval *timeout);
fd_set *readfds,	**传入传出参数**
select有可能**会修改**rdset，因此**每次需要重置  FD_SET**

如何找到就绪的fd

- 轮询 polling
- 回调 callback

**如果一方关闭了聊天，另一方陷入死循环**
管道一直就绪导致的
写端先关闭 	读端read会读到EOF（就绪）
读端关闭 	写端 继续write（进程崩溃 接收 SIGPIPE信号）
`Ctrl` + `D` 输入一个EOF
```c
        if(FD_ISSET(fdr,&rdset)){
            puts("msg from pipe");
            memset(buf,0,sizeof(buf));
            int ret = read(fdr,buf,sizeof(buf));
            if(ret == 0){
                printf("end!\n");
                break;
            }
            puts(buf);
        }
        if(FD_ISSET(STDIN_FILENO,&rdset)){
            puts("msg from stdin");
            memset(buf,0,sizeof(buf));
            int ret = read(STDIN_FILENO,buf,sizeof(buf));
            if(ret == 0){
                write(fdw,"nishigehaoren",13);
                break;
            }
            write(fdw,buf,strlen(buf));
        }
```
```c
#include <43func.h>
int main(int argc, char *argv[]){
    // ./chat1 1.pipe 2.pipe
    ARGS_CHECK(argc,3);
    int fdr = open(argv[1], O_RDONLY);
    int fdw = open(argv[2], O_WRONLY);
    puts("pipe open");
    char buf[4096] = {0};
    fd_set rdset;
    while(1){
        FD_ZERO(&rdset);
        FD_SET(STDIN_FILENO,&rdset);
        FD_SET(fdr,&rdset);
        // timeout
        struct timeval timeout;
        timeout.tv_sec = 2;
        timeout.tv_usec = 500000;
        int sret = select(fdr+1,&rdset,NULL,NULL,&timeout);
        if(sret == 0){
            puts("time out!");
            continue;
        }
        if(FD_ISSET(fdr,&rdset)){
            puts("msg from pipe");
            memset(buf,0,sizeof(buf));
            int ret = read(fdr,buf,sizeof(buf));
            if(ret == 0){
                printf("end!\n");
                break;
            }
            puts(buf);
        }
        if(FD_ISSET(STDIN_FILENO,&rdset)){
            puts("msg from stdin");
            memset(buf,0,sizeof(buf));
            int ret = read(STDIN_FILENO,buf,sizeof(buf));
            if(ret == 0){
                write(fdw,"nishigehaoren",13);
                break;
            }
            write(fdw,buf,strlen(buf));
        }
    }
}

#include <43func.h>
int main(int argc, char *argv[]){
    // ./chat2 1.pipe 2.pipe
    ARGS_CHECK(argc,3);
    int fdw = open(argv[1], O_WRONLY);
    int fdr = open(argv[2], O_RDONLY);
    puts("pipe open");
    char buf[4096] = {0};
    fd_set rdset;
    while(1){
        FD_ZERO(&rdset);
        FD_SET(STDIN_FILENO,&rdset);
        FD_SET(fdr,&rdset);
        select(fdr+1,&rdset,NULL,NULL,NULL);
        if(FD_ISSET(fdr,&rdset)){
            puts("msg from pipe");
            memset(buf,0,sizeof(buf));
            int ret = read(fdr,buf,sizeof(buf));
            if(ret == 0){
                printf("end!\n");
                break;
            }
            puts(buf);
        }
        if(FD_ISSET(STDIN_FILENO,&rdset)){
            puts("msg from stdin");
            memset(buf,0,sizeof(buf));
            int ret = read(STDIN_FILENO,buf,sizeof(buf));
            if(ret == 0){
                write(fdw,"nishigehaoren",13);
                break;
            }
            write(fdw,buf,strlen(buf));
        }
    }
}
```

**select的超时**
```c
struct timeval {
    long    tv_sec;     /* seconds */
    long    tv_usec;    /* microseconds */
};
```
timeout 也是 传入传出参数，每次循环开始时，要设置timeout
使用select的返回值（return 0 -> timeout )来区分超时导致的就绪
```c
struct timeval timeout;
timeout.tv_sec = 2;
timeout.tv_usec = 500000;
int sret = select(fd + 1, &rdset, NULL, NULL, &timeout);
if (sret == 0){
    puts("time out!");
    continue;
}
```

**关于管道**
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649576685657-fe243104-4fd7-473d-af50-b103ce031c73.png)
有一个进程 读管道 写管道   为避免永久阻塞  使用select

使用select同时监听读和写
```c
#include <43func.h>
int main(int argc, char *argv[]){
    ARGS_CHECK(argc,2);
    int fdr = open(argv[1],O_RDWR);
    int fdw = open(argv[1],O_RDWR);
    puts("pipe open");
    char buf[4096];
    fd_set rdset; // read
    fd_set wrset; // write
    int cnt = 0;
    while(1){
        FD_ZERO(&rdset);
        FD_SET(fdr,&rdset);
        FD_ZERO(&wrset);
        FD_SET(fdw,&wrset);
        select(fdw + 1,&rdset,&wrset,NULL,NULL);
        if(FD_ISSET(fdr,&rdset)){
            printf("read cnt = %d\n", cnt ++);
            read(fdr,buf,2048);
        }
        if(FD_ISSET(fdw,&wrset)){
            printf("write cnt = %d\n", cnt ++);
            // 4097 会导致永久阻塞
            // pipe size  读写缓冲区大小4096
            // select 认为写就绪的条件 写缓冲区为空
            write(fdw,buf,4096);
        }
        //sleep(1);
    }
}
```
_从一开始 “一读一写” 到满了以后，“两读一写”_

**select实现的原理**
```c
/* fd_set for select and pselect.  */
typedef struct
  {
    /* XPG4.2 requires this member name.  Otherwise avoid the name
       from the global namespace.  */
#ifdef __USE_XOPEN
    __fd_mask fds_bits[__FD_SETSIZE / __NFDBITS];
# define __FDS_BITS(set) ((set)->fds_bits)
#else
    __fd_mask __fds_bits[__FD_SETSIZE / __NFDBITS];
# define __FDS_BITS(set) ((set)->__fds_bits)
#endif
  } fd_set;

```
 open file  	// 1024bit  位图
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649576978398-817063df-b407-4c1f-b006-a5b029aa56cf.png)
fd_set的本质是一个**位图 **

**调用select**
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649574616184-b080b090-3c48-4407-bc6a-957caa4526c9.png)
劣势：

- 监听和就绪共用一个内存空间
- 文件数量固定，只能修改内核源码更改
- 大量用户态到内核态的拷贝
- 找到就绪的方法（轮询）浪费大量时间  ( epoll )
