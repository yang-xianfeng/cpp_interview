课程大纲：<br />vim<br />编译，汇编，链接<br />***系统编程*** <br />文件系统 ： 文件属性 、文件内容 、万物皆文件、**IO多路复用-即时聊天**<br />进程 ： 系统资源  多进程 进程间通信（管道、信号）<br />**线程 ：多线程  互斥与同步**<br />*****网络***** <br />服务器结构  ： 进程池/线程池<br />SQL语句<br />*****网盘项目*****
<a name="JvyL0"></a>
# 1. 编译&汇编&链接
IDE<br />SDK 

gcc  : GNU project C and C++ compiler<br />clang<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1648820723537-c498e252-3227-45fd-821f-b4db75b3c4a8.png#clientId=u473e819e-1289-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=254&id=N1HiP&margin=%5Bobject%20Object%5D&name=image.png&originHeight=318&originWidth=1566&originalType=binary&ratio=1&rotation=0&showTitle=false&size=187879&status=done&style=none&taskId=u5e6538ae-0f10-4382-a5b8-6e01d191100&title=&width=1252.8)
<a name="B8UWO"></a>
## 1.1预处理
作用 : 执行预处理指令<br />#include 文件包含<br />#include M 5 宏定义 ( 简单的文本替换 )<br />#include SIZE(a)   (sizeof(a) / sizeof(a[0]) )  宏函数

`$ gcc -E hello.c -o hello`<br />     -E // 预处理<br />     			   -o  // output object 目标文件名字


宏开关 :   <br />`#if    #else    #endif`<br />`$ gcc -E hello.c -o hello.i `
```c
#if 0  
    case 1; 
#else  
    case 2;
#endif
```

条件编译 : 为不同的客户或者目标平台生成不同的代码<br /> `#if  N     #else       #endif`<br />`$ gcc -E hello.c -o hello.i -D N`
```c
#if N 
    case 1; 
#else  
    case 2;
#endif
```

防御式声明 (避免重复包含多个头文件）<br />`#ifdef     #else       #endif`<br />`$ gcc -E hello.c -o hello.i `
```c
# ifndef __FOO_H__
// 可以在此写出 "foo.h" 头文件
# define N 100
...
...
...
#endif
```

<a name="WVE8j"></a>
## 1.2编译
将 C语言代码 编译成 汇编代码

两种编译方式

      - AT&T汇编
      - x86/x86_64

`$ gcc -S hello.i -o hello.s`<br />`$ gcc -S hello.c -o hello.s`

汇编 :<br />x86架构 8086     数据总线16bits     地址总线20bits<br />一个字长: 	word	 16bits<br />l :	   long word      32bits<br />       q: 	  quadra word  64bits<br />`double`   `triple`    `quadra`    `penta`

`as` :  the portable GNU assembler<br />`nm` : list symbols from object files
```c
$ as test.s -o test.o		// 
    
$ nm test.o	// 显示参数U 表示 先占位，尚未链接
```

```c
push 	// 入栈
pop		// 出栈

call 	// 函数调用
ret  	// 函数返回

mov		// 移动 (赋值)
add		// +
sub		// -    
lea // load effective address // 加载有效地址  & 
    
xor		// 
jmp		// jump // loop chieved by goto
je		// jump equal
jle		// jump less equal


%rbp   //  register of base pointer  	// 栈帧基址寄存器
%rsp   //  register of stack pointer   // 栈顶寄存器
%rbp - %rsp // 栈 向下生长   // 栈帧的大小

%eax	// 存放函数返回值, 此寄存器只有一个

%rdi   // parameter  regesiter
```

一些结论：<br />**变量的名字和类型  -->  内存位置和占空间大小（只与机器字长有关）**

**循环的底层是用 goto 实现的**

complier<br />assember
<a name="AJfCd"></a>
## 1.3 链接：
`ld` : The GNU Linker ( 直接调用)<br />gcc  间接调用	<br />链接错误 ： 函数/全局变量定义0次/全局变量超过两次  

**执行  可执行程序：**<br />**绝对路径 + 可执行程序名字**<br />**当前目录：** .**/ 可执行程序名字**

**汇编 ：gcc -C   广义编译**<br />**反汇编 ： objdump **<br />只输入** 可执行程序名字 **默认是**系统内的程序，**没有则**不执行**


<a name="bLvfl"></a>
## 1.4 库函数
|  | 文件大小 | 部署难度 | 升级难度 |
| --- | --- | --- | --- |
| 静态库 | 大 | 容易 | 难 |
| 动态库 | 小 | 难 | 容易 |

<a name="kbfyc"></a>
### 1.4.1 生成静态库
`$ gcc fun.o test.o -o test`  链接到 test 可执行程序

生成静态库 :

- 生成目标文件

`$ gcc -c func.c -o func.o `

- 打包成静态库文件

`$ ar crsv lib_name.a func.o`

- 移动到系统搜索目录  /usr/lib/
- 链接时加上 `-lfunc`

`$ gcc fun.o test.o -o test`  链接到 test 可执行程序

<a name="VySW2"></a>
### 1.4.2 生成动态库 :

- 编译成目标文件  **相对地位-位置无关代码  **`**-fpic**`

`$ gcc func.c -o func.o -fpic`

- 打包成动态库文件

`$ gcc -shared func.o -o lib_name.so`

- 移动到系统搜索目录  /usr/lib/

sudo cp lib_name.so /usr/lib

- 链接时加上 `-lfunc`

`$ gcc test.o -o test -lfunc`

**软链接 、符号链接 **<br />**$ sudo ln -s libfunc.so.0.1 libfun.so**<br />用来**更新、升级**版本  —— 好处 是可以回滚（recoll）版本

<a name="sBHdr"></a>
## 1.5 gcc的其他选项：
<a name="aHKJ2"></a>
### 1.5.1 增加搜索路径`-I` 
$ gcc src/test.c `-I` include/

参考： [gcc编译参数](https://segmentfault.com/a/1190000020325922)<br />$ gcc -I [大写字母i]寻找头文件目录 /usr/local/include      <br />$ gcc -L [大写字母l]寻找库文件 /usr/local/lib     <br />$ gcc -l word [小写字母l], 寻找动态链接库文件libword.so
<a name="Qr4Ay"></a>
### 1.5.2 编译优化`-O` 
编译优化 ：修改指令顺序和内存位置，加快执行速度<br />$ gcc test.c `-O0`   :   不作优化<br />$ gcc test.c `-O1`   :   产品常用<br />$ gcc test.c `-O2`   :   开源常用<br />$ gcc test.c `-O3`   :   优化较深，C与汇编的对应关系就变了
<a name="E1BzS"></a>
### 1.5.3 编译警告`-W` 
$ gcc src/test.c `-I` include/  `-Wall` 

<a name="u5OZJ"></a>
# 2. gdb
编译时 补充调试信息 `-g`<br />$ gdb test <br />(gdb) :
<a name="VQssW"></a>
#### 2.1 在gdb中调试
list		(l)		[file_name:] [line_number]/[func_name]  // 某行/某函数处内容	<br />run		(r)		// 运行程序		<br />break	(b)	[file_name:] [line_number]/[func_name]  // 某行/某函数处打断点	<br />continue	(c)	 	// 继续运行	<br />step		(s)		 // VS F11    逐语句：跳入自定义函数内部执行<br />next		(n)		 // VS F10    逐过程，函数直接执行<br />finsh       (fin)		 // 跳出本次函数调用

info break(i b)	// 查看断点信息

delete  [num] 		// delete breakpoint num line <br />delete			// delete all<br />ignore [num] [count] // 忽略num处断点count次

<a name="aGJ6M"></a>
#### 2.2 在gdb中查看监视	
print(p)  表达式 <br />display   表达式  // 然后每次都会自动输出所监视的变量

先 info display<br />再 undisplay  display_num

<a name="zFjC6"></a>
#### 2.3 在gdb中查看内存	
help x    // for help<br />FMT<br />repeat count :  多少个单位<br />format letter : 

      - o 	  //  八进制 
      - x   	  //  十六进制 
      - d 	  //  十进制 
      - u 	  //  无符号
      - t  	  //  二进制 

size letter : 

      - b	// 1b
      - h	 // 2b
      - w	 // 4b
      - g	 // 8b

<a name="h7UIC"></a>
#### 2.4 检查崩溃的程序
`core` core 文件 —— 程序崩溃时内存的堆栈<br />segementation fault<br />stack overflow

```c
$ ulimit -a
-t: cpu time (seconds)              unlimited
-f: file size (blocks)              unlimited
-d: data seg size (kbytes)          unlimited
-s: stack size (kbytes)             8192
-c: core file size (blocks)         0
-m: resident set size (kbytes)      unlimited
-u: processes                       7823
-n: file descriptors                1024
-l: locked-in-memory size (kbytes)  64
-v: address space (kbytes)          unlimited
-x: file locks                      unlimited
-i: pending signals                 7823
-q: bytes in POSIX msg queues       819200
-e: max nice                        0
-r: max rt priority                 0
-N 15:                              unlimited
```
如果生成不了：<br />$ echo core > /proc/sys/kernel/core_pattern  （当前窗口有效，关闭自动恢复）

```c
$ gcc error1.c -g -O0
$ ulimit -c unlimited
执行程序
$ gdb 可执行 core		// 
```

`bt`  : backtrace（或bt）: 查看各级函数调用及参数
```c
set args ...  ...  ...	// set the parameter for executing 
show args 				// display all args
```
参考 ：[gdb命令使用](https://segmentfault.com/a/1190000040284357)

<a name="voCYd"></a>
# 3.  makefile
增量编译 生成代码<br />树形结构<br />需要增量编译的情况：

- 没有目标文件
- 依赖文件比目标文件新

<a name="Mt5Bg"></a>
## 3.1 makefile的实现： 
名字 makefile / Makefile<br />目标： 一个        依赖：  零个-多个<br />[tab] 命令：0-多个<br />最终生成文件作为第一个规则目标。

<a name="NrKol"></a>
## 3.2 伪目标

- 目标不存在
- 执行命令生成不了目标文件  

作用：用来实现每次make都一定执行的指令。
```c
main:main.o add.o
    gcc main.o add.o -o main
main.o:main.c
    gcc -c main.c -o main.o
add.o:add.c
    gcc -c add.c -o add.o
.PHONY:clean rebuild
clean:
	rm -rf main.o add.o main
rebuild:clean main
```

<a name="o3FRD"></a>
## 3.3 makefile 通用
<a name="tZHjB"></a>
### 3.3.1 变量
自定义变量：  变量名=值（所有值都是字符串类型）    引用变量： $ （变量名）<br />预定义变量：<br />自动变量： 同一个变量名 值随着规则变化而变化

-  $^  所有依赖文件，以空格分隔          
-  $@  目标文件  
<a name="foPcR"></a>
### 3.3.2 用 %字符 管理格式关系：
按格式匹配依赖文件，完成匹配文件的编译

<a name="Uj5mB"></a>
### 3.3.3 内置函数
wildcard (可以类比通配符) ： 从当前目录所有文件中选取所有符合要求的文件名<br />patsubst (pattern substitude)
```c
// wildward
SRCS:=$(wildcard *.c)
    
// pattern substitude
OBJS:=$(patsubst %.c,%.o,$(SRCS))
```
```c
OUT:=main
SRCS:=$(wildcard *.c)
#OBJS:=main.o add.o sub.o
OBJS:=$(patsubst %.c,%.o,$(SRCS))
CC:=gcc
$(OUT):$(OBJS)
    $(CC) $^ -o $@
%.o:%.c
	$(CC) -c $^ -o $@ 
.PHONY:clean rebuild
clean:
	$(RM) $(OUT) $(OBJS)
rebuild:clean main
```

<a name="j9VBk"></a>
### 3.3.4 单独编译链接
伪目标 ： all
```c
SRCS:=$(wildcard *.c)
EXES:=$(patsubst %.c,%,$(SRCS))
all:$(EXES)
%:%.c
	gcc $^ -o $@ // -g // for gdb
.PHONY:clean rebuild
clean:
	$(RM) $(EXES)
rebuild:clean all
```





