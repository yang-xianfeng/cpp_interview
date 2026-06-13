`select(1024 轮询)` 、  `poll` 、 `epoll`   都有各自适应的场景



<a name="2eb79535"></a>
## C++Day31
<a name="9e17ecdb"></a>
### 一、问题回顾
1、熟练写出线程池的代码？

2、计算机网络基础？

<a name="07e621b7"></a>
### 二、计算机网络
<a name="40d872b0"></a>
#### 1、网络模型
OSI七层模型、TCP/IP四层（五层）模型<br />![image-20220621090232880.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655797693686-1b53817a-1054-4a65-8a41-fb38a9b0772e.png#clientId=uc573125d-2b3a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u1c001853&margin=%5Bobject%20Object%5D&name=image-20220621090232880.png&originHeight=462&originWidth=766&originalType=binary&ratio=1&rotation=0&showTitle=false&size=211742&status=done&style=none&taskId=u387c806d-9a50-412e-bff9-5e6d14f0bbc&title=)

<a name="TEO8d"></a>
#### 2、每一层数据包的名字
![image-20220621090305184.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655797708855-7c7d3d45-9bfa-4de4-a950-fb1b3fd3e3d6.png#clientId=uc573125d-2b3a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uf4ed07b5&margin=%5Bobject%20Object%5D&name=image-20220621090305184.png&originHeight=372&originWidth=980&originalType=binary&ratio=1&rotation=0&showTitle=false&size=258248&status=done&style=none&taskId=ued420e56-2413-433e-aa15-0ca147e19d3&title=)

<a name="9cdd430d"></a>
#### 3、每一层的协议格式
以太网帧格式<br />IP段格式<br />TCP数据报格式、UDP数据报格式

<a name="76ba4a7c"></a>
#### 4、TCP协议（重点）
TCP协议是一个传输层的协议；TCP面向连接的协议；TCP是一个可靠的协议；TCP是全双工的协议。

**TCP的建立连接的三次握手、断开连接的四次挥手？SYN、ACK、FIN（这个是面试常考点）**

相应的文字解析，希望自己可以看看课件，自己好好复习一下。<br />![image-20220621091051593.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655797749065-bf69bb6e-34a6-4079-9f71-014916e5fccd.png#clientId=uc573125d-2b3a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u6e5d83d6&margin=%5Bobject%20Object%5D&name=image-20220621091051593.png&originHeight=814&originWidth=791&originalType=binary&ratio=1&rotation=0&showTitle=false&size=127541&status=done&style=none&taskId=u54691280-b4a2-461e-bbeb-1a288b4530e&title=)


<a name="b139b931"></a>
#### 5、TCP状态迁移图（重点）
记住其中的11个状态；以及使用代码验证这部分状态。

可以使用nc命名
```bash
nc ip   port

nc 127.0.0.1 8888
```

粗实线 ：主动发起连接与主动关闭连接；<br />虚线：被动发起连接与被动关闭连接；<br />细实线: 两端同时操作 的部分。  <br />![image-20220621090827235.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655797792791-7bc248f3-3030-49ca-9a43-38bfbd62329d.png#clientId=uc573125d-2b3a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u1967cd57&margin=%5Bobject%20Object%5D&name=image-20220621090827235.png&originHeight=819&originWidth=886&originalType=binary&ratio=1&rotation=0&showTitle=false&size=205624&status=done&style=none&taskId=uda3c8a1c-933a-43a7-a3ea-5620455ff2d&title=)<br />半关闭状态、2MSL？

 
<a name="ccbf8f9e"></a>
### 三、计算机网络

<a name="bcf3db13"></a>
#### 1、计算机网络基础
网络字节序、主机字节序、大端、小端

<a name="5d42d0f0"></a>
#### 2、网络编程的函数
<a name="9d99bbbf"></a>
##### 结构体
<a name="xfqQW"></a>
##### ![image-20220621100118239.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655797846551-3938c65a-b55b-43f3-8164-5a12f1675b2d.png#clientId=uc573125d-2b3a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u8b9c3af3&margin=%5Bobject%20Object%5D&name=image-20220621100118239.png&originHeight=606&originWidth=1020&originalType=binary&ratio=1&rotation=0&showTitle=false&size=94754&status=done&style=none&taskId=u2df7dd4c-d355-4b72-9f7c-fd9da14a9e1&title=)

<a name="870a51ba"></a>
##### 函数
socket、bind、listen、accept、connect、close

服务器
```c
int lfd = socket;
bind;
listen;//服务器处于监听状态
int cfd = accept;//cfd有正常值的时候，证明三次握手已经完成（TCP连接已经建立）

while(1)
{
    //服务器真正的业务逻辑
    read;
    //
    //....
    //
    write;
}

close(lfd);//四次挥手
close(cfd);
```

客户端
```c
int lfd = socket;
connect;
while(1)
{
    //客户端的业务逻辑
     read;
    //
    //....
    //
    write;
}

close(lfd);//四次挥手
```


![image-20220621102555658.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655797877319-1385d377-0b3a-487d-86eb-290b0947b925.png#clientId=uc573125d-2b3a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ub52a6673&margin=%5Bobject%20Object%5D&name=image-20220621102555658.png&originHeight=394&originWidth=1070&originalType=binary&ratio=1&rotation=0&showTitle=false&size=95830&status=done&style=none&taskId=u17edfd33-d0c1-428b-ae36-ce28c5bf10e&title=)


<a name="eef46514"></a>
#### 3、端口复用
```c
int opt = 1;
setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
int opt = 1;
setsockopt(listenfd, SOL_SOCKET, SO_REUSEPORT, &opt, sizeof(opt));
```

<a name="0cf26ac0"></a>
### 四、IO多路复用模型
<a name="2fd22088"></a>
#### 1、基本思想
![image-20220621105818412.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655797905246-4fd7a298-9881-4526-aebf-385a8a088530.png#clientId=uc573125d-2b3a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u364e4834&margin=%5Bobject%20Object%5D&name=image-20220621105818412.png&originHeight=713&originWidth=1105&originalType=binary&ratio=1&rotation=0&showTitle=false&size=157936&status=done&style=none&taskId=u4951ca14-0c89-4a50-b568-bad2b521a67&title=)

**位图、跳表两个数据结构**

<a name="32115cbb"></a>
#### 2、select
```c
int select(int nfds, fd_set *readfds, fd_set *writefds,
           fd_set *exceptfds, struct timeval *timeout);

void FD_CLR(int fd, fd_set *set);
int  FD_ISSET(int fd, fd_set *set);
void FD_SET(int fd, fd_set *set);
void FD_ZERO(fd_set *set);
```
客户端与服务器连接的读事件，1、客户端请求与服务器进行连接的事件   2、客户端发送数据给了服务器，此时服务器需要读这个数据

<a name="348fd016"></a>
#### 3、poll
```c
#include <poll.h>
int poll(struct pollfd *fds, nfds_t nfds, int timeout);

struct pollfd 
{
    int   fd;         /* file descriptor */
    short events;     /* requested events */
    short revents;    /* returned events */
};
```

<a name="b3865667"></a>
#### 4、epoll

![image-20220621150138380.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655812887265-efb47987-c703-4a80-8bd6-60beebe8bb2f.png#clientId=uc573125d-2b3a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ub52a0761&margin=%5Bobject%20Object%5D&name=image-20220621150138380.png&originHeight=771&originWidth=1272&originalType=binary&ratio=1&rotation=0&showTitle=false&size=360668&status=done&style=none&taskId=u95516d96-d2fa-4f92-929e-74227c355f2&title=)

```c
select/poll/epoll

listenfd       select   监听

//listenfd新的连接请求的标志
if(listenfd == 读事件)
{
    //有新的连接请求进来
    connfd = accept();
   //只要connfd是正常的
}

//之前老的连接上面有新的数据传送过来，write
if(connfd == 读事件)
{
    n = read;
    if(n > 0)
    {
        //数据能正常的接收
        //全部转换为大写
        //write回给客户端
    }
    else if(n == 0)
    {
        //客户端要断开连接
        //close(connfd);
    }
    else if(n == -1)//异常
    {
        close;
        return ;
    }
}

listenfd
    
nready = select/poll;
nready = 5;//有五个读事件满足条件
if(读事件 == listenfd)//有新的连接请求上来
{
    confd = accept;
    confd存在数据结构里面
}

if(读事件 == confd)//老客户端有新的需要读数据传过来，
{
    n = read;
    if(n > 0)
    {
        //数据能正常的接收
        //全部转换为大写
        //write回给客户端
    }
    else if(n == 0)
    {
        //客户端要断开连接
        //close(connfd);
    }
    else if(n == -1)//异常
    {
        close;
        return ;
    }
    
}
```

<a name="9e752f3c"></a>
### 五、回调函数

C语言  回调函数
```c
int pthread_create(pthread_t *thread, const pthread_attr_t *attr,
                          void *(*start_routine) (void *), void *arg);

void *threadFunc(void *arg)
{
    //
}

//C语言  中的结构体可以一次存大量数据
//void *
pthread_create(&thid, nullptr, threadFunc, arg);//注册threadFunc回调函数

//C语言中有个函数指针，有了结构体
void (*pFunc)();

pFunc = add;
pFunc = func;
```

C++
```c
void func(int x, int y)
{
    
}
funtion<void()> f = bind(func, _1, _2);//func注册
//业务逻辑
//..

f(100, 20);//执行
```


C++中的多态：类、虚函数、继承<br />C中：struct、函数指针


<a name="9959cff7"></a>
### 六、Reactor
![ReactorV5.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655814199886-1da4b197-3ff9-40a2-affb-8fdeadc29271.png#clientId=uc573125d-2b3a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=UgKXx&margin=%5Bobject%20Object%5D&name=ReactorV5.png&originHeight=1741&originWidth=4026&originalType=binary&ratio=1&rotation=0&showTitle=false&size=725444&status=done&style=none&taskId=ud3801ddc-3089-4527-8a8c-89fbab7aa3e&title=)

<a name="z9k0Z"></a>
#### Reactor V1 

![ReactorV1.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/916648/1655907907757-5aa6c2be-495d-45e2-a2b5-056a4674b3c1.jpeg#clientId=u224aa471-270c-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ud8466d5a&margin=%5Bobject%20Object%5D&name=ReactorV1.jpg&originHeight=872&originWidth=1073&originalType=binary&ratio=1&rotation=0&showTitle=false&size=197195&status=done&style=none&taskId=u99bffb12-ebc2-4788-9ef0-28b32ba08ae&title=)

1、InetAddress：网络地址类，负责所有的地址相关的操作，获取ip地址，获取端口号，strcut sockaddr_in
```cpp
// InetAdress.h
#ifndef __INETADDRESS_H__
#define __INETADDRESS_H__

#include <arpa/inet.h>

#include <string>

using std::string;

class InetAddress {
public:
    InetAddress(const string &ip, unsigned short port);
    InetAddress(const struct sockaddr_in &addr);
    ~InetAddress();
    string ip() const;
    unsigned short port() const;
    const sockaddr_in *getInetAddrPtr() const;

private:
    struct sockaddr_in _addr;
};

#endif
```

```cpp
// InetAdress.cc
#include "InetAddress.h"
/* #include <sys/types.h> */
/* #include <sys/socket.h> */
#include <strings.h>
/* #include <netinet/in.h> */

InetAddress::InetAddress(const string &ip, unsigned short port) {
    ::bzero(&_addr, sizeof(struct sockaddr_in));
    _addr.sin_family = AF_INET;
    _addr.sin_port = htons(port);
    _addr.sin_addr.s_addr = inet_addr(ip.c_str());  // host->network
}

InetAddress::InetAddress(const struct sockaddr_in &addr)
    : _addr(addr) {
}

InetAddress::~InetAddress() {
}
string InetAddress::ip() const {
    return string(inet_ntoa(_addr.sin_addr));
}

unsigned short InetAddress::port() const {
    return ntohs(_addr.sin_port);
}

const sockaddr_in *InetAddress::getInetAddrPtr() const {
    return &_addr;
}
```

2、Socket：套接字类，所有的与套接字相关的，都可以用这个类。
```cpp
//Socket.h
#ifndef __SOCKET_H__
#define __SOCKET_H__

#include "NonCopyable.h"

class Socket
    : NonCopyable {
public:
    Socket();
    explicit Socket(int fd);
    ~Socket();
    int fd() const;
    void shutDownWrite();

private:
    int _fd;
};

#endif
```

```cpp
// Socket.cc
#include "Socket.h"

#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

Socket::Socket() {
    _fd = ::socket(AF_INET, SOCK_STREAM, 0);
    if (_fd < 0) {
        perror("socket");
        return;
    }
}

Socket::Socket(int fd)
    : _fd(fd) {
}

Socket::~Socket() {
    close(_fd);
}

int Socket::fd() const {
    return _fd;
}

void Socket::shutDownWrite() {
    //关闭写端
    int ret = shutdown(_fd, SHUT_WR);
    if (ret) {
        perror("shutdown");
        return;
    }
}
```

3、Acceptor：连接器类，负责所有的 端口复用、listen、bind、accept
```cpp
// Acceptor.h
#ifndef __ACCEPTOR_H__
#define __ACCEPTOR_H__

#include "Socket.h"
#include "InetAddress.h"
#include <string>

using std::string;

class Acceptor
{
public:
    Acceptor(const string &ip, unsigned short port);
    ~Acceptor();
    void ready();
    void setReuseAddr();
    void setReusePort();
    void bind();
    void listen();
    int accept();
    int fd() const;

private:
    Socket _listenSock;
    InetAddress _servAddr;
};

#endif
```

```cpp
// Acceptor.cc
#include "Acceptor.h"

#include <stdio.h>

Acceptor::Acceptor(const string &ip, unsigned short port)
    : _listenSock(), _servAddr(ip, port) {
}

Acceptor::~Acceptor() {
}

void Acceptor::ready() {
    setReuseAddr();
    setReusePort();
    bind();
    listen();
}

void Acceptor::setReuseAddr() {
    int on = 1;
    int ret = setsockopt(_listenSock.fd(), SOL_SOCKET, SO_REUSEADDR, &on, sizeof(on));
    if (ret) {
        perror("setsockopt");
        return;
    }
}

void Acceptor::setReusePort() {
    int on = 1;
    int ret = setsockopt(_listenSock.fd(), SOL_SOCKET, SO_REUSEPORT, &on, sizeof(on));
    if (-1 == ret) {
        perror("setsockopt");
        return;
    }
}

void Acceptor::bind() {
    int ret = ::bind(_listenSock.fd(),
                     (struct sockaddr *)_servAddr.getInetAddrPtr(),
                     sizeof(struct sockaddr));
    if (-1 == ret) {
        perror("bind");
        return;
    }
}

void Acceptor::listen() {
    int ret = ::listen(_listenSock.fd(), 128);
    if (-1 == ret) {
        perror("listen");
        return;
    }
}

int Acceptor::accept() {
    int connfd = ::accept(_listenSock.fd(), nullptr, nullptr);
    if (-1 == connfd) {
        perror("listen");
        return -1;
    }
    return connfd;
}
int Acceptor::fd() const {
    return _listenSock.fd();
}
```

4、TcpConnection：TCP连接类，该对象创建完毕，就表名三次握手己经建立完毕，该连接就是一个TCP连接，该连接就可以进行发送数据与接收数据

```cpp
// TcpConnection.h
#ifndef __TCPCONNECTION_H__
#define __TCPCONNECTION_H__

#include "InetAddress.h"
#include "Socket.h"
#include "SocketIO.h"

class TcpConnection {
public:
    TcpConnection(int fd);
    ~TcpConnection();
    void send(const string &msg);
    string receive();
    string toString();

private:
    InetAddress getLocalAddr();
    InetAddress getPeerAddr();

private:
    Socket _sock;
    SocketIO _sockIO;
    InetAddress _localAddr;
    InetAddress _peerAddr;
};

#endif
```

```cpp
// TcpConnection.cc
#include "TcpConnection.h"

#include <iostream>
#include <sstream>

using std::cout;
using std::endl;
using std::ostringstream;

TcpConnection::TcpConnection(int fd)
    : _sock(fd)
    , _sockIO(fd)
    , _localAddr(getLocalAddr())
    , _peerAddr(getPeerAddr()) {    
    // 进入构造函数，对象空间已经创建完毕，只是没有初始化  
}

TcpConnection::~TcpConnection() {
    
}

void TcpConnection::send(const string &msg) {
    _sockIO.writen(msg.c_str(), msg.size());
}

string TcpConnection::receive() {
    char buff[65535] = {0};
    _sockIO.readLine(buff, sizeof(buff));

    return string(buff);
}

string TcpConnection::toString() {
    ostringstream oss;
    oss << _localAddr.ip() << ":"
        << _localAddr.port() << "---->"
        << _peerAddr.ip() << ":"
        << _peerAddr.port();

    return oss.str();
}

//获取本端的网络地址信息
InetAddress TcpConnection::getLocalAddr() {
    struct sockaddr_in addr;
    socklen_t len = sizeof(struct sockaddr);
    int ret = getsockname(_sock.fd(), (struct sockaddr *)&addr, &len);
    if (-1 == ret) {
        perror("getsockname");
    }

    return InetAddress(addr);
}

//获取对端的网络地址信息
InetAddress TcpConnection::getPeerAddr() {
    struct sockaddr_in addr;
    socklen_t len = sizeof(struct sockaddr);
    int ret = getpeername(_sock.fd(), (struct sockaddr *)&addr, &len);
    if (-1 == ret) {
        perror("getpeername");
    }

    return InetAddress(addr);
}
```

5、SocketIO：真正进行数据发送与接收的类。
```cpp
// SocketIO.h
#ifndef __SOCKETIO_H__
#define __SOCKETIO_H__

class SocketIO {
public:
    explicit SocketIO(int fd);
    ~SocketIO();
    int readn(char *buf, int len);
    int readLine(char *buf, int len);
    int writen(const char *buf, int len);

private:
    int _fd;
};

#endif
```

```cpp
//SocketIO.cc
#include "SocketIO.h"

#include <errno.h>
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

SocketIO::SocketIO(int fd)
    : _fd(fd) {
}

SocketIO::~SocketIO() {
    
}
int SocketIO::readn(char *buf, int len) {
    int left = len;
    char *pstr = buf;
    int ret = 0;

    while (left > 0) {
        ret = read(_fd, pstr, left);
        if (-1 == ret && errno == EINTR) {
            continue;
        } else if (-1 == ret) {
            perror("read error -1");
            return len - ret;
        } else if (0 == ret) {
            break;
        } else {
            pstr += ret;
            left -= ret;
        }
    }

    return len - left;
}

int SocketIO::readLine(char *buf, int len) {
    int left = len - 1;
    char *pstr = buf;
    int ret = 0, total = 0;

    while (left > 0) {
        //不会将缓冲区中的数据进行清空
        ret = recv(_fd, pstr, left, MSG_PEEK);
        if (-1 == ret && errno == EINTR) {
            continue;
        } else if (-1 == ret) {
            perror("readLine error -1");
            return len - ret;
        } else if (0 == ret) {
            break;
        } else {
            for (int idx = 0; idx < ret; ++idx) {
                if (pstr[idx] == '\n') {
                    int sz = idx + 1;
                    readn(pstr, sz);
                    pstr += sz;
                    *pstr = '\0';

                    return total + sz;
                }
            }

            readn(pstr, ret);  //从内核态拷贝到用户态
            total += ret;
            pstr += ret;
            left -= ret;
        }
    }
    *pstr = '\0';

    return total - left;
}

int SocketIO::writen(const char *buf, int len) {
    int left = len;
    const char *pstr = buf;
    int ret = 0;

    while (left > 0) {
        ret = write(_fd, pstr, left);
        if (-1 == ret && errno == EINTR) {
            continue;
        } else if (-1 == ret) {
            perror("writen error -1");
            return len - ret;
        } else if (0 == ret) {
            break;
        } else {
            pstr += ret;
            left -= ret;
        }
    }

    return len - left;
}
```
read 会将缓冲区的数据清空。<br />recv( xx，xx，xx，MSG_PEEK ) 发生拷贝操作，但不会从缓冲区中移除数据

测试文件：
```cpp
// TestTcpConnection.cc
#include "Acceptor.h"
#include "TcpConnection.h"
#include <iostream>
#include <unistd.h>

using std::cout;
using std::endl;

void test() {
    Acceptor acceptor("127.0.0.1", 8888);
    acceptor.ready();//此时处于监听状态

    //三次握手就已经建立，可以创建一条TCP连接
    TcpConnection con(acceptor.accept());

    cout << con.toString() << " has connected" << endl;

    while(1) {
        cout << ">>recv msg from client: " << con.receive() << endl;
        con.send("hello baby\n");
    }
}
int main(int argc, char **argv) {
    test();
    return 0;
}
```


<a name="ae130823"></a>
## C++Day32

<a name="318397f2"></a>
#### Tcp通信过程中的三个半事件
连接建立：包括服务器端被动接受连接（accept）和客户端主动发起连接（connect）。TCP连接一旦建立，客户端和服务端就是平等的，可以各自收发数据。<br />连接断开：包括主动断开（close、shutdown）和被动断开（read()返回0）。<br />消息到达：**文件描述符可读**。这是最为重要的一个事件，对它的处理方式决定了网络编程的风格（阻塞还是非阻塞，如何处理分包，应用层的缓冲如何设计等等）。<br />消息发送完毕：这算半个。对于低流量的服务，可不必关心这个事件；另外，这里的“发送完毕”是指数据写入操作系统缓冲区（内核缓冲区），将由TCP协议栈负责数据的发送与重传，不代表对方已经接收到数据。

<a name="iaRvN"></a>
#### Reactor V2
![ReactorV2.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/916648/1655908885952-2db559d6-d619-48b8-ad68-22e312629a8f.jpeg#clientId=u224aa471-270c-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uc5862b61&margin=%5Bobject%20Object%5D&name=ReactorV2.jpg&originHeight=1158&originWidth=1806&originalType=binary&ratio=1&rotation=0&showTitle=false&size=430735&status=done&style=none&taskId=u7991b218-63f5-40e2-9ab2-f27a8da2241&title=)


**回调函数**

TcpConnection
```cpp
// TcpConnection.h
#ifndef __TCPCONNECTION_H__
#define __TCPCONNECTION_H__

#include <functional>
#include <memory>

#include "InetAddress.h"
#include "Socket.h"
#include "SocketIO.h"

using std::function;
using std::shared_ptr;

class TcpConnection
    : public std::enable_shared_from_this<TcpConnection> {
    using TcpConnectionPtr = shared_ptr<TcpConnection>;
    using TcpConnectionCallback = function<void(const TcpConnectionPtr &)>;

public:
    TcpConnection(int fd);
    ~TcpConnection();
    void send(const string &msg);
    string receive();
    string toString();

    bool isClosed() const;

    //注册三个事件的回调函数
    void setConnectionCallback(const TcpConnectionCallback &cb);
    void setMessageCallback(const TcpConnectionCallback &cb);
    void setCloseCallback(const TcpConnectionCallback &cb);

    //三个事件回调函数的执行
    void handleConnectionCallback();
    void handleMessageCallback();
    void handleCloseCallback();

private:
    InetAddress getLocalAddr();
    InetAddress getPeerAddr();

private:
    Socket _sock;
    SocketIO _sockIO;
    InetAddress _localAddr;
    InetAddress _peerAddr;

    TcpConnectionCallback _onConnectionCb;
    TcpConnectionCallback _onMessageCb;
    TcpConnectionCallback _onCloseCb;
};

#endif
```

```cpp
// TcpConnection.cc
#include "TcpConnection.h"

#include <iostream>
#include <sstream>

using std::cout;
using std::endl;
using std::ostringstream;

TcpConnection::TcpConnection(int fd)
    : _sock(fd)
    , _sockIO(fd)
    , _localAddr(getLocalAddr())
    , _peerAddr(getPeerAddr()) {
    // 进入构造函数，对象空间已经创建完毕，只是没有初始化
}

TcpConnection::~TcpConnection() {

}

void TcpConnection::send(const string &msg) {
    _sockIO.writen(msg.c_str(), msg.size());
}

string TcpConnection::receive() {
    char buff[65535] = {0};
    _sockIO.readLine(buff, sizeof(buff));

    return string(buff);
}

string TcpConnection::toString() {
    ostringstream oss;
    oss << _localAddr.ip() << ":"
        << _localAddr.port() << "---->"
        << _peerAddr.ip() << ":"
        << _peerAddr.port();

    return oss.str();
}

bool TcpConnection::isClosed() const {
    char buf[10] = {};
    int ret = ::recv(_sock.fd(), buf, sizeof(buf), MSG_PEEK);

    return (ret == 0);
}

//获取本端的网络地址信息
InetAddress TcpConnection::getLocalAddr() {
    struct sockaddr_in addr;
    socklen_t len = sizeof(struct sockaddr);
    int ret = getsockname(_sock.fd(), (struct sockaddr *)&addr, &len);
    if (-1 == ret) {
        perror("getsockname");
    }

    return InetAddress(addr);
}

//获取对端的网络地址信息
InetAddress TcpConnection::getPeerAddr() {
    struct sockaddr_in addr;
    socklen_t len = sizeof(struct sockaddr);
    int ret = getpeername(_sock.fd(), (struct sockaddr *)&addr, &len);
    if (-1 == ret) {
        perror("getpeername");
    }

    return InetAddress(addr);
}

void TcpConnection::setConnectionCallback(const TcpConnectionCallback &cb) {
    _onConnectionCb = std::move(cb);
}

void TcpConnection::setMessageCallback(const TcpConnectionCallback &cb) {
    _onMessageCb = std::move(cb);
}

void TcpConnection::setCloseCallback(const TcpConnectionCallback &cb) {
    _onCloseCb = std::move(cb);
}

//三个事件回调函数的执行
void TcpConnection::handleConnectionCallback() {
    if (_onConnectionCb) {
        /* using TcpConnectionPtr = shared_ptr<TcpConnection>; */
        /* using TcpConnectionCallback = function<void(const TcpConnectionPtr &)>; */
        /* TcpConnectionCallback _onConnectionCb; */
        // function<void(const shared_ptr<TcpConnection> &)> _onConnectionCb;
        _onConnectionCb(shared_from_this());
    }
}
void TcpConnection::handleMessageCallback() {
    if (_onMessageCb) {
        _onMessageCb(shared_from_this());
    }
}
void TcpConnection::handleCloseCallback() {
    if (_onCloseCb) {
        _onCloseCb(shared_from_this());
    }
}
```

EventLoop
```cpp
// EventLoop.h
#ifndef __EVENTLOOP_H__
#define __EVENTLOOP_H__

#include <sys/epoll.h>

#include <functional>
#include <map>
#include <memory>
#include <vector>

#include "Acceptor.h"
#include "TcpConnection.h"

using std::function;
using std::map;
using std::shared_ptr;
using std::vector;

using TcpConnectionPtr = shared_ptr<TcpConnection>;
using TcpConnectionCallback = function<void(const TcpConnectionPtr &)>;

class EventLoop {
public:
    EventLoop(Acceptor &acceptor);
    ~EventLoop();
    void loop();
    void unloop();

    void setConnectionCallback(TcpConnectionCallback &&cb);
    void setMessageCallback(TcpConnectionCallback &&cb);
    void setCloseCallback(TcpConnectionCallback &&cb);

private:
    void waitEpollFd();
    void handleNewConnection();
    void handleMessage(int fd);
    int createEpollFd();
    void addEpollReadFd(int fd);
    void delEpollReadFd(int fd);

private:
    int _epfd;  //红黑树的根节点
    Acceptor &_acceptor;
    bool _isLooping;
    vector<struct epoll_event> _evtList;
    /* map<int, shared_ptr<TcpConnection>> _conns; */
    map<int, TcpConnectionPtr> _conns;

    TcpConnectionCallback _onConnectionCb;
    TcpConnectionCallback _onMessageCb;
    TcpConnectionCallback _onCloseCb;
};

#endif
```

```cpp
//EventLoop.cc
#include "EventLoop.h"

#include <unistd.h>

EventLoop::EventLoop(Acceptor &acceptor)
    : _epfd(createEpollFd())
    , _acceptor(acceptor)
    , _isLooping(false)
    , _evtList(1024) {
    addEpollReadFd(acceptor.fd());  //把listenfd放在红黑树上进行监听
}

EventLoop::~EventLoop() {
    if (_epfd) {
        close(_epfd);
    }
}

void EventLoop::loop() {
    _isLooping = true;
    while (_isLooping) {
        waitEpollFd();
    }
}

void EventLoop::unloop() {
    _isLooping = false;
}

void EventLoop::waitEpollFd() {
    int nready = -1;
    do {
        nready = ::epoll_wait(_epfd, &*_evtList.begin(), _evtList.size(), 5000);
    } while (-1 == nready && errno == EINTR);

    if (-1 == nready) {
        perror("nready == -1");
        return;
    } else if (0 == nready) {
        printf(">>epoll_wait timeout\n");
    } else {
        if (nready == (int)_evtList.size()) {
            _evtList.resize(2 * nready);  //考虑到了监听超过上限的问题
        }

        for (int idx = 0; idx < nready; ++idx) {
            int fd = _evtList[idx].data.fd;
            if (fd == _acceptor.fd())  //有新的连接请求进来
            {
                if (_evtList[idx].events & EPOLLIN) {
                    handleNewConnection();
                }
            } else {
                if (_evtList[idx].events & EPOLLIN) {
                    handleMessage(fd);  //有数据的传输
                }
            }
        }
    }
}
void EventLoop::handleNewConnection() {
    //只要peerfd有正确的返回值，就证明三次握手已经建立完成
    int peerfd = _acceptor.accept();
    addEpollReadFd(peerfd);  //把peerfd放到红黑树上进行监听

    TcpConnectionPtr con(new TcpConnection(peerfd));

    // Tcp连接创建之后就可以进行三个事件的注册
    con->setConnectionCallback(_onConnectionCb);  //连接建立
    con->setMessageCallback(_onMessageCb);        //消息的到达
    con->setCloseCallback(_onCloseCb);            //连接的断开

    _conns.insert(std::make_pair(peerfd, con));
    con->handleConnectionCallback();
}

void EventLoop::handleMessage(int fd) {
    auto iter = _conns.find(fd);
    if (iter != _conns.end()) {
        //用Tcp连接里面定义一个函数
        // isClose,里面执行recv，recv的返回值等于0
        //
        bool flag = iter->second->isClosed();
        if (flag) {
            //连接是断开的
            iter->second->handleCloseCallback();
            delEpollReadFd(fd);  //将文件描述符从红黑树上删除
            _conns.erase(iter);  //将文件描述符从map中删除

        } else {
            //连接是正常
            iter->second->handleMessageCallback();
        }

    } else {
        /* cout << "该连接不存在" << endl; */
        printf("该连接不存在\n");
    }
}

int EventLoop::createEpollFd() {
    int fd = epoll_create(100);
    if (-1 == fd) {
        perror("epoll_create");
        return -1;
    }
    return fd;
}

void EventLoop::addEpollReadFd(int fd) {
    struct epoll_event evt;
    evt.events = EPOLLIN;
    evt.data.fd = fd;

    int ret = ::epoll_ctl(_epfd, EPOLL_CTL_ADD, fd, &evt);
    if (ret == -1) {
        perror("epoll_ctl add");
        return;
    }
}

void EventLoop::delEpollReadFd(int fd) {
    struct epoll_event evt;
    evt.events = EPOLLIN;
    evt.data.fd = fd;

    int ret = ::epoll_ctl(_epfd, EPOLL_CTL_DEL, fd, &evt);
    if (ret == -1) {
        perror("epoll_ctl del");
        return;
    }
}

void EventLoop::setConnectionCallback(TcpConnectionCallback &&cb) {
    _onConnectionCb = std::move(cb);
}

void EventLoop::setMessageCallback(TcpConnectionCallback &&cb) {
    _onMessageCb = std::move(cb);
}

void EventLoop::setCloseCallback(TcpConnectionCallback &&cb) {
    _onCloseCb = std::move(cb);
}
```

测试文件：
```cpp
// TestEventLoop.cc
#include <unistd.h>

#include <iostream>

#include "Acceptor.h"
#include "EventLoop.h"
#include "TcpConnection.h"

using std::cout;
using std::endl;

void onConnection(const TcpConnectionPtr &con) {
    cout << con->toString() << " has connected!" << endl;
}

void onMessage(const TcpConnectionPtr &con) {
    string msg = con->receive();
    cout << "recv msg  " << msg << endl;
    //接收与发送之间，消息msg是没有做任何处理的
    //...
    //
    con->send(msg);
}

void onClose(const TcpConnectionPtr &con) {
    cout << con->toString() << " has closed!" << endl;
}

void test() {
    Acceptor acceptor("127.0.0.1", 8888);
    acceptor.ready();  //此时处于监听状态

    EventLoop loop(acceptor);
    //回调函数的注册
    loop.setConnectionCallback(std::move(onConnection));
    loop.setMessageCallback(std::move(onMessage));
    loop.setCloseCallback(std::move(onClose));

    loop.loop();
}
int main(int argc, char **argv) {
    test();
    return 0;
}
```

Test  ( 注册、执行） --使用-->  EventLoop ( 容器、注册、执行 )  --调用--> TcpConnection ( 容器、 注册、执行 )


<a name="80078dce"></a>
## C++Day33

epoll处理的逻辑：
```c
void waitEpollFd()
{
    nready = epoll_wait;
    if(-1 == nready && errno == EINTR)
    {
        //....
    }
    else if(-1 == nready)
    {
        perror;
        return;
    }
    else if(0 == nready)
    {
        printf("");
    }
    else 
    {
        for(idx = 0; idx < nready; ++idx);
        {
            if(fd == listenfd)
            {
                //处理新的链接
                handleNewConnetion();
            }
            else
            {
                //数据的收发
                handleMessage(fd);
            }
        }
    }
}


void handleNewConnetion()
{
    //三次握手就建立
   peerfd =  accptor.accept;
    
   //创建tcp链接
    TcpConnecttion con(peerfd);
    //注册三个回调函数
    con.setConnectCallback();
    con.setMessageCallback();
    con.setCloseCallback();
    
    //把peerfd与con存在数据结构里面去map<peerfd, con>
    con.handleConnectionCallback();
    
}

void handleMessage(fd)
{
    //本来应该做数据的发送与接收
    n = recv;
    if(n > 0)
    {
        write();
    }
    else if(n < 0)
    {
        //异常处理
    }
    else 
    {
        //n = 0
        //断开连接
        //文件描述符fd从红黑树上删除
    }
    
}
```


<a name="hzrrU"></a>
#### Reactor V3
![ReactorV3.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/916648/1656037714591-49fd3e60-7c74-4506-a67d-262ca53f26c9.jpeg#clientId=u84773e56-5773-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uc5bdc1af&margin=%5Bobject%20Object%5D&name=ReactorV3.jpg&originHeight=1862&originWidth=1782&originalType=binary&ratio=1&rotation=0&showTitle=false&size=181141&status=done&style=none&taskId=u7ee90302-3785-4b18-ad86-68b7d242ce7&title=)

将V2中 TestEventLoop.cc 进一步封装成  TcpServer.h
```cpp
// TcpServer.h
#ifndef __TCPSERVER_H__
#define __TCPSERVER_H__

#include <unistd.h>

#include <iostream>

#include "Acceptor.h"
#include "EventLoop.h"
#include "TcpConnection.h"

using std::cout;
using std::endl;

class TcpServer {
public:
    TcpServer(const string &ip, unsigned short port)
        : _acceptor(ip, port)
        , _loop(_acceptor) {

    }

    void start() {
        _acceptor.ready();
        _loop.loop();
    }

    void stop() {
        _loop.unloop();
    }

    void setAllCallback(TcpConnectionCallback &&onConnection,
                        TcpConnectionCallback &&onMessage,
                        TcpConnectionCallback &&onClose) {
        _loop.setConnectionCallback(std::move(onConnection));
        _loop.setMessageCallback(std::move(onMessage));
        _loop.setCloseCallback(std::move(onClose));
    }

private:
    Acceptor _acceptor;
    EventLoop _loop;
};

#endif
```

测试文件：
```cpp
// TestTcpServer.cc
#include <unistd.h>

#include <iostream>

#include "TcpServer.h"

using std::cout;
using std::endl;

void onConnection(const TcpConnectionPtr &con) {
    cout << con->toString() << " has connected!" << endl;
}

void onMessage(const TcpConnectionPtr &con) {
    //回显
    string msg = con->receive();
    cout << "recv msg  " << msg << endl;
    //接收与发送之间，消息msg是没有做任何处理的
    //...
    //
    //处理msg的业务逻辑全部在此处实现的话
    //将msg这些信息打个包交给MyTask，然后将MyTask注册给线程池
    //让线程池去处理具体的业务逻辑，此时业务逻辑的处理就不在
    // EventLoop线程中

    /* MyTask task(msg); */
    /* threadPool.addTask(task); */

    con->send(msg);
}

void onClose(const TcpConnectionPtr &con) {
    cout << con->toString() << " has closed!" << endl;
}

void testV2() {
    Acceptor acceptor("127.0.0.1", 8888);
    acceptor.ready();  //此时处于监听状态

    EventLoop loop(acceptor);
    //回调函数的注册
    loop.setConnectionCallback(std::move(onConnection));
    loop.setMessageCallback(std::move(onMessage));
    loop.setCloseCallback(std::move(onClose));

    loop.loop();
}

void testV3() {
    TcpServer server("127.0.0.1", 8888);
    server.setAllCallback(std::move(onConnection)
                        , std::move(onMessage)
                        , std::move(onClose));

    server.start();
}
int main(int argc, char **argv) {
    testV3();
    return 0;
}
```


EventLoop对应的线程：就是负责数据的收发，也就是基本IO操作，**IO线程**<br />ThreadPool线程池对应的线程：去处理正常的业务逻辑，处理编解码、计算的。**计算线程**

<a name="4b3e50d9"></a>
### eventfd的使用
特点：可以在进程或线程间进行通信。<br />eventfd返回一个文件描述符，evtfd，A线程与B线程如果都可以看到evtfd。A线程取进行read操作，B线程进行write操作

函数接口
```c
#include <sys/eventfd.h>
int eventfd(unsigned int initval, int flags);
initval:计数器的值，由内核进行维护。
flag：早期版本（2.6.26）之前直接设置0,2.6.26版本之后设置为其他值。
```
A进程对应是父进程，父进程进行read操作。会读evtfd文件描述符对应的数据，并且将该数据清空为0。<br />B进程对应是子进程，子进程进行warite操作，write可以将evtfd对应的内核维护的数据进行累加操作。

<a name="XkFtA"></a>
#### eventfd的封装
![image-20220623170753708.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656171581722-baa99032-67d9-40b9-9967-f5c92807de74.png#clientId=u84773e56-5773-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u61af6231&margin=%5Bobject%20Object%5D&name=image-20220623170753708.png&originHeight=480&originWidth=979&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33132&status=done&style=none&taskId=u04725c15-c1c0-483a-a927-4b034bb90df&title=)


<a name="TDyGS"></a>
#### Reactor V4

Thread.h  (`vector<unique_ptr<Thread>> _threads;` )
```cpp
// Thread.h
#ifndef __THREADPOOL_H__
#define __THREADPOOL_H__

#include <memory>
#include <vector>

#include "TaskQueue.h"
#include "Thread.h"

using std::unique_ptr;
using std::vector;

class ThreadPool {
public:
    ThreadPool(size_t threadNum, size_t queSize);
    ~ThreadPool();

    void start();
    void stop();

    void addTask(Task &&cb);
    Task getTask();

private:
    void threadFunc();

private:
    size_t _threadNum;
    size_t _queSize;
    vector<unique_ptr<Thread>> _threads;
    TaskQueue _taskQue;
    bool _isExit;
};

#endif
```

TcpConnection.h ( `sendInLoop()` )
```cpp
// TcpConnection.h
#ifndef __TCPCONNECTION_H__
#define __TCPCONNECTION_H__

#include "Socket.h"
#include "SocketIO.h"
#include "InetAddress.h"
#include <memory>
#include <functional>

using std::shared_ptr;
using std::function;

class EventLoop;

class TcpConnection
    : public std::enable_shared_from_this<TcpConnection> {
    using TcpConnectionPtr = shared_ptr<TcpConnection>;
    using TcpConnectionCallback = function<void(const TcpConnectionPtr &)>;

public:
    TcpConnection(int fd, EventLoop *loop);
    ~TcpConnection();
    void send(const string &msg);
    void sendInLoop(const string &msg);
    string receive();
    string toString();

    bool isClosed() const;

    //注册三个事件的回调函数
    void setConnectionCallback(const TcpConnectionCallback &cb);
    void setMessageCallback(const TcpConnectionCallback &cb);
    void setCloseCallback(const TcpConnectionCallback &cb);

    //三个事件回调函数的执行
    void handleConnectionCallback();
    void handleMessageCallback();
    void handleCloseCallback();

private:
    InetAddress getLocalAddr();
    InetAddress getPeerAddr();
private:
    EventLoop *_loop;
    Socket _sock;
    SocketIO _sockIO;
    InetAddress _localAddr;
    InetAddress _peerAddr;

    TcpConnectionCallback _onConnectionCb;
    TcpConnectionCallback _onMessageCb;
    TcpConnectionCallback _onCloseCb;

};

#endif
```

```cpp
// TcpConnection.cc
#include "TcpConnection.h"

#include <iostream>
#include <sstream>

#include "EventLoop.h"

using std::cout;
using std::endl;
using std::ostringstream;

TcpConnection::TcpConnection(int fd, EventLoop *loop)
    : _loop(loop)
    , _sock(fd)
    , _sockIO(fd)
    , _localAddr(getLocalAddr())
    , _peerAddr(getPeerAddr()) {

}

TcpConnection::~TcpConnection() {

}

void TcpConnection::send(const string &msg) {
    _sockIO.writen(msg.c_str(), msg.size());
}

void TcpConnection::sendInLoop(const string &msg) {
    if (_loop) {
        //注册到EventLoop
        _loop->runInLoop(std::bind(&TcpConnection::send, this, msg));
        // void runInLoop(function<void()> &&cb);
    }
}

string TcpConnection::receive() {
    char buff[65535] = {0};
    _sockIO.readLine(buff, sizeof(buff));

    return string(buff);
}

string TcpConnection::toString() {
    ostringstream oss;
    oss << _localAddr.ip() << ":"
        << _localAddr.port() << "---->"
        << _peerAddr.ip() << ":"
        << _peerAddr.port();

    return oss.str();
}

bool TcpConnection::isClosed() const {
    char buf[10] = {};
    int ret = ::recv(_sock.fd(), buf, sizeof(buf), MSG_PEEK);

    return (ret == 0);
}

//获取本端的网络地址信息
InetAddress TcpConnection::getLocalAddr() {
    struct sockaddr_in addr;
    socklen_t len = sizeof(struct sockaddr);
    int ret = getsockname(_sock.fd(), (struct sockaddr *)&addr, &len);
    if (-1 == ret) {
        perror("getsockname");
    }

    return InetAddress(addr);
}

//获取对端的网络地址信息
InetAddress TcpConnection::getPeerAddr() {
    struct sockaddr_in addr;
    socklen_t len = sizeof(struct sockaddr);
    int ret = getpeername(_sock.fd(), (struct sockaddr *)&addr, &len);
    if (-1 == ret) {
        perror("getpeername");
    }

    return InetAddress(addr);
}

void TcpConnection::setConnectionCallback(const TcpConnectionCallback &cb) {
    _onConnectionCb = std::move(cb);
}

void TcpConnection::setMessageCallback(const TcpConnectionCallback &cb) {
    _onMessageCb = std::move(cb);
}

void TcpConnection::setCloseCallback(const TcpConnectionCallback &cb) {
    _onCloseCb = std::move(cb);
}

//三个事件回调函数的执行
void TcpConnection::handleConnectionCallback() {
    if (_onConnectionCb) {
        /* using TcpConnectionPtr = shared_ptr<TcpConnection>; */
        /* using TcpConnectionCallback = function<void(const TcpConnectionPtr &)>; */
        /* TcpConnectionCallback _onConnectionCb; */
        // function<void(const shared_ptr<TcpConnection> &)> _onConnectionCb;
        _onConnectionCb(shared_from_this());
    }
}
void TcpConnection::handleMessageCallback() {
    if (_onMessageCb) {
        _onMessageCb(shared_from_this());
    }
}
void TcpConnection::handleCloseCallback() {
    if (_onCloseCb) {
        _onCloseCb(shared_from_this());
    }
}
```

EventLoop.h( `RunInLoop()` 、`map<fd,con>`  、 EventFd( `wakeup() `、 `doPendingsFunctors()` )
```cpp
// EventLoop.h
#ifndef __EVENTLOOP_H__
#define __EVENTLOOP_H__

#include <sys/epoll.h>

#include <functional>
#include <map>
#include <memory>
#include <vector>

#include "Acceptor.h"
#include "MutexLock.h"
#include "TcpConnection.h"

using std::function;
using std::map;
using std::shared_ptr;
using std::vector;

using TcpConnectionPtr = shared_ptr<TcpConnection>;
using TcpConnectionCallback = function<void(const TcpConnectionPtr &)>;
using Functor = function<void()>;

class EventLoop {
public:
    EventLoop(Acceptor &acceptor);
    ~EventLoop();
    void loop();
    void unloop();

    void runInLoop(Functor &&cb);

    void wakeup();
    void handleRead();

    void doPengingFunctors();

    void setConnectionCallback(TcpConnectionCallback &&cb);
    void setMessageCallback(TcpConnectionCallback &&cb);
    void setCloseCallback(TcpConnectionCallback &&cb);

private:
    void waitEpollFd();
    void handleNewConnection();
    void handleMessage(int fd);
    int createEpollFd();
    void addEpollReadFd(int fd);
    void delEpollReadFd(int fd);
    int createEventFd();

private:
    int _epfd;  //红黑树的根节点
    int _evtfd;
    Acceptor &_acceptor;
    bool _isLooping;
    vector<struct epoll_event> _evtList;
    /* map<int, shared_ptr<TcpConnection>> _conns; */
    map<int, TcpConnectionPtr> _conns;

    TcpConnectionCallback _onConnectionCb;
    TcpConnectionCallback _onMessageCb;
    TcpConnectionCallback _onCloseCb;

    vector<Functor> _pengingsCb;
    MutexLock _mutex;
};

#endif
```

```cpp
//EventLoop.h
#include "EventLoop.h"

#include <sys/eventfd.h>
#include <unistd.h>

EventLoop::EventLoop(Acceptor &acceptor)
    : _epfd(createEpollFd())
    , _evtfd(createEventFd())
    , _acceptor(acceptor)
    , _isLooping(false)
    , _evtList(1024) {
    addEpollReadFd(acceptor.fd());  //把listenfd放在红黑树上进行监听
    addEpollReadFd(_evtfd);         //放在红黑树上进行监听
}

EventLoop::~EventLoop() {
    if (_epfd) {
        close(_epfd);
    }

    if (_evtfd) {
        close(_evtfd);
    }
}

void EventLoop::loop() {
    _isLooping = true;
    while (_isLooping) {
        waitEpollFd();
    }
}

void EventLoop::unloop() {
    _isLooping = false;
}

void EventLoop::runInLoop(Functor &&cb) {
    //可以使用大括号将某些栈变量/栈对象提前结束
    {
        MutexLockGuard autoLock(_mutex);
        _pengingsCb.push_back(std::move(cb));
    }

    //....
    //...
    wakeup();
}

void EventLoop::doPengingFunctors() {
    vector<Functor> tmp;
    {
        //粒度
        MutexLockGuard autoLock(_mutex);
        tmp.swap(_pengingsCb);
    }

    // vector<Functor> _pengingsCb;
    for (auto &cb : tmp) {
        cb();
    }
}

void EventLoop::wakeup() {
    uint64_t one = 1;
    int ret = ::write(_evtfd, &one, sizeof(one));
    if (ret != sizeof(one)) {
        perror("write");
        return;
    }
}

void EventLoop::handleRead() {
    uint64_t one = 1;
    int ret = ::read(_evtfd, &one, sizeof(one));
    if (ret != sizeof(one)) {
        perror("read");
        return;
    }
}
void EventLoop::waitEpollFd() {
    int nready = -1;
    do {
        nready = ::epoll_wait(_epfd, &*_evtList.begin(), _evtList.size(), 5000);
    } while (-1 == nready && errno == EINTR);

    if (-1 == nready) {
        perror("nready == -1");
        return;
    } else if (0 == nready) {
        printf(">>epoll_wait timeout\n");
    } else {
        if (nready == (int)_evtList.size()) {
            _evtList.resize(2 * nready);  //考虑到了监听超过上限的问题
        }

        for (int idx = 0; idx < nready; ++idx) {
            int fd = _evtList[idx].data.fd;
            if (fd == _acceptor.fd())  //有新的连接请求进来
            {
                if (_evtList[idx].events & EPOLLIN) {
                    handleNewConnection();
                }
            } else if (fd == _evtfd) {
                handleRead();
                doPengingFunctors();
            } else {
                if (_evtList[idx].events & EPOLLIN) {
                    handleMessage(fd);  //有数据的传输
                }
            }
        }
    }
}
void EventLoop::handleNewConnection() {
    //只要peerfd有正确的返回值，就证明三次握手已经建立完成
    int peerfd = _acceptor.accept();
    addEpollReadFd(peerfd);  //把peerfd放到红黑树上进行监听

    TcpConnectionPtr con(new TcpConnection(peerfd, this));

    // Tcp连接创建之后就可以进行三个事件的注册
    con->setConnectionCallback(_onConnectionCb);  //连接建立
    con->setMessageCallback(_onMessageCb);        //消息的到达
    con->setCloseCallback(_onCloseCb);            //连接的断开

    _conns.insert(std::make_pair(peerfd, con));
    con->handleConnectionCallback();
}

void EventLoop::handleMessage(int fd) {
    auto iter = _conns.find(fd);
    if (iter != _conns.end()) {
        //用Tcp连接里面定义一个函数
        // isClose,里面执行recv，recv的返回值等于0
        //
        bool flag = iter->second->isClosed();
        if (flag) {
            //连接是断开的
            iter->second->handleCloseCallback();
            delEpollReadFd(fd);  //将文件描述符从红黑树上删除
            _conns.erase(iter);  //将文件描述符从map中删除

        } else {
            //连接是正常
            iter->second->handleMessageCallback();
        }

    } else {
        /* cout << "该连接不存在" << endl; */
        printf("该连接不存在\n");
    }
}

int EventLoop::createEpollFd() {
    int fd = epoll_create(100);
    if (-1 == fd) {
        perror("epoll_create");
        return -1;
    }
    return fd;
}

void EventLoop::addEpollReadFd(int fd) {
    struct epoll_event evt;
    evt.events = EPOLLIN;
    evt.data.fd = fd;

    int ret = ::epoll_ctl(_epfd, EPOLL_CTL_ADD, fd, &evt);
    if (ret == -1) {
        perror("epoll_ctl add");
        return;
    }
}

void EventLoop::delEpollReadFd(int fd) {
    struct epoll_event evt;
    evt.events = EPOLLIN;
    evt.data.fd = fd;

    int ret = ::epoll_ctl(_epfd, EPOLL_CTL_DEL, fd, &evt);
    if (ret == -1) {
        perror("epoll_ctl del");
        return;
    }
}

void EventLoop::setConnectionCallback(TcpConnectionCallback &&cb) {
    _onConnectionCb = std::move(cb);
}

void EventLoop::setMessageCallback(TcpConnectionCallback &&cb) {
    _onMessageCb = std::move(cb);
}

void EventLoop::setCloseCallback(TcpConnectionCallback &&cb) {
    _onCloseCb = std::move(cb);
}
int EventLoop::createEventFd() {
    int fd = eventfd(10, 0);
    if (-1 == fd) {
        perror("eventfd");
        return -1;
    }

    return fd;
}
```

测试文件：
```cpp
TestTcpServer.cc
#include <unistd.h>

#include <iostream>

#include "TcpServer.h"
#include "ThreadPool.h"

using std::cout;
using std::endl;

class MyTask {
public:
    MyTask(const string &msg, const TcpConnectionPtr &con)
        : _msg(msg), _con(con) {
    }

    //该函数在线程池中执行的
    void process() {
        //在process函数中去进行真正的业务逻辑的处理
        //....
        //...
        /* string newMsg = msg + 1; */
        //现在计算线程（ThreadPool）处理完业务逻辑之后，需要
        //将处理完后数据发送给IO线程（EventLoop/Reactor），
        // IO线程如何与计算线程进行通信？(eventfd)
        _con->sendInLoop(_msg);
        //数据的发送需要在EventLoop里面进行发送
        // TcpConnection需要将数据发送给EventLoop，让EventLoop去
        //进行发送数据IO操作
        //此时TcpConnection需要知道EventLoop存在
    }

private:
    string _msg;
    TcpConnectionPtr _con;
};

ThreadPool *gThreadPool = nullptr;

void onConnection(const TcpConnectionPtr &con) {
    cout << con->toString() << " has connected!" << endl;
}

void onMessage(const TcpConnectionPtr &con) {
    //回显
    string msg = con->receive();
    cout << "recv msg  " << msg << endl;
    //接收与发送之间，消息msg是没有做任何处理的
    //...
    //
    //处理msg的业务逻辑全部在此处实现的话
    //将msg这些信息打个包交给MyTask，然后将MyTask注册给线程池
    //让线程池去处理具体的业务逻辑，此时业务逻辑的处理就不在
    // EventLoop线程中

    MyTask task(msg, con);
    /* gThreadPool->addTask(std::bind(&MyTask::process, &task)); */
    gThreadPool->addTask(std::bind(&MyTask::process, task));

    /* con->send(msg); */
}

void onClose(const TcpConnectionPtr &con) {
    cout << con->toString() << " has closed!" << endl;
}

void testV2() {
    Acceptor acceptor("127.0.0.1", 8888);
    acceptor.ready();  //此时处于监听状态

    EventLoop loop(acceptor);
    //回调函数的注册
    loop.setConnectionCallback(std::move(onConnection));
    loop.setMessageCallback(std::move(onMessage));
    loop.setCloseCallback(std::move(onClose));

    loop.loop();
}

void testV4() {
    ThreadPool threadPool(5, 10);  //局部变量
    threadPool.start();
    gThreadPool = &threadPool;

    TcpServer server("127.0.0.1", 8888);
    server.setAllCallback(std::move(onConnection)
                        , std::move(onMessage)
                        , std::move(onClose));

    server.start();
}

int main(int argc, char **argv) {
    testV4();
    return 0;
}
```


<a name="XwypT"></a>
#### Reactor V5

![fde2b313-02c1-4a5e-b36a-cbb81ca189ff.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/916648/1656064110645-1042d07e-faad-4c6d-baf4-2f4bde3ca108.jpeg#clientId=u84773e56-5773-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ue4db8583&margin=%5Bobject%20Object%5D&name=fde2b313-02c1-4a5e-b36a-cbb81ca189ff.jpg&originHeight=1351&originWidth=3316&originalType=binary&ratio=1&rotation=0&showTitle=false&size=723969&status=done&style=none&taskId=u7b148d87-f062-4fb8-92c1-640fbf02643&title=)

[https://gitee.com/yangxf98/Reactor/tree/master/ReactorV5](https://gitee.com/yangxf98/Reactor/tree/master/ReactorV5)



<a name="688bb85b"></a>
## C++Day34

<a name="9286ec07"></a>
### timerfd的封装
```c
int timerfd_create(int clockid, int flags);
功能：该函数生成一个定时器对象，返回与之关联的文件描述符。
参数详解：
clockid:可设置为
CLOCK_REALTIME：相对时间，从1970.1.1到目前的时间。更改系统时间 会更改获取的值，它以系统时间为坐标。
CLOCK_MONOTONIC：绝对时间，获取的时间为系统重启到现在的时间，更改系统时间对齐没有影响。
flags: 可设置为
TFD_NONBLOCK（非阻塞），
TFD_CLOEXEC（同O_CLOEXEC）
linux内核2.6.26版本以上都指定为0
```

```c
int timerfd_settime(int fd, int flags, const struct itimerspec *new_value,
                                       struct itimerspec *old_value);
功能：该函数能够启动和停止定时器
参数详解：
fd: timerfd对应的文件描述符
flags: 
    0表示是相对定时器
    TFD_TIMER_ABSTIME表示是绝对定时器
new_value:设置超时时间，如果为0则表示停止定时器。
old_value:一般设为NULL, 不为NULL,则返回定时器这次设置之前的超时时间
    
struct timespec 
{
    time_t tv_sec;                /* Seconds */
    long   tv_nsec;               /* Nanoseconds */
};

struct itimerspec 
{
    struct timespec it_interval;  /* Interval for periodic timer */
    struct timespec it_value;     /* Initial expiration */
};
```

```c
read：读取缓冲区中的数据，其占据的存储空间，为sizeof(uint64_t)，表示超时次数。

select/poll/epoll：当定时器超时时，会触发定时器相对应的文件描述符上的读操作，IO复用操作会返回，然后再去对该读事件进行处理。
```

![image-20220624174913775.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656171686942-b606f909-7cdf-4e44-a39d-95d560e0cde4.png#clientId=u84773e56-5773-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ub47f52f8&margin=%5Bobject%20Object%5D&name=image-20220624174913775.png&originHeight=402&originWidth=967&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30313&status=done&style=none&taskId=u391a2ca7-2c66-4190-abea-c536d667171&title=)
