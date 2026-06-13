## 进程间通信  ( Inter Process Communication )
打破进程间的隔离，从而进程间可以共享数据。

- **_管道 _**
- ~~_共享内存_~~
- ~~_信号量_~~
- _消息队列_
- **_信号 _**

### 1. 管道
有名管道 : 在文件系统存在一个管道文件
匿名管道：在文件系统不存在管道文件，只能用于**父子进程**间。

#### `popen`和`pclose`( 库函数 )
#include <stdio.h>
FILE *popen(const char *command, const char *type);
int pclose(FILE *stream);
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649756541118-c4f9a5a2-3878-47c8-b033-cef67f16f40a.png)
```c
w	// 父进程可写入FILE内，子进程把自己的stdin重定向到管道
r	// 父进程可读取FILE内，子进程把自己的stdout重定向到管道
```
```c
#include <myhead.h>
int main(){
    FILE *fp = popen("./print", "r");
    ERROR_CHECK(fp,NULL,"popen");
    char buf[1024] = {0};
    fread(buf,1,sizeof(buf),fp);
    printf("msg from pipe, buf = %s\n", buf);
}

// stdout -> pipe
// print.c
#include <myhead.h>
int main() {
    printf("I am print, waiting to stdout\n");
}
```
```c
#include <myhead.h>
int main(){
    FILE *fp = popen("./sub","w");
    ERROR_CHECK(fp,NULL,"popen");
    fwrite("1000 999",1,8,fp);

    pclose(fp);
}

// stdin -> pipe
// sub.c
#include <myhead.h>
int main(){
    int lhs, rhs;
    scanf("%d%d", &lhs,&rhs);
    printf("lhs - rhs = %d\n", lhs-rhs);
}
```

#### pipe系统调用 （不跨平台）
`pipe` - create an interprocess channel
#include <unistd.h>
int pipe(int fildes[2]);
// 参数应该是一个长度为2 的int数组 数组名
pipefd[0]是**读**端的文件描述符，pipefd[1]是**写**端的文件描述符。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649816157533-d0840a8e-085a-4b22-b566-246ced45881f.png)
```c
#include <myhead.h>
int main(){
    int pipefds[2];
    pipe(pipefds);
    printf("pipefd[0] = %d, pipefd[1] = %d\n", pipefds[0], pipefds[1]);
    write(pipefds[1],"jiayou",6);
    char buf[10] = {0};
    read(pipefds[0],buf,sizeof(buf));
    printf("msg from pipe = %s\n", buf);
}
```
自说自话

**先pipe再fork( )**
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649838215056-8840a585-e6e5-4eb1-b5f1-ccf0c363009e.png)
父子对话
```c
#include <myhead.h>
int main(){
    int fds1[2];
    int fds2[2];
    pipe(fds1);
    pipe(fds2);
    // fds1   子读	子写
    // fds2   父读	父写
    /* fds1:  子读
       fds2:          父写
       --------------------
       fds1: 		  子写
       fds2:  父读		  */
    if(fork() == 0){
        close(fds1[1]);
        close(fds2[0]);
        write(fds2[1],"msg from child", 14);
        char buf[1024] = {0};
        read(fds1[0],buf,sizeof(buf));
        puts(buf);
    }
    else{
        close(fds1[0]);
        close(fds2[1]);
        char buf[1024] = {0};
        read(fds2[0],buf,sizeof(buf));
        puts(buf);
        write(fds1[1],"msg from parent", 15);
        wait(NULL);
    }
}
```
阻塞(父进程read阻塞，等待子进程write完成）实现的同步

#### 有名管道的函数
`mkfifo` - 创建有名管道
#include <sys/types.h>
#include <sys/stat.h>
int mkfifo(const char *pathname, mode_t mode);

`unlink` - 删除文件
#include <unistd.h>
int unlinko(const char *pathname);

`rename` - mv文件
#include <stdio.h>
int rename(const char *oldpath, const char *newpath);

`link` - 创建硬链接
#include <unistd.h>
int link(const char *oldpath, const char *newpath);

## 2. 共享内存
**共享内存 **- 让不同进程的虚拟内存页page 映射到 同一个 物理页框 phrame
是效率最高的进程间通信(IPC)   ( 最常用的：信号，管道，共享内存 )
库文件就是经常使用共享内存的例子
$ lsof   	// 打开的库文件列表

System V 的共享内存机制 _（ 简单了解 ）_
`ftok`- convert a pathname and a project identifier to a System V IPC **key(整数)**
#include <sys/types.h>
#include <sys/ipc.h>
key_t ftok(const char *pathname, int proj_id);
```c
#include <myhead.h>
int main(){
    key_t key = ftok("file1",1);
    ERROR_CHECK(key,-1,"ftok");
    printf("key = %d\n", key);
}
```

`shmget` - allocates a System V shared memory segment //创建共享内存
#include <sys/ipc.h>
#include <sys/shm.h>
int shmget(key_t key, size_t size, int shmflg);
key_t key // 共享内存ID
size_t size // always 4096
int shmflg // 生存属性** IPC_CREAT | 0600**
```c
#include <43func.h>
int main(){
    key_t key = ftok("file1",1);
    ERROR_CHECK(key,-1,"ftok");
    printf("key = %d\n", key);
    int shmid = shmget(key,4096,IPC_CREAT|0600);
    ERROR_CHECK(shmid,-1,"shmget");
}
```
```c
#include <myhead.h>
int main(){
    key_t key = 1000;
    int shmid = shmget(key,4096,IPC_CREAT|0600);
    ERROR_CHECK(shmid,-1,"shmget");
}
```

`shmat`  - System V shared memory operations
// 为共享内存分配虚拟内存空间
#include <sys/types.h>
#include <sys/shm.h>
void *shmat(int shmid, const void *shmaddr, int shmflg);

- int shmid     // shmget的返回值 key
- const void *shmaddr   // NULL 自动分配
- int shmflg		// flag  // 0

使用方法 和 mmap 和 malloc 类似

`shmdt` - 回收虚拟内存
#include <sys/types.h>
#include <sys/shm.h>
int shmdt(const void *shmaddr);

`shmctl` // 删除共享内存，彻底不可用，释放空间。
#include <sys/ipc.h>
#include <sys/shm.h>
int shmctl(int shmid, int cmd, struct shmid_ds *buf);
shmctl (sid, IPC_RMID,0)
```c
#include <myhead.h>
int main(){
    int shmid = shmget(1000,4096,IPC_CREAT|0600);// init all 0
    ERROR_CHECK(shmid,-1,"shmget");
    char *p = (char *)shmat(shmid,NULL,0);
    ERROR_CHECK(p,(void *)-1,"shmat");

    strcpy(p,"hello");

    shmdt(p);
}

#include <myhead.h>
int main(){
    int shmid = shmget(1000,4096,IPC_CREAT|0600);// init all 0
    ERROR_CHECK(shmid,-1,"shmget");
    char *p = (char *)shmat(shmid,NULL,0);
    ERROR_CHECK(p,(void *)-1,"shmat");

    for(int i = 0; i < 5; ++i){
        printf("p[%d] = %c\n",i, p[i]);
    }
    shmdt(p);
}
```

IPC_PRIVATE  - 私有共享内存  ( 类似匿名管道) 只能父子间使用
```c
#include <myhead.h>
int main(){
    int shmid = shmget(IPC_PRIVATE,4096,IPC_CREAT|0600);
    ERROR_CHECK(shmid,-1,"shmget");
    int *p = (int *)shmat(shmid,NULL,0);
    ERROR_CHECK(p,(void *)-1,"shmat");

    if(fork() == 0){
        sleep(1); //不等待则可能没有任何打印信息
        printf("child p = %s\n", p);
    }
    else{
        strcpy(p, "msg from parent");
        wait(NULL);
    }

    shmdt(p);
}
```

```c
#include <myhead.h>
#define NUM 10000000
int main(){
    int shmid = shmget(IPC_PRIVATE,4096,IPC_CREAT|0600);
    ERROR_CHECK(shmid,-1,"shmget");
    int *p = (int *)shmat(shmid,NULL,0);
    ERROR_CHECK(p,(void *)-1,"shmat");
    p[0] = 0;
    if(fork() == 0){
        for(int i = 0; i < NUM; ++i){
            ++p[0];
        }
    }
    else{
        for(int i = 0; i < NUM; ++i){
            ++p[0];
        }
        wait(NULL);
        printf("p[0] = %d\n", p[0]);
    }
    shmdt(p);
}
```
两个进程并发的访问共享资源
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649841547516-0b8fbd8f-51fa-41dc-9e9d-d4b8a04c878b.png)

$ ipcs // 查看存在的共享内存

$ ipcrm -M  key_value // 删除
$ ipcrm -m  shmid      // 删除
$ ipcrm -a   // 删除

获取共享内存的状态
`shmctl`
#include <sys/ipc.h>
#include <sys/shm.h>
int shmctl(int shmid, int cmd, struct shmid_ds *buf);

- int cmd
   - IPC_STAT  	// 获取状态
   - IPC_SET  		// 修改状态
   - IPC_RMID	// 删除

违背了“单一职责”原则

```c
#include <myhead.h>
int main(){
    int shmid = shmget(1000,4096,IPC_CREAT|0600);
    ERROR_CHECK(shmid,-1,"shmget");
    struct shmid_ds stat;
    int ret = shmctl(shmid,IPC_STAT,&stat);
    ERROR_CHECK(ret,-1,"shmctl IPC_STAT");
    printf("perm = %o\n", stat.shm_perm.mode);
    printf("size = %lu\n", stat.shm_segsz);
    stat.shm_perm.mode = 0666;
    // 必须先IPC_STAT , 在修改后, IPC_SET
    ret = shmctl(shmid,IPC_SET,&stat);
    ERROR_CHECK(ret,-1,"shmctl IPC_SET");
}
```
**先IPC_STAT , 在修改后 ， IPC_SET**

删除共享内存
shmctl ( RMID  )   // 标记共享内存将被删除

- 当最后一个detach的进程都断开，就删除
- 不能再attach其他进程
```c
#include <myhead.h>
int main(){
    int shmid = shmget(1000,4096,IPC_CREAT|0600);
    ERROR_CHECK(shmid,-1,"shmget");
    void * ret = shmat(shmid,NULL,0);
    ERROR_CHECK(ret,(void *)-1,"shmat");
    int iret = shmctl(shmid,IPC_RMID,NULL);
    ERROR_CHECK(iret,-1,"shmctl RMID");
    sleep(20);
    shmdt(ret);
}

// 0x00000000  48   user1  666   4096   1   dest(destoryed)
```

**虚拟内存和物理内存的转换**
硬件 	x86		分段  分页( 页 固定大小)

| 20位（页号） | 12位（页内偏移） |
| --- | --- |

页内偏移 在转换时不变，不需存储
页表 ：220个页表项( 一个页表项大小 4B）

| 物理页号 | 控制信号 |
| --- | --- |

**减少页表的大小 （ 局部性原理）**
2 10 (页目录表）x**  210  （一级页表）**    **多级页表**
x86-64 的设计

|  — | 9 | 9 | 9 | 9 | 12 |
| --- | --- | --- | --- | --- | --- |

页表是每个进程各自维护自己的一个
不同的进程    虚拟地址 -> 物理地址 映射关系

进程切换的代价：

- 切换上下文 ( 寄存器状态 CPU )
- 切换页表

父进程 ->  fork( )  -> 子进程
COW	未写入时，共用一个页表
第一次写入时，内核会意识到对应的物理页是属于父进程的，此时会为子进程分配一个新的物理页，如果要分配的物理页不在主存储器中，此时会触发一个异常名为缺页异常，当异常处理完成以后，子进程会被分配一 个新的物理页，并且物理页内容会是原来页的拷贝。这就是所谓的**写时复制**。

单核：软件方法实现互斥 （dekker算法 Linux_Day_12 作业）
```c
#include<myhead.h>
#define NUM 10000000
int main(){
    int shmid = shmget(IPC_PRIVATE,4096,IPC_CREAT|0600);
    ERROR_CHECK(shmid,-1,"shmget");
    int *p = (int *)shmat(shmid,NULL,0);
    ERROR_CHECK(p,(void *)-1,"shmat");
    p[0] = 0;
    p[1] = 0;
    p[2] = 0;
    p[3] = 0;
    if(fork() == 0){
        for(int i = 0; i < NUM; ++i){
            p[1] = 1;
            while(p[2]){
                if(p[3] != 0){
                    p[1] = 0;
                    while(p[3] != 0){

                    }
                    p[1] = 1;
                }
            }
            ++p[0];
            p[3] = 1;
            p[1] = 0;
        }
    }
    else{
        for(int i = 0; i < NUM; ++i){
            p[2] = 1;
            while(p[1]){
                if(p[3] != 1){
                    p[2] = 0;
                    while(p[3] != 1){

                    }
                    p[2] = 1;
                }
            }
            ++p[0];
            p[3] = 0;
            p[2] = 0;
        }
        wait(NULL);
        printf("p[0] = %d\n", p[0]);
    }
    shmdt(p);
    shmctl(shmid,IPC_RMID,NULL);
}
```
多核：会因为多核的竞争造成结果不如预期。

## 3. 信号量
互斥机制：System V
整数：描述资源的个数

- 计数信号量 	// 资源个数
- 二元信号量	// 0/1   P操作、V操作

P操作**（测试并加锁） _不可分割 原语_  需通过硬件实现**

   - 检查sem
      - sem>0   	--sem
      - sem≤0    	wait(NULL);

V操作 （解锁）

   - ++sem

临界区（临界段）：访问共享资源，且不想被分割的代码片段
临界区**越小越好**，充分利用多进程。

利用信号量保护共享资源
System V中 ：	信号量是一个信号量集合（整数数组）
使用只有一个值的数组，下标为0

`semget` - get a System V semaphore set identifier
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
int semget(key_t key, int nsems, int semflg);

`semctl` - System V semaphore control operations
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
int semctl(int semid, int semnum, int cmd, ...);

1.
- int semnum // 数组下标 0 ~ nsems-1
- int cmd	// SETVAL
- ...		// emun
   - union semun {

               int              val;    		/* Value for SETVAL */
               struct semid_ds *buf;     /* Buffer for IPC_STAT, IPC_SET */
               unsigned short  *array;  /* Array for GETALL, SETALL */
               struct seminfo  *__buf;  /* Buffer for IPC_INFO
                                           (Linux-specific) */
           };

2.
- int semnum // 数组下标 0 ~ nsems-1
- int cmd	// GETVAL

**实现PV操作**

1. 定义PV操作
1. 调用PV操作

int semop (int semid, struct sembuf *sops,size_t nsops);
unsigned short sem_num;  /* semaphore number */   // 下标
short          sem_op;           /* semaphore operation */ // +正数  -负数
short          sem_flg; 	   /* operation flags */   	// SEM_UNDO

- 若sem_op > 0 , 资源加上sem_op
- 若sem_op < 0 , 且当前资源 + sem_op ≥ 0，继续运行
- 若sem_op < 0 , 且当前资源 + sem_op < 0，阻塞到资源变化。

```c
#include<myhead.h>
#define NUM 10000000
int main(){
    int shmid = shmget(IPC_PRIVATE,4096,IPC_CREAT|0600);
    ERROR_CHECK(shmid,-1,"shmget");
    int *p = (int *)shmat(shmid,NULL,0);
    ERROR_CHECK(p,(void *)-1,"shmat");
    p[0] = 0;
    int semid = semget(1000,1,IPC_CREAT|0600);
    ERROR_CHECK(semid,-1,"semget");
    int ret = semctl(semid,0,SETVAL,1);
    ERROR_CHECK(ret,-1,"semctl SETVAL");
    ret = semctl(semid,0,GETVAL);
    ERROR_CHECK(ret,-1,"semctl GETVAL");
    printf("semval = %d\n", ret);
    struct sembuf P,V;
    P.sem_num = 0;//下标
    P.sem_op = -1;//对资源的影响
    P.sem_flg = SEM_UNDO;
    V.sem_num = 0;
    V.sem_op = 1;
    V.sem_flg = SEM_UNDO;
    if(fork() == 0){
        for(int i = 0; i < NUM; ++i){
            semop(semid,&P,1);
            ++p[0];
            semop(semid,&V,1);
        }
    }
    else{
        for(int i = 0; i < NUM; ++i){
            semop(semid,&P,1);
            ++p[0];
            semop(semid,&V,1);
        }
        wait(NULL);
        printf("p[0] = %d\n", p[0]);
    }
    shmdt(p);
    shmctl(shmid,IPC_RMID,NULL);
}
```

`gettimeofday` - get time
#include <sys/time.h>
int gettimeofday(struct timeval *tv, struct timezone *tz);
```c
#include<myhead.h>
#define NUM 10000000
int main(){
    int shmid = shmget(IPC_PRIVATE,4096,IPC_CREAT|0600);
    ERROR_CHECK(shmid,-1,"shmget");
    int *p = (int *)shmat(shmid,NULL,0);
    ERROR_CHECK(p,(void *)-1,"shmat");
    p[0] = 0;
    int semid = semget(1000,1,IPC_CREAT|0600);
    ERROR_CHECK(semid,-1,"semget");
    int ret = semctl(semid,0,SETVAL,1);
    ERROR_CHECK(ret,-1,"semctl SETVAL");
    ret = semctl(semid,0,GETVAL);
    ERROR_CHECK(ret,-1,"semctl GETVAL");
    printf("semval = %d\n", ret);
    struct sembuf P,V;
    P.sem_num = 0;//下标
    P.sem_op = -1;//对资源的影响
    P.sem_flg = SEM_UNDO;
    V.sem_num = 0;
    V.sem_op = 1;
    V.sem_flg = SEM_UNDO;
    struct timeval timeBeg,timeEnd;
    gettimeofday(&timeBeg,NULL);// begin time
    if(fork() == 0){
        for(int i = 0; i < NUM; ++i){
            semop(semid,&P,1);
            ++p[0];
            semop(semid,&V,1);
        }
    }
    else{
        for(int i = 0; i < NUM; ++i){
            semop(semid,&P,1);
            ++p[0];
            semop(semid,&V,1);
        }
        wait(NULL);
        gettimeofday(&timeEnd,NULL); // end time
        printf("total time = %ld us\n",
            (timeEnd.tv_sec - timeBeg.tv_sec)*1000000 + timeEnd.tv_usec - timeBeg.tv_usec);
        printf("p[0] = %d\n", p[0]);
    }
    shmdt(p);
    shmctl(shmid,IPC_RMID,NULL);
}

// semval= 1
//total time = 23852665 us
// p[0] = 20000000
```
_信号量 ：600ns  // 开销比较大_
_if else  ： 3ns_
_内存缺页：100ns_

多个信号量组成的集合

1. 二元信号量+共享内存

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649940715301-1041c7ea-8237-49f2-9d91-afe90515f479.png)

2. 计数信号量

key相同的信号量，长度也必须相同
```c
#include <myhead.h>
int main(){
    int semid = semget(1001,2,IPC_CREAT|0600);
    //key相同的信号量，长度必须相同
    ERROR_CHECK(semid,-1,"semget");
    //semctl(semid,0,SETVAL,10);
    //semctl(semid,1,SETVAL,10);
    unsigned short arr[2] = {10,10};
    semctl(semid,0,SETALL,arr);
    unsigned short retArr[2];
    semctl(semid,0,GETALL,retArr);
    printf("egg = %d, flour = %d\n", retArr[0],retArr[1]);
    //printf("egg = %d, flour = %d\n", semctl(semid,0,GETVAL), semctl(semid,1,GETVAL));
    struct sembuf bread[2];
    bread[0].sem_num = 0;
    bread[0].sem_op = -3;
    bread[0].sem_flg = SEM_UNDO;
    bread[1].sem_num = 1;
    bread[1].sem_op = -2;
    bread[1].sem_flg = SEM_UNDO;
    struct sembuf cake[2];
    cake[0].sem_num = 0;
    cake[0].sem_op = -5;
    cake[0].sem_flg = SEM_UNDO;
    cake[1].sem_num = 1;
    cake[1].sem_op = -1;
    cake[1].sem_flg = SEM_UNDO;
    if(fork() == 0){
        while(1){
            printf("before make bread\n");
            printf("egg = %d, flour = %d\n", semctl(semid,0,GETVAL), semctl(semid,1,GETVAL));
            semop(semid,bread,2);
            printf("after make bread\n");
            printf("egg = %d, flour = %d\n", semctl(semid,0,GETVAL), semctl(semid,1,GETVAL));
            sleep(1);
        }
    }
    else{
        while(1){
            printf("before make cake\n");
            printf("egg = %d, flour = %d\n", semctl(semid,0,GETVAL), semctl(semid,1,GETVAL));
            semop(semid,cake,2);
            printf("after make cake\n");
            printf("egg = %d, flour = %d\n", semctl(semid,0,GETVAL), semctl(semid,1,GETVAL));
            sleep(1);
        }
        wait(NULL);
    }
}
```

多个生产者/多个消费者
典型错误： 临界资源过小而没达到预期
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649940972297-fc963136-d930-4f62-beee-bbd7ce05d0f3.png)
```c
#include <myhead.h>
int main()
{
    int shmid = shmget(IPC_PRIVATE, 4096, IPC_CREAT | 0600);
    ERROR_CHECK(shmid, -1, "shmget");
    int *p = (int *)shmat(shmid, NULL, 0);
    ERROR_CHECK(p, (void *)-1, "shmat");
    p[0] = 10; // p[0] 表示仓库的个数
    p[1] = 0;  // p[1] 表示商品的个数
    int semid = semget(1000, 1, IPC_CREAT | 0600);
    ERROR_CHECK(semid, -1, "semget");
    int ret = semctl(semid, 0, SETVAL, 1);
    ERROR_CHECK(ret, -1, "semctl SETVAL");
    ret = semctl(semid, 0, GETVAL);
    ERROR_CHECK(ret, -1, "semctl GETVAL");
    printf("semval = %d\n", ret);
    struct sembuf P, V;
    P.sem_num = 0; //下标
    P.sem_op = -1; //对资源的影响
    P.sem_flg = SEM_UNDO;// 0 会在子进程意外中止时，其他进程不能解锁
    V.sem_num = 0;
    V.sem_op = 1;
    V.sem_flg = SEM_UNDO;// 0 会在子进程意外中止时，其他进程不能解锁
    if (fork() == 0)
    {
        while (1)
        {
            semop(semid, &P, 1);
            if (p[0] > 0)
            {
                printf("before produce, space = %2d, good = %2d, total = %d\n", p[0], p[1], p[0] + p[1]);
                --p[0];
                ++p[1];
                printf("after produce, space = %2d, good = %2d, total = %d\n", p[0], p[1], p[0] + p[1]);
            }
            semop(semid, &V, 1);
            // sleep(1);
        }
    }
    else if (fork() == 0)
    {
        while (1)
        {
            semop(semid, &P, 1);
            if (p[0] > 0)
            {
                printf("before produce, space = %2d, good = %2d, total = %d\n", p[0], p[1], p[0] + p[1]);
                --p[0];
                ++p[1];
                printf("after produce, space = %2d, good = %2d, total = %d\n", p[0], p[1], p[0] + p[1]);
            }
            semop(semid, &V, 1);
            // sleep(1);
        }
    }
    else
    {
        while (1)
        {
            semop(semid, &P, 1);
            if (p[1] > 0)
            {
                printf("before consume , space = %2d, good = %2d, total = %d\n", p[0], p[1], p[0] + p[1]);
                --p[1];
                ++p[0];
                printf("after consume, space = %2d, good = %2d, total = %d\n", p[0], p[1], p[0] + p[1]);
            }
            semop(semid, &V, 1);
            // usleep(100000);
        }
        wait(NULL);
    }
    shmdt(p);
    shmctl(shmid, IPC_RMID, NULL);
}
```
PV操作 一定要保护到**完整的共享资源**访问

```c
#include <myhead.h>
int main()
{
    int shmid = shmget(IPC_PRIVATE, 4096, IPC_CREAT | 0600);
    ERROR_CHECK(shmid, -1, "shmget");
    int *p = (int *)shmat(shmid, NULL, 0);
    ERROR_CHECK(p, (void *)-1, "shmat");
    p[0] = 0; // p[0] 表示仓库的个数
    p[1] = 10;  // p[1] 表示商品的个数
    int semid = semget(1003, 1, IPC_CREAT | 0600);
    ERROR_CHECK(semid, -1, "semget");
    int ret = semctl(semid, 0, SETVAL, 1);
    ERROR_CHECK(ret, -1, "semctl SETVAL");
    ret = semctl(semid, 0, GETVAL);
    ERROR_CHECK(ret, -1, "semctl GETVAL");
    printf("semval = %d\n", ret);
    struct sembuf P, V;
    P.sem_num = 0; //下标
    P.sem_op = -1; //对资源的影响
    P.sem_flg = SEM_UNDO;// 0 会在子进程意外中止时，其他进程不能解锁
    V.sem_num = 0;
    V.sem_op = 1;
    V.sem_flg = SEM_UNDO;// 0 会在子进程意外中止时，其他进程不能解锁
    if (fork() == 0)
    {
        while (1)
        {
            semop(semid, &P, 1);
            printf("before produce, p[1] = %d, sem = %d\n", p[1], semctl(semid,0,GETVAL));
            if (p[0] > 0)
            {
                --p[0];
                ++p[1];
            }
            sleep(2);
            semop(semid, &V, 1);
            printf("after produce, p[1] = %d, sem = %d\n", p[1], semctl(semid,0,GETVAL));
        }
    }
    else
    {
        while (1)
        {
            semop(semid, &P, 1);
            printf("before consume, p[1] = %d, sem = %d\n", p[1], semctl(semid,0,GETVAL));
            if (p[1] > 0)
            {
                --p[1];
                ++p[0];
            }
            sleep(2);
            semop(semid, &V, 1);
            printf("after consume, p[1] = %d, sem = %d\n", p[1], semctl(semid,0,GETVAL));
        }
        wait(NULL);
    }
    shmdt(p);
    shmctl(shmid, IPC_RMID, NULL);
}
```
上述程序中 ，P.sem_flg = 0  V.sem_flg = 0 会使子进程意外中止时，其他进程不能解锁
处于加锁状态的一个进程异常中止的，其他进程不能继续，导致死锁2。

**SEM_UNDO  ** 在某个进程终止时，把其减去的资源加回来，维护多进程正常运行。

## 4.消息队列
IPC 只能在本机通信     保留消息边界
_//  广义的消息队列： 网络通信 Kafka RabbitMQ_

_管道消息 (流式消息)	没有边界_
_TCP 流 	UDP 数据包_

`msgget` - get a System V message queue identifier
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
int msgget(key_t key, int msgflg);

- int msgflg   // IPC_CREAT | 0600

`msgsnd` 和 `msgrcv`
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
int msgsnd(int msqid, const void *msgp, size_t msgsz, int msgflg);

- const void *msgp     // 消息
- size_t msgsz   // **strlen**( msg.mtext)

ssize_t msgrcv(int msqid, void *msgp, size_t msgsz, long msgtyp, int msgflg);

- size_t msgsz   // **sizeof**( msg.mtext)
- struct msgbuf {

               long mtype;       /* message type, must be > 0 */
               char mtext[1];    /* message data */
           };  // 需要自己修改 mtext[ ] 的长度
```c
#include <myhead.h>
typedef struct msgbuf{
    long mtype;
    char mtext[256];
} myMsg_t;
int main(){
    int msqid = msgget(1000,IPC_CREAT|0600);
    ERROR_CHECK(msqid,-1,"msgget");
    myMsg_t msg1;//Huangxiaoming
    myMsg_t msg2;//Wuyifan
    myMsg_t msg3;//Caixukun
    msg1.mtype = 1;
    strcpy(msg1.mtext,"Ganenguoqusuoyou,weilairenshijiaren");
    msg2.mtype = 2;
    strcpy(msg2.mtext,"skr skr~");
    msg3.mtype = 3;
    strcpy(msg3.mtext,"jinitaimei");
    msgsnd(msqid,&msg1,strlen(msg1.mtext), 0);
    msgsnd(msqid,&msg2,strlen(msg2.mtext), 0);
    msgsnd(msqid,&msg3,strlen(msg3.mtext), 0);
    puts("send over");

}
```
```c
#include <myhead.h>
typedef struct msgbuf{
    long mtype;
    char mtext[256];
} myMsg_t;
int main(){
    int msqid = msgget(1000,IPC_CREAT|0600);
    ERROR_CHECK(msqid,-1,"msgget");
    long type;
    printf("who are you? 1 huangxiaoming 2 wuyifan 3 caixukun\n");
    scanf("%ld",&type);
    myMsg_t msg;
    memset(&msg,0,sizeof(msg));
    //msgrcv(msqid,&msg,sizeof(msg.mtext),type,0);
    //msgrcv(msqid,&msg,sizeof(msg.mtext),0,0);
    int ret = msgrcv(msqid,&msg,sizeof(msg.mtext),0,IPC_NOWAIT);
    ERROR_CHECK(ret,-1,"msgrcv");
    printf("you are %ld, msg = %s\n", type, msg.mtext);
}
```

## proc 文件系统
伪文件系统   process
操作系统的运行状态在文件系统的映射
可以像修改文件语言，修改操作系统的属性。

## 5. 信号
信号：一种软件层面的异步事件机制。
中断：硬件层面
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649988664291-1ebbccc7-1e6e-4513-a592-4593939f74e2.png)

$ man 7 signal
不同信号对应不同的整数

$ kill -l  // 简略对应编号

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1649989680674-0a6b7843-4e0b-4c50-b45c-b045cfcd8bd4.png)

信号产生的时机

- 软件 + 异步  	// $ kill -p pid
- 软件 + 同步	// abort( )  // kill -6
- 硬件 + 异步	// Ctrl + C  Ctrl + \
- 硬件 + 同步 	// 除0

产生  --**- 间隔时间  ( pending 未决）**--->  递送
来源								   目标进程
信号产生：会修改目标进程的task_struct (目标进程认为所有信号来自内核 )
响应时机： 可递送信号的时机 （几乎所有状态，除了D状态 不可中断的）

**更改默认信号行为 ( **本课程
不再执行默认行为，而是调用一个函数 sigFunc( )
Term   Default action is to terminate the process. // 中止
Ign      Default action is to ignore the signal.  // 忽略
Core    Default action is to terminate the process and dump core (see core(5)). // 中止并生成core
Stop    Default action is to stop the process.  // 暂停
Cont    Default action is to continue the process if it is currently stopped.

`signal` - ANSI C signal handling // 注册信号处理行为 // 恢复
#include <signal.h>
typedef void (*sighandler_t)(int);
sighandler_t signal(int signum, sighandler_t handler);
注册信号处理行为  <-   等到信号到来时，才会调用。 // 被动

- 第1个参数 signum 表示要捕捉的信号
- 第 2 个参数是个函数指针，表示捕获信号后执行的函数（回调函数），
   - 是 SIG_DFL，表示交由系统缺省处理
   - 是 SIG_IGN，表示忽略掉该信号而不做任何处理。

`signal`

- 如果调用成功，返回以前该信号的处理函数的地址
- 否则返回SIG_ERR。

sighandler_t 是信号捕捉函数，是一个回调函数，在 signal 函数中注册， 注册后在整个进程运行过程中均有效，并且对不同的信号可以注册同一个回调函数。该函数只有一个整型参数，表示信号值。
```c
#include <myhead.h>
void sigFunc(int num){
    //printf("num = %d\n", num);
    //printf("num = %d", num); 记得加上换行
    printf("before sleep, I am %d\n", num);
    sleep(3);
    printf("after sleep, I am %d\n", num);
}
int main(){
    void (*ret)(int);
    ret = signal(SIGINT,sigFunc);
    ERROR_CHECK(ret,SIG_ERR,"signal");

    while(1){

    }
}
```

信号递送的行为
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1650024981410-63a155e3-22e2-43ef-af99-416f8b4c8128.png)

阻塞和未决实现的原理
阻塞：让产生的信号不能马上递送，而是处于未决状态。阻塞信号集 mask
未决：已产生，但未递送的信号。 未决信号集pending
阻塞信号集mask 和 未决信号集pending  **位图 **

1. 递送信号A，把信号A本身加入阻塞信号集mask；
1. 之后有A信号产生，将其加入未决信号集pending ；
1. 信号递送完成后，从mask移除A，递送pending中的A信号。

**位图** 只有0/1 ，所以**pending**中一个信号只能**同时存在一个**

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1650023403968-7177ecf0-b42d-4ab5-90b2-68fe782fdf3a.png)
不同信号的阻塞
```c
#include <myhead.h>
void sigFunc(int num){
    //printf("num = %d\n", num);
    //printf("num = %d", num); 记得加上换行
    printf("before sleep, I am %d\n", num);
    sleep(3);
    printf("after sleep, I am %d\n", num);
}
int main(){
    void (*ret)(int);
    ret = signal(SIGINT,sigFunc);
    ERROR_CHECK(ret,SIG_ERR,"signal");
    ret = signal(SIGQUIT,sigFunc);
    ERROR_CHECK(ret,SIG_ERR,"signal");
    while(1){

    }
}
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1650005088863-6ca6c44f-d13c-41f6-9f43-ac880b7669c4.png)

- 一个信号递送时，有其他信号，会转而处理其他信号，类似 递归栈
- 单个信号最多一个在递送，一个处于pending中

低速系统调用
有可能陷入永久等待的系统调用。
```c
#include <43func.h>
void sigFunc(int num){
    //printf("num = %d\n", num);
    //printf("num = %d", num); 记得加上换行
    printf("before sleep, I am %d\n", num);
    sleep(3);
    printf("after sleep, I am %d\n", num);
}
int main(){
    void (*ret)(int);
    ret = signal(SIGINT,sigFunc);
    ERROR_CHECK(ret,SIG_ERR,"signal");
    //ret = signal(SIGQUIT,sigFunc);
    //ERROR_CHECK(ret,SIG_ERR,"signal");
    char buf[100] = {0};
    read(STDIN_FILENO,buf,sizeof(buf));
    printf("buf = %s\n", buf);
}
```
信号递送完成之后会自动重启低速系统调用。

让注册只生效一次。
```c
#include <43func.h>
void sigFunc(int num){
    printf("num = %d\n", num);
    signal(SIGINT,SIG_DFL);
}
int main(){
    void (*ret)(int);
    ret = signal(SIGINT,sigFunc);
    ERROR_CHECK(ret,SIG_ERR,"signal");
    char buf[100] = {0};
    read(STDIN_FILENO,buf,sizeof(buf));
    printf("buf = %s\n", buf);
}
```

`signal` 的特点

1. 一次注册，永久生效。
1. 递送A时，会将A加入mask， 其他信号不会加入mask
1. 会自动重启低速系统调用

`**sigaction**` - examine and change a signal action **可以完全取代signal**
#include <signal.h>
int sigaction(int signum, const struct sigaction *act,  struct sigaction *oldact);

   - 默认使用第一个(1个参数)版本的回调函数
   - 默认不自动重启低速系统调用   // 用SA_RESTART去修改
   - 默认修改过程会把自己加入mask
- int signum
- struct sigaction { // 前两个是递送行为，二选一

               void     (*sa_handler)(int);
               void     (*sa_sigaction)(int, siginfo_t *, void *);
               sigset_t   sa_mask; // 额外mask
               int        sa_flags;    // 额外属性
             ~~  void     (*sa_restorer)(void);~~
           };    // 新状态

   - sa_flgs:
      - SA_SIGINFO - he  signal  handler  takes three arguments, not one.
         - 三参数版本
      - SA_RESTART - 重启低系统调用
      - SA_RESETHAND - Restore the signal action to the default upon entry to the signal handler.
         - 只注册一次
      - SA_NODEFFER - Do not prevent the signal from being received from within its own signal  handler
         - 在递送A时不屏蔽A，有新的A信号则转而递送新的Ａ信号
   - sa_mask  本质是一个位图

typedef struct {
unsigned long int __val[ _SIGSET_NWORDS]
} _sigset_t;

- struct sigaction *oldact  // 保存旧状态（不想保存就填NULL)

```c
#include <43func.h>
void sigFunc(int num){
    printf("before, num = %d\n", num);
    sleep(3);
    printf("after, num = %d\n", num);
}
void sigFunc3(int num, siginfo_t *siginfo , void * p){
    printf("num = %d\n", num);
    printf("sender pid = %d\n", siginfo->si_pid);
}
int main(){
    struct sigaction act;
    memset(&act,0,sizeof(act));
    act.sa_handler = sigFunc;
    //act.sa_sigaction = sigFunc3;
    //act.sa_flags = SA_RESTART|SA_SIGINFO|SA_RESETHAND;
    //act.sa_flags = SA_RESTART|SA_NODEFER;
    act.sa_flags = SA_RESTART;
    sigaddset(&act.sa_mask,SIGQUIT);
    int ret = sigaction(SIGINT,&act,NULL);
    ERROR_CHECK(ret,-1,"sigaction");
    //ret = sigaction(SIGQUIT,&act,NULL);
    //ERROR_CHECK(ret,-1,"sigaction");
    char buf[100] = {0};
    read(STDIN_FILENO,buf,sizeof(buf));
    printf("buf = %s\n", buf);
    //while (1)
    //{
    //}

}
```

sa_mask  **位图**
修改sa_mask的操作：
int sigemptyset(sigset_t *set);			// 清空集合
int sigfillset(sigset_t *set);				// 集合的每一位为1
int sigaddset(sigset_t *set, int signum);		// 将signum加入到集合中
int sigdelset(sigset_t *set, int signum);		// 将signum从集合中移除
int sigismember(const sigset_t *set, int signum); // 判断signum是否在集合中
mask 	阻塞集合		平时没有信号，在递送中，将自己加入 (SA_NODEFER则不加入）
pending	未决集合

sa_mask 用来指定递送过程中的额外屏蔽信号
在SIGINT 信号的递送过程中，把SIGQUIT 加入阻塞。
sa_mask 是一种临时的额外阻塞。

### 有关信号的函数
`sigprocmask` 实现全程阻塞
#include <signal.h>
/* Prototype for the glibc wrapper function */
int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);

- int how
   - SIG_BLOCK 		// +
   - SIG_UNBLOCK 	// -
   - SIG_SETMASK 	// =
- const sigset_t *set    // 新设置
- sigset_t *oldset  	 // 原来的设置（不想保存就填NULL)
```c
#include <43func.h>
void sigFunc(int num){
    printf("num = %d\n", num);
}
int main(){
    signal(SIGQUIT,sigFunc);
    sigset_t set;
    sigemptyset(&set);
    sigaddset(&set,SIGQUIT);
    sigset_t oldset;
    sigprocmask(SIG_SETMASK,&set,&oldset);// 屏蔽SIGQUIT
    printf("I am going to sleep!\n");
    sleep(10);
    printf("I wake up\n");
    sigprocmask(SIG_SETMASK,&oldset,NULL);// 解除屏蔽SIGQUIT
    printf("byebye!\n");// 不会打印
    return 0;
}
```

`sigpending` - examine pending signals. // 获取pending集合
#include <signal.h>
int sigpending(sigset_t *set);
```c
#include <43func.h>
void sigFunc(int num){
    printf("num = %d\n", num);
}
int main(){
    signal(SIGQUIT,sigFunc);
    sigset_t set;
    sigemptyset(&set);
    sigaddset(&set,SIGQUIT);
    sigset_t oldset;
    sigprocmask(SIG_SETMASK,&set,&oldset);
    printf("I am going to sleep!\n");
    sleep(10);
    printf("I wake up\n");
    sigset_t pending;
    sigpending(&pending);
    if(sigismember(&pending,SIGQUIT)){
        printf("SIGQUIT is pending!\n");
    }
    else{
        printf("SIGQUIT is not pending!\n");
    }
    sigprocmask(SIG_SETMASK,&oldset,NULL);
    printf("byebye!\n");
    return 0;
}
```

`pause` - wait for signal.
#include <unistd.h>
int pause(void);
```c
#include <43func.h>
void sigFunc(int num){
    printf("num = %d\n", num);
}
int main(){
    signal(SIGINT,sigFunc);
    pause();
}
```

`kill`- send a signal to a process or a group of processes. // 给其他进程发送信号
#include <signal.h>
int kill (pid_t pid, int sig);
```c
#include <43func.h>
int main(int argc, char *argv[])
{
    // ./kill -sig pid
    ARGS_CHECK(argc, 3);
    // argv[1] "-9"
    int sig = atoi(argv[1] + 1); // 9
    pid_t pid = atoi(argv[2]);
    int ret = kill(pid, sig);
    ERROR_CHECK(ret, -1, "kill");

    return 0;
}
```

`raise` - - send a signal to the caller // 给主调函数发信号
#include <signal.h>
int raise(int sig);
```c
#include <43func.h>
void sigFunc(int num){
    printf("num = %d\n", num);
}
int main(){
    signal(SIGINT,sigFunc);
    while(1){
        getchar();
        raise(2);
    }
}
```
有序退出

`alarm` - set an alarm clock for delivery of a signal.
#include <unistd.h>
unsigned int alarm(unsigned int seconds);
```c
#include <43func.h>
void sigFunc(int signum){
    time_t now = time(NULL);
    printf("%s\n", ctime(&now));
}
int main(){
    signal(SIGALRM,sigFunc);
    sigFunc(0);
    alarm(5);
    pause();
}
```

自己实现一个`mysleep`
```c
#include <43func.h>
void sigFunc(int num){
}
void mysleep(int second){
    signal(SIGALRM,sigFunc);
    alarm(second);
    pause();
}
int main(){
    mysleep(1);
}
```

时钟
间隔定时器
`getitimer` - get value of an interval timer
#include <sys/time.h>
int getitimer(int which, struct itimerval *curr_value);
```c
struct itimerval {
     struct timeval it_interval; /* Interval for periodic timer */
     struct timeval it_value;    /* Time until next expiration */
};
// 先过value响一次，再每过interval 响一次

struct timeval {
     time_t      tv_sec;         /* seconds */
     suseconds_t tv_usec;        /* microseconds */
};
```

#include <sys/time.h>
int getitimer(int which, struct itimerval *curr_value);
int setitimer(int which, const struct itimerval *new_value, struct itimerval *old_value);

- ITIMER_REL		// 真实时间 SIGALARM
- ITIMER_VITURL	// 虚拟时间，占用用户态CPU的时间  SIGVTALARM
- ITIME_PROF		// 实用时间 ，占用用户态＋内核态的CPU时间 SIGPROF
```c
#include <43func.h>
void sigFunc(int signum){
    time_t now = time(NULL);
    puts(ctime(&now));
}
int main(){
    struct itimerval itimer;
    itimer.it_value.tv_sec = 5;
    itimer.it_value.tv_usec = 0;
    itimer.it_interval.tv_sec = 1;
    itimer.it_interval.tv_usec = 0;
    signal(SIGPROF,sigFunc);
    setitimer(ITIMER_PROF,&itimer,NULL);
    sigFunc(0);
    while(1);
}
```

### 练习及作业

`bzero` - zero a byte string
#include <strings.h>
void bzero(void *s, size_t n);

```c
#include <43func.h>
int main(){
    int fds[2];
    pipe(fds);
    //父读文件 写管道
    //子读管道 写文件
    if(fork() == 0){
        close(fds[1]);//子进程关闭写端
        int fd = open("file2", O_RDWR|O_CREAT|O_TRUNC,0666);
        ERROR_CHECK(fd,-1,"open");
        char buf[4096] = {0};
        while(1){
            bzero(buf,sizeof(buf));
            int ret = read(fds[0],buf,sizeof(buf));
            //读管道和读文件表现是不一样的
            //没有数据时 读文件返回0 读管道阻塞
            ERROR_CHECK(ret,-1,"read");
            if(ret == 0){
                break;
            }
            write(fd,buf,ret);
        }
        close(fds[0]);
    }
    else{
        close(fds[0]);
        int fd = open("file1",O_RDWR);
        ERROR_CHECK(fd,-1,"open");
        char buf[4096];
        while(1){
            bzero(buf,sizeof(buf));
            int ret = read(fd,buf,sizeof(buf));
            ERROR_CHECK(ret,-1,"read");
            if(ret == 0){
                break;
            }
            write(fds[1],buf,ret);
        }
        close(fds[1]);
        wait(NULL);
    }
}
```

自己实现一个bash
```c
#include <43func.h>
void sigFunc(int signum){
    printf("\n%s$", getcwd(NULL,0));
    fflush(stdout);
}
int main(){
    signal(SIGINT,sigFunc);
    while(1){
        printf("%s$", getcwd(NULL,0));
        fflush(stdout);
        char cmd[4096] = {0};
        read(STDIN_FILENO,cmd,sizeof(cmd));
        cmd[strlen(cmd)-1] = 0;
        if(fork() == 0){
            signal(SIGINT,SIG_DFL);
            char *argvector[100] = {0};
            argvector[0] = strtok(cmd," ");
            int i = 1;
            while(1){
                argvector[i] = strtok(NULL," ");
                if(argvector[i] == NULL){
                    break;
                }
                ++i;
            }
            execv(argvector[0],argvector);
        }
        else{
            wait(NULL);
        }
    }
}
```

四窗口聊天
```c
#include<43func.h>
int p0;
int p1;
int p2;
int p3;
void sigFunc(int num){
    //kill()
    sig = 10;
    pid_t pid = atoi(argv[2]);
    int ret = kill(pid,sig);
    ERROR_CHECK(ret,-1,"kill");

 }
int main(){
    int shmid = shmget(1000,4096,IPC_CREAT|0600);
    int *pid = (int *)shmat(shmid,NULL,0);
    pid[0] = getpid();
    while(pid[0] == 0 || pid[1] == 0 || pid[2] == 0 || pid[3] == 0){}
    p0 = pid[0];
    //...
   signal(SIGUSR1,sigFunc);
}
```
