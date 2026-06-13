
<a name="YkLFn"></a>
## 工程课的特点：

- 会大量引入第三方框架和产品
- 不要求掌握产品的所有细节，把精力放在和业务需求相关的功能

学习上的要求：

- 不要求全 会用、懂原理
- 注重实践 下课时间 马上练习
- 逻辑性不强 了解问题场景&解决方案
- 一定要记录笔记
- 广度优先

<a name="cy3ZD"></a>
## 课程大纲 
HTTP协议

- 自己写一个简单的http服务端 了解协议的内容
- nginx
- 利用nginx 反向代理 缓存 负载均衡

HTTP的库

- workflow 搜狗公司的一个开源库 异步回调
- 分块上传功能 redis实现缓存
- 网盘的一般的功能

分布式架构的网盘

- 使用ceph或者OSS持久存储数据
- 使用消息队列rabbitmq实现异步转移
- 远程过程调用rpc
- 序列化和反序列化 protobuf
- 使用现有的rpc框架 srpc搜狗公司
- 服务注册中心consul 分布式系统

分布式的理论

- 底层所使用的共识协议 raft
- ACID vs BASE

Lua课程

- Lua的语法
-  Lua和openresty


<a name="oKcuT"></a>
## HTTP
超文本传输协议

<a name="uwrKa"></a>
#### 网络协议
应用层协议：ISO/OSI  第7层    TCP/IP  第4(5)层<br />基于可靠传输的传输层  一般是TCP

<a name="UaWt2"></a>
#### 传输模型 C/S
`client` 发送请求， `server` 回复一个请求  <br />(请求， 响应)   ——>  事务


![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656733325427-16d350ee-7fa8-45c6-b03f-51a1e08a4eb2.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=316&id=u34afb8a0&margin=%5Bobject%20Object%5D&name=image.png&originHeight=434&originWidth=1096&originalType=binary&ratio=1&rotation=0&showTitle=false&size=263523&status=done&style=none&taskId=u92dcbd3b-b7e1-4e22-91b9-184b6ed4bda&title=&width=797.0909090909091)<br />超文本 HTML<br />二进制及其他任何类型的数据

<a name="hLU5w"></a>
#### 网页的组成：
HTML ： 网页的骨架 + 内容（超链接）<br />CSS  ：  层叠样式文件（字体，格式，位置）<br />Javascript ： 动态行为

<a name="a5ou4"></a>
#### http协议的特点
应用层协议<br />C/S模型   `client` 发送请求， `server` 回复一个请求 <br />可靠    传输层<br />文本协议      头（ 文本协议 ） + 载荷（二进制/文本 ）<br />无状态协议    stateless   （ 无状态  ：事务结束以后， 不占用任何内存 ）<br />无状态好处：

         1. 一个事务对另一个事务没有影响
         1. 支持水平拓展

有状态  ： 支持垂直拓展<br />无状态  ： 支持垂直拓展，水平拓展<br />（ 数据 存下来， 不支持水平拓展  （存到数据库，此时的数据库不支持水平拓） ）

<a name="eoXzu"></a>
## day02
http 模型的头部是可读的，body可以装载所有类型的数据<br />http是一种无状态的协议<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656940446064-0029d291-9234-417b-a30c-9b14513e933f.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0.0607&crop=1&crop=0.9454&from=paste&height=165&id=u276d2d47&margin=%5Bobject%20Object%5D&name=image.png&originHeight=227&originWidth=475&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20515&status=done&style=none&taskId=u08d57015-9753-4b37-8ed0-a21d78e8c8e&title=&width=345)

<a name="hEiNO"></a>
#### 把状态转移到客户端：
浏览器     本地可以存储数据       cookie<br />session ： <br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656940502882-c7b91a0b-ea5a-4a0a-8abc-e132c2bd28bb.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0.0277&crop=1&crop=0.9908&from=paste&height=108&id=ua06f0b72&margin=%5Bobject%20Object%5D&name=image.png&originHeight=149&originWidth=501&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14530&status=done&style=none&taskId=u962d801e-39d7-41e1-bdfc-68b2fbb54e7&title=&width=364)<br />token ： <br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656940519609-5bb66658-cb83-4291-bb70-fb28768a21ee.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0.0393&crop=1&crop=0.9607&from=paste&height=129&id=u52e26bf9&margin=%5Bobject%20Object%5D&name=image.png&originHeight=177&originWidth=668&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21491&status=done&style=none&taskId=u6ea7d054-2cca-45c6-8fb9-34c2c68101b&title=&width=486)

<a name="dH3JJ"></a>
#### 浏览器 
天生是http的客户端

<a name="a9Mob"></a>
#### html的结构
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656940735435-2a22839c-a3e9-4689-a239-e79aac322be8.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=331&id=u510d9906&margin=%5Bobject%20Object%5D&name=image.png&originHeight=755&originWidth=1050&originalType=binary&ratio=1&rotation=0&showTitle=false&size=230951&status=done&style=none&taskId=udfaadae1-9c4a-4447-929c-67df1995ab5&title=&width=460.727294921875)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656940786400-2b75d122-ce9f-4adc-a894-c6af0b6b6dfc.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=309&id=u141e924c&margin=%5Bobject%20Object%5D&name=image.png&originHeight=364&originWidth=475&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31523&status=done&style=none&taskId=u55acd713-e6a4-4486-86fc-4f190bc8f98&title=&width=403.4545593261719)


![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656940920180-f9c7a9ce-a887-414a-8672-a75b37393289.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=327&id=ubc9eb08b&margin=%5Bobject%20Object%5D&name=image.png&originHeight=450&originWidth=760&originalType=binary&ratio=1&rotation=0&showTitle=false&size=75558&status=done&style=none&taskId=u0384c5d2-fed7-4cf6-8921-0bbdb85c841&title=&width=552.7272727272727)


使用浏览器

1. 在浏览器输入网址
1. 和网页中的元素交互
1. Javascript  ![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656941023004-a5561cc9-6dc8-4c64-ad47-17da9faa40aa.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=90&id=ua3028e67&margin=%5Bobject%20Object%5D&name=image.png&originHeight=124&originWidth=369&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12840&status=done&style=none&taskId=u8d17b72d-f8b8-4b9f-94e8-62ee5d4eb89&title=&width=268.3636363636364)


<a name="bDLky"></a>
#### URI和URL
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656941094218-a9b449f7-d3cf-482a-b13b-cdacda372eda.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=405&id=u3a5754bd&margin=%5Bobject%20Object%5D&name=image.png&originHeight=557&originWidth=834&originalType=binary&ratio=1&rotation=0&showTitle=false&size=134960&status=done&style=none&taskId=ubbb2049f-3cc2-4e63-86a3-44df6d4a773&title=&width=606.5454545454545)

一个简单的http的服务器
```cpp
#include <arpa/inet.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#include <iostream>
#include <memory>

class TcpConn {
public:
    TcpConn(const char *ip, const char *port)
        : _ip(ip), _port(port) {

    }

    int Start() {
        // socket
        _sockfd = socket(AF_INET, SOCK_STREAM, 0);
        struct sockaddr_in addr;
        addr.sin_family = AF_INET;
        addr.sin_addr.s_addr = inet_addr(_ip);
        addr.sin_port = htons(atoi(_port));
        // 端口复用
        int reuse = 1;
        setsockopt(_sockfd, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof(int));
        int ret = bind(_sockfd, (struct sockaddr *)&addr, sizeof(addr));
        listen(_sockfd, 10);

        return 0;
    }

    int RecvAndShow() {
        int netfd = accept(_sockfd, NULL, NULL);

        //更好的方式是使用RAII，将accept放入构造函数中，将close放入析构函数中
        std::unique_ptr<char[]> buf(new char[4096]);
        bzero(buf.get(), 4096);
        int ret = recv(netfd, buf.get(), 4096, 0);
        fprintf(stderr, "%s\n", buf.get());

        std::string firstLine = "HTTP/1.1 200 OK\r\n";
        send(netfd, firstLine.c_str(), firstLine.size(), 0);
        std::string type = "Content-Type:text/plain\r\n"
                            "Content-Length:5\r\n";
        send(netfd, type.c_str(), type.size(), 0);
        std::string emptyline = "\r\n";
        send(netfd, emptyline.c_str(), emptyline.size(), 0);
        std::string content = "hello";
        send(netfd, content.c_str(), content.size(), 0);

        close(netfd);
        fprintf(stderr, "closed\n");

        return 0;
    }

private:
    const char *_ip;
    const char *_port;
    int _sockfd;
};

int main() {
    TcpConn conn("0.0.0.0", "6789");
    conn.Start();
    while (1) {
        conn.RecvAndShow();
    }
}
```

客户端输入 `crul 192.168.4.28:6789`
```bash
hello
```
 

<a name="PdjbB"></a>
#### 客户端的选择

1. 浏览器
1. curl
1. postman

<a name="kUVYs"></a>
#### http请求报文的组成部分
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656941352016-a6215bed-22f8-4612-8c76-001bbd3cac94.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=203&id=u065a5f49&margin=%5Bobject%20Object%5D&name=image.png&originHeight=279&originWidth=604&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69749&status=done&style=none&taskId=u799249f7-943d-4bf1-b6fe-ed4b5f39b07&title=&width=439.27272727272725)

```bash
GET / HTTP/1.1
Host: 192.168.4.28:6789
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;
q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6

closed
```

<a name="brvUm"></a>
#### 方法   表明请求的行为 （大小写不敏感）
在HTTP请求当中，第一行的第一个字段就是请求的方法。 

- GET：用来获取资源； 
- HEAD：用来获取资源的首部字段（不获取响应体）； 
- POST：用来提交表单给对应的资源，这个请求通常来说会修改资源的状态（称为有副作用的）； 
- PUT：用请求的内容替换掉目标资源的内容； 
- DELETE：删除目标资源； 
- TRACE：用来做环回测试； 
- OPTIONS：描述目标资源的通信选项。 

一般情况下，GET、POST请求是最常使用的。 
> curl命令的用法可以参考curl 的用法指南 - [阮一峰的网络日志](https://www.ruanyifeng.com/blog/2019/09/curl-reference.html) ([ruanyifeng.com](https://www.ruanyifeng.com/blog/2019/09/curl-reference.html))  


<a name="houh3"></a>
#### get  读      post  写

POST  最为常见的请求体的形式有着两种： 

1. application/x-www-form-urlencoded   key1= value1 & key2 = value2
1. multipart/form-data ： 
   1. 指定一个boundary
   1. 把请求的元信息和内容放入若干个boundary之间 

<a name="g07YU"></a>
#### URI的路径和query部分 : 
uri总是以/开头， 默认/<br />query : 

- path  ： 服务端自定义，一般对应资源（文件 或者 服务）
- query  ： map<key, value>

http版本：<br />0.9   1.0   **1.1 **  2.0   3.0

<a name="en706"></a>
#### 首部字段
若干行    每行  name : value \r\n<br />通用首部字段<br />自定义首部字段

<a name="DJ0vb"></a>
#### host的效果：
让不同的域名可以对应到相同的 `ip : port`

keep-alive  长连接  /   closed 短连接


> 面试常问的一个坑：`<html>` 应该在http报文体(body)中


<a name="p49gg"></a>
#### 响应报文
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1656941993688-4cd8ec63-a6c2-43dc-8bae-f8aeb6eb2037.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=204&id=ub031d5f4&margin=%5Bobject%20Object%5D&name=image.png&originHeight=281&originWidth=622&originalType=binary&ratio=1&rotation=0&showTitle=false&size=65746&status=done&style=none&taskId=u238d99eb-75dc-4c24-b30f-d7392d8023e&title=&width=452.3636363636364)

- 在报文体中传递参数
- 在响应报文体中返回结果     

用json/xml传递关键信息


<a name="Yv1zp"></a>
#### 状态码和原因字符串
HTTP 响应状态码用来表明特定 [HTTP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP) 请求是否成功完成。 响应被归为以下五大类：

1. [信息响应](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status#%E4%BF%A1%E6%81%AF%E5%93%8D%E5%BA%94) (100–199)
1. [成功响应](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status#%E6%88%90%E5%8A%9F%E5%93%8D%E5%BA%94) (200–299)
1. [重定向消息](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status#%E9%87%8D%E5%AE%9A%E5%90%91%E6%B6%88%E6%81%AF) (300–399)
1. [客户端错误响应](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status#%E5%AE%A2%E6%88%B7%E7%AB%AF%E9%94%99%E8%AF%AF%E5%93%8D%E5%BA%94) (400–499)
1. [服务端错误响应](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%94%99%E8%AF%AF%E5%93%8D%E5%BA%94) (500–599)

200    成功<br />301 302   + location   重定向<br />400  客户端错误<br />500  服务端错误/网络拥堵


<a name="AwxkH"></a>
#### RESTful    把视图和关键状态分离
REST(表示状态转换 Representational state transfer)

1. 行为一般分为： 
- 增 post
- 删 delete
- 查 get
- 改 put
2. 使用url的path定位资源
2. 将参数放入请求体  （ json / xml 组织 ）
2. 得到的响应只有关键数据的集合， json / xml 组织， 不是html文档

<a name="NlENi"></a>
#### 幂等性   ( 多次重复结果不变 )

- 加法   不幂等
- 并集   幂等  （ 唯一id    set  ）

幂等： get   delete   put    可以充分利用缓存<br />不幂等 :  post 

全局唯一id的实现方法（面试问题）

- redis的唯一索引
- 雪花算法 

可以查询相关技术网站

<a name="RL8bD"></a>
#### https
http   明文传递  不安全的 <br />http  + ssl  ( secure socket  leyer  ->  TLS )  加密


<a name="zTP9u"></a>
#### 对称加密  和 非对称加密
对称加密 ：AES/DES   效率较高<br />非对称加密 : RSA

利用加密手段生成https<br />握手阶段 ： 第一次非对称 传输 **密钥**<br />传输阶段  ：  用该**密钥** 对称加密（ 效率高 ）

当前生成密钥的算法：<br />两边各自生成自己的私钥和公钥 ，A给予B公钥，B给予A私钥，可以通过算法使A和B生成一个完全相同的密钥。



<a name="dSL8v"></a>
## day03
分布式数据库     C++黄金方向

如何解决粘包问题？（面试常问）

1. 每次固定长度
1. 每次先读取长度，再根据此次长度 读取对应长度的内容
1. 设定标志字符（在正文中一定不会出现），读到此符号即终止

<a name="wvRbS"></a>
#### C++四个方向  （ 10：06 ）
网络    Nginx  、 Gataway<br />~~消息   消息队列 （Java）~~<br />缓存   数据库  、redis<br />存储   分布式


<a name="gXdGw"></a>
#### Nginx
C语言写的轻量级http服务端   ( -d  daemon 守护进程 )<br />多进程 + 事件驱动


Apache   

- 出现的早 
- Linux 服务器的占比增加

 基于进程/线程     上限千条连接    c10k（单核  2000QPS  每秒2000查询）<br />Nginx   事务驱动  每个连接占用的内存小 -->  高并发<br />使用select/epoll  `I/O`多路复用 去管理时间调度    单核10万QPS

dpdk   单机千万       mmap映射到用户态，由用户态处理

AB  /  wrk    压力测试


<a name="zjCKH"></a>
#### Nginx的使用
```bash
$ curl -i www.jd.com
HTTP/1.1 302 Moved Temporarily
Server: nginx
Date: Tue, 05 Jul 2022 12:21:28 GMT
Content-Type: text/html
Content-Length: 138
Connection: keep-alive
Location: https://www.jd.com/
Timing-Allow-Origin: *
X-Trace: 302-1657023688857-0-0-0-0-0
Strict-Transport-Security: max-age=3600
```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657023329306-9d0294ee-5feb-44d8-b2db-644eaa4df6e4.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=220&id=cOaVB&margin=%5Bobject%20Object%5D&name=image.png&originHeight=303&originWidth=654&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32271&status=done&style=none&taskId=uca612091-b6e5-4595-84ee-2d77a05e6a6&title=&width=475.6363636363636)<br />Nginx  企业服务端的边缘节点

<a name="At4X0"></a>
#### Nginx的一般功能
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657023892272-1cf4a8c2-6d5c-4c42-a66d-7a7dd8bc411c.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=348&id=sflKf&margin=%5Bobject%20Object%5D&name=image.png&originHeight=478&originWidth=659&originalType=binary&ratio=1&rotation=0&showTitle=false&size=73209&status=done&style=none&taskId=u91cae65f-dac2-4ef0-a89f-413f961e537&title=&width=479.27272727272725)

API网关    Kong / Apisix      基于 openresty 

Nginx的优点

- 高并发 、高性能    架构优秀
- 可拓展性好  模块化    （事件驱动  核心模块）
- 可靠性好    “三年不重启”   5~6 个 9  （99.9999 %）
- 热部署   运行时更换配置


<a name="Txdcq"></a>
#### Nginx的安装和使用

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657024642022-09239689-94e1-4a27-81f4-12193cdacbea.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=284&id=u9f56dd0a&margin=%5Bobject%20Object%5D&name=image.png&originHeight=391&originWidth=653&originalType=binary&ratio=1&rotation=0&showTitle=false&size=120648&status=done&style=none&taskId=ue25cfa5b-3ca7-46bc-b1a9-6566891f1f7&title=&width=474.90909090909093)

Nginx的安装有很多种方法，我们这里选择的是从源码安装Nginx。 <br />首先，需要先安装依赖的3个动态库。可以选择从源代码安装，也可以从包管理器中下载安装：  
```bash
sudo apt install libz-dev #安装zlib库 处理压缩的事宜
sudo apt install libpcre3-dev #安装pcre库 处理正则表达式
sudo apt install libssl-dev #安装openssl库 处理SSL连接

curl -O https://nginx.org/download/nginx-1.20.1.tar.gz
tar xvfz nginx-1.20.1.tar.gz

# cd到源代码目录
./configure # 生成makefile文件
make # 编译
sudo make install # 将生成的文件移动到系统的合适目录下
```
 采用这种最简单的方式安装Nginx之后会只安装了最基本的模块，如果需要安装其他模块，则需要重新 配置和install。默认情况下，Nginx的默认目录是`/usr/local/nginx/`，可执行程序 是 `/usr/local/nginx/sbin/nginx`，配置文件是 `/usr/local/nginx/conf/nginx.conf`。  

 下面是一些相关的命令，注意应当使用特权用户启动nginx：  
```bash
/usr/local/nginx/sbin/nginx # 默认方式启动
# 参数：
# -h 查看帮助
# -c x.conf 指定配置文件x.conf启动
# -p /opt/nginx 指定工作目录是/opt/nginx
# -s stop 强制停止nginx
# -s quit 优雅停止nginx（等待当前任务结束）
# -s reload 重启nginx
# -s reopen 重新打开日志文件
## 如果启动Nginx的时候使用了-c/-p，那么使用-s的时候也必须加上
# -t 检查默认配置文件
# -T 检查默认配置文件并输出
# -t -c x.conf 检查x.conf
# -v/-V 显示版本信息
```

`sbin/nginx -v`   显示版本<br />`sbin/nginx -V`  显示版本和编译信息

`sbin/nginx -s`  给master进程发送信号<br /> <br />`sbin/nginx -c` 指定配置文件xxx.conf启动

`sbin/nginx -t`  检查配置文件的语法错误<br />`sbin/nginx -T`  检查默认配置文件并输出

将 contribute/vim文件夹中的全部文件  cp到 ~/.vim/ 中，即可让Nginx的配置文件也有高亮。

<a name="H1Hpv"></a>
#### 安装好的目录
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657024756954-b99bb491-93b6-4157-a2e2-005d61253ed6.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=289&id=u284b3eac&margin=%5Bobject%20Object%5D&name=image.png&originHeight=398&originWidth=627&originalType=binary&ratio=1&rotation=0&showTitle=false&size=123752&status=done&style=none&taskId=u2e93a5b9-2db7-47e6-b3df-14b86dfc1ad&title=&width=456)

实例 静态资源服务器<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657024834344-c0ccbecd-7fac-4ff0-81e1-f9c065125957.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=315&id=uaa0cfb3b&margin=%5Bobject%20Object%5D&name=image.png&originHeight=433&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=89724&status=done&style=none&taskId=u28eb4589-f41d-41d6-90d4-8286196d0a5&title=&width=422.54545454545456)

可以多个域名部署在同一台服务器
```nginx
worker_processes  1;
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  logs/access01.log  main; #main是日志的名字
    sendfile        on;
    keepalive_timeout  65;
    server {
        listen       80;
        server_name  test0.abc;
        location / {
            return 200 "hello";
        }
    }
    server {
        listen       80;
        server_name test1.abc;
        location / {
            return 200 "world";
        }
    }
}
```


configure
```nginx
 # 指令 参数
# 指定worker进程的数量
worker_processes 1;

events {
    # events 上下文  { ... } 指令块
    worker_connections 1024;
}
http {
    # mime 文件类型映射文件
    include mime.types;
    #不知道什么文件，浏览器会下载下来
    default_type application/octet-stream; 
    sendfile on;
    keepalive_timeout 65;
    server {
        # 虚拟服务端
        listen 80;
        server_name localhost;
        location / {
            # 用来匹配uri的path部分，默认是前缀匹配 /
            # /usr/local/nginx/    html/   index.html
            root html; 
            index index.html index.htm;
        }
        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
            # /usr/local/nginx/html/50x.html
            root html;
        }
    }
}

```

<a name="ZpFM8"></a>
#### 配置文件的特点 :

1. 配置文件 = 指令 ( 指令名 参数; )+ 指令块 ( 指令块名 参数{ }; )
1. `#`单行注释
1. include 包含另一个文件
1. `$` 引用变量
1. 支持正则表达式

<a name="HTblY"></a>
#### Nginx的日志系统
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657025055294-b12dd19c-8120-4085-bfe2-a8d6246896f2.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=281&id=uba51b8e2&margin=%5Bobject%20Object%5D&name=image.png&originHeight=386&originWidth=698&originalType=binary&ratio=1&rotation=0&showTitle=false&size=93557&status=done&style=none&taskId=ua39a6c26-4fae-49c8-a36f-a89626f3eb1&title=&width=507.6363636363636)

<a name="FkPf6"></a>
### Nginx 4个重要的模块
http模块     提高网络服务，在最外层<br />server模块   -->  **虚拟服务端**<br />location模块   -->   根据uri匹配配置功能<br />upstream模块 -->  支持反向代理


域名解析成IP地址 ：

1. 查缓存
1. 检查本地的hosts文件
```bash
$cat /etc/hosts
```

3. 查询DNS服务

`nslookup`  

<a name="IMwAU"></a>
#### 如何处理网络问题  （ 面试常问 ）

1. netstat      （ 涉及到知识点 :  TCP 11个状态  ）
1. tcpdump  -w  filename.cap    再用wireshark查看filename.cap文件
```bash
netstat  -a   // all
netstat  -t   // tcp协议
```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657025210702-d4263ce7-f190-49d8-95b4-eab55d907231.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=324&id=u1f344c1b&margin=%5Bobject%20Object%5D&name=image.png&originHeight=445&originWidth=548&originalType=binary&ratio=1&rotation=0&showTitle=false&size=99050&status=done&style=none&taskId=ucbb26f7d-d746-40f6-89fc-994df2f5d2e&title=&width=398.54545454545456)

<a name="tBXsG"></a>
#### location模块
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657025267178-9f2b2434-3655-4b25-b714-827128dada96.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=250&id=uac90aa3f&margin=%5Bobject%20Object%5D&name=image.png&originHeight=254&originWidth=344&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33737&status=done&style=none&taskId=u0dfe051e-9547-4535-9f90-ae3033033cf&title=&width=339.18182373046875)

```nginx
worker_processes  1;
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  logs/access01.log  main; #main是日志的名字
    sendfile        on;
    keepalive_timeout  65;
    server {
        listen       80;
        server_name  test0.abc;
        location / {
            return 200 "hello\n";
        }
        location = /abc {
            return 200 "abc\n";
        }
        location ~ /(.*)test {
            return 200 "test\n";
        }
        location ~* /(.*)star{
            return 200 "star\n";
        }
        location ^~ /123{
            return 200 "123\n";
        }
    }
}
```

指定一个匹配规则，让不同path的请求对应到不同的location指令块中 。
```nginx
location [ = | ~ | ~* | ^~ ] uri { ... }
#location使用配置文件当中的uri参数去匹配请求的uri的路径部分(路径部分包括开头的/)
#uri参数建议用单引号括起来，避免参数中的符号和配置文件本身的语法冲突
#如果第一个符号参数为空，则默认是前缀匹配
#如果第一个符号参数是^~,也是前缀匹配
#如果第一个符号参数是=，则表示完全匹配
#如果第一个符号参数是～，大小写敏感正则匹配
#如果第一个符号参数是～*，大小写不敏感正则匹配
```

1. 找到所有前缀匹配项缓存中最长的一个
1. 按在配置文件中出现的顺序找到**第一个**正则匹配项
1. 再找完全匹配项

完全匹配项若存在，则使用完全匹配项<br />完全和正则皆不存在，则使用前缀匹配<br />完全不存在，正则（找 先出现）存在，如果 1. ^~   前缀  2. 空 正则 

<a name="yLINU"></a>
#### location匹配的优先级
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657025316980-fef84f84-e5c4-4c7b-a596-39dcf11a6a44.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=310&id=u13b303f0&margin=%5Bobject%20Object%5D&name=image.png&originHeight=330&originWidth=283&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33193&status=done&style=none&taskId=u925c458f-9db2-4b33-abe0-38940642c16&title=&width=265.8181915283203)

```nginx
worker_processes  1;
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  logs/access01.log  main; #main是日志的名字
    sendfile        on;
    keepalive_timeout  65;
    server {
        listen       80;
        server_name  test0.abc;
        location / {
            return 200 "/\n";
        }
        location  /1 {
            return 200 "/1\n";
        }
        location ~ /([0-9]*) {
            return 200 "/$1\n";
        }
        location ~ /([0-9]*)([a-z]*) {
            return 200 "/$1--$2\n";
        }
    }
}
```

<a name="I0osF"></a>
#### 作业
使用Nginx搭建静态服务器<br />file 配置块    uri --> 本地文件系统的路径

root  将location后的路径拼接上root的路径，必须在本地存在，暴露本地路径<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657025362153-75a6759e-9220-477a-89ed-ce4c5626192a.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=257&id=u09c0a556&margin=%5Bobject%20Object%5D&name=image.png&originHeight=354&originWidth=603&originalType=binary&ratio=1&rotation=0&showTitle=false&size=68952&status=done&style=none&taskId=ub194609d-212c-4346-ae33-e4740307198&title=&width=438.54545454545456)

alias  将location后的路径替换为 alias指定的本地路径<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657025394150-6db4e234-8360-4273-b051-d4ff1ba30c99.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=284&id=u0cbf50ed&margin=%5Bobject%20Object%5D&name=image.png&originHeight=391&originWidth=663&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69630&status=done&style=none&taskId=u727fe80d-69b4-4d67-9e70-2661c014b4c&title=&width=482.1818181818182)

index 当url的path以/结尾时（是个目录），自动转向index指向的文件<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657025406228-79054c78-3a51-41ae-afd0-2f4662154f25.png#clientId=ue9602e91-0e3e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=211&id=u6db58200&margin=%5Bobject%20Object%5D&name=image.png&originHeight=276&originWidth=418&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22821&status=done&style=none&taskId=uacc3d992-c937-4826-8de3-8e988285998&title=&width=319)

```nginx
worker_processes  1;
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
        '$status $body_bytes_sent "$http_referer" '
        '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  logs/access01.log  main; #main是日志的名字
        sendfile        on;
    keepalive_timeout  65;
    server {
        listen       80;
        server_name  test0.abc;
        #location /test/ {
        #    root test/; 
        # 192.168.135.132/test/1.txt -> /usr/local/nginx/test/test/1.txt
        #}
        location /test/ {
            alias test/;
            autoindex on; # 自动生成相关联的 index页面
        # 192.168.135.132/test/1.txt -> /usr/local/nginx/test/1.txt
        }
        location /ref/{
            alias reference/;
            index en/index.html;
        }
    }
}
```


<a name="nrxOh"></a>
### day04
进程    2倍核心数 <br />QPS  和最大连接数 没关系   （ 1s  对 计算机来说很长 ）<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657105475133-b59e0b32-cc68-46ff-866f-bbcd68bed4ae.png#clientId=ub3f42f7e-6195-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=369&id=u180d1337&margin=%5Bobject%20Object%5D&name=image.png&originHeight=508&originWidth=678&originalType=binary&ratio=1&rotation=0&showTitle=false&size=60762&status=done&style=none&taskId=u11143386-0c17-4efc-8b53-6bfe6cee560&title=&width=493.09090909090907)

<a name="DrMXF"></a>
#### 启用压缩的指令
压缩和解压缩 需要CPU计算资源 <br />`I/O`密集型可以高压缩， 计算密集型 需要 低压缩或不压缩

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657105535705-e1a3eb22-0ff0-47a6-b89f-f125c2a23b93.png#clientId=ub3f42f7e-6195-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=324&id=u4036972b&margin=%5Bobject%20Object%5D&name=image.png&originHeight=445&originWidth=669&originalType=binary&ratio=1&rotation=0&showTitle=false&size=113706&status=done&style=none&taskId=u4abfcd84-010c-4a39-b25d-3a8acb43b03&title=&width=486.54545454545456)

<a name="cavBs"></a>
#### 变量
`$uri`  uri的路径<br />`$args` query的参数


引入第三方模块

1. 下载模块源代码到本地
1. 修改nginx的makefile
```nginx
./configure --add-dynamic-module=/home/user/echo-nginx-module
```

3. make modules
3. <br />
```nginx
cp objs/ngx_http_echo_module.so /usr/local/nginx/modules
```


使用第三方模块
```nginx
load_module modules/ngx_http_echo_module.so;

location /test1/ {
    echo 'test1';
}
```

<a name="cRSkY"></a>
#### 反向代理
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657106978489-740c44d0-56f1-4c4a-8d3c-f96d2d63f974.png#clientId=ub3f42f7e-6195-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=194&id=u4631afec&margin=%5Bobject%20Object%5D&name=image.png&originHeight=267&originWidth=438&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21791&status=done&style=none&taskId=u531add2c-6b49-4498-b99b-9b9a190ffd9&title=&width=318.54545454545456)<br />10：18-10:24  代理

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657106967461-d4bd1f17-9b55-48c0-b358-de5c32f12bc4.png#clientId=ub3f42f7e-6195-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=316&id=u786e4184&margin=%5Bobject%20Object%5D&name=image.png&originHeight=435&originWidth=615&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46610&status=done&style=none&taskId=ub261293f-20da-43cd-a5d3-997a914427f&title=&width=447.27272727272725)<br />LAMP ： Linux  、 Apache  、 MySQL  、 PHP<br />LNMP

方向代理 proxy  business  关闭错误<br />此时，不同同时启动两个nginx的原因，默认的pid_file文件只有一个，记录了一个nginx进程的pid，退出时发信号给此pid。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657106997091-4bcc2dc1-4179-4dce-9acd-55a325305363.png#clientId=ub3f42f7e-6195-4&crop=0&crop=0&crop=0.9007&crop=1&from=paste&height=160&id=pYd8y&margin=%5Bobject%20Object%5D&name=image.png&originHeight=230&originWidth=471&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33294&status=done&style=none&taskId=u6cc3fc91-7e95-41c8-bfcb-9b0e49270a8&title=&width=327)

config 文件  设置  记录此进程pid的文件
```nginx
pid logs/5_business.pid;
```


不同nginx进程的access.logs **最好**分开保存
```nginx
access_log logs/access05.log main;
```


<a name="hQDd5"></a>
#### 配置反向代理
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657107079404-0f086bd8-c83b-4fc5-aae8-983cff53cf78.png#clientId=ub3f42f7e-6195-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=253&id=u775cca0c&margin=%5Bobject%20Object%5D&name=image.png&originHeight=348&originWidth=580&originalType=binary&ratio=1&rotation=0&showTitle=false&size=64772&status=done&style=none&taskId=ua1456921-78bd-4730-aeb5-ec4965fabfb&title=&width=421.8181818181818)

```nginx
#configure

upstream backend {
    server 私网ip:port
}

server {
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    
    proxy_pass http://localhost/;  # nginx 会替换
}
```


<a name="uxbZl"></a>
#### 设置缓存的指令
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657107125651-82319bb5-aa4c-43a1-8ec5-534c42245337.png#clientId=ub3f42f7e-6195-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=225&id=u48a1dccd&margin=%5Bobject%20Object%5D&name=image.png&originHeight=309&originWidth=666&originalType=binary&ratio=1&rotation=0&showTitle=false&size=62403&status=done&style=none&taskId=udaeafba4-e03b-424c-b279-09ddaddcf69&title=&width=484.3636363636364)

```nginx
#configure

upstream backend {
    server 私网ip:port
}

proxy_cache_path /tmp/myCache level=1:2 keys_zone=my_cache:10m max_size=10g interactive=60m use_temp_path=off;g

server {
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    
    proxy_cache my_cache;
    proxy_cache_key $host$uri$is_args$args;
    proxy_cache_valid 200 304 302 1d;
        
    proxy_pass http://localhost/;  # nginx 会替换
}
```


<a name="NleCq"></a>
### day05
复习：<br />模块<br />反向代理：

- 业务服务器  普通的http
- 反向代理 
   1. http服务端
   1. 转发到哪里  	         upstream  上游/后端
   1. 什么样会被转发     location --> proxy_pass


<a name="kjr13"></a>
#### 反向代理     负载均衡（加权轮询）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657203736914-2612d9ae-56fb-44d7-b091-2bb42e8c75db.png#clientId=u088d4830-492d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=381&id=u539b7f6d&margin=%5Bobject%20Object%5D&name=image.png&originHeight=524&originWidth=726&originalType=binary&ratio=1&rotation=0&showTitle=false&size=95307&status=done&style=none&taskId=uaf27d458-268c-4d17-afd4-b63c44aaae2&title=&width=528)

<a name="tJILM"></a>
#### 缓存   ( 目标服务器可以设置缓存 )
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657203757569-89eb6504-210a-42c4-88d6-8eddc1694ced.png#clientId=u088d4830-492d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=343&id=u194af6de&margin=%5Bobject%20Object%5D&name=image.png&originHeight=471&originWidth=754&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63188&status=done&style=none&taskId=u435190b6-067e-41eb-aa0a-1e3f9a33b77&title=&width=548.3636363636364)<br />CDN(Content Delivery Network)   内容分发网络（内容传送网络）


<a name="mR5o7"></a>
#### 直接hash策略
如果某个服务器宕机，对其他服务器的业务有影响（ 原来的处理顺序会被打乱 ）
```nginx
upstream{
    ip hash;
}
```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657203772632-d7703b3c-9955-4ec5-ad1b-cc54aba48b53.png#clientId=u088d4830-492d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=139&id=ua61752a5&margin=%5Bobject%20Object%5D&name=image.png&originHeight=191&originWidth=503&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22919&status=done&style=none&taskId=u7c059091-bdfd-441f-9acb-3224b8d9c3c&title=&width=365.8181818181818)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657203795105-8720d6c0-13fc-451d-b1b9-4072119996d5.png#clientId=u088d4830-492d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=283&id=u94122c16&margin=%5Bobject%20Object%5D&name=image.png&originHeight=389&originWidth=708&originalType=binary&ratio=1&rotation=0&showTitle=false&size=48746&status=done&style=none&taskId=u1ede9632-739d-4172-80be-7ed9732e8ef&title=&width=514.9090909090909)

<a name="zfYUV"></a>
#### 一致性hash策略
```nginx
upstream{
    hash key [];
}
```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657203810234-680dcaae-d335-4c6f-9e68-410cc902b919.png#clientId=u088d4830-492d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=311&id=u9f24c2bb&margin=%5Bobject%20Object%5D&name=image.png&originHeight=427&originWidth=603&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53076&status=done&style=none&taskId=u7df2271f-8211-4d57-89ef-4652109467c&title=&width=438.54545454545456)


<a name="sWfVg"></a>
### Nginx的架构设计
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657203832805-e42cd66d-f832-416a-ad7b-f873af3f4c2e.png#clientId=u088d4830-492d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=258&id=u38c0a30e&margin=%5Bobject%20Object%5D&name=image.png&originHeight=355&originWidth=634&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39361&status=done&style=none&taskId=u36e2b7d1-e42e-4190-a1d1-343c117d71e&title=&width=461.09090909090907)


accept惊群  Linux2.6以后 维护一个等待队列，取第一个就绪

epoll惊群   

- reusepoll   
- Linux5.4 以后，同样维护一个队列。








