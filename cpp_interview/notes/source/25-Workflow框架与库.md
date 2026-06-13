常见的框架和库

TCP   : <br />reactor   -->  muduo  （ 事件驱动 ）<br />proactor  -->  boost : : asio

http  :<br />libhv ( reactor ）<br />异步框架  workflow<br />协程框架  brpc

高性能服务器 三种方法： 1. 事件驱动   2. 异步   3. 协程( 等价于 事件驱动  但是使用简单 )

```cpp
// httpServer.cc
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


<a name="ICvRx"></a>
### 安装和配置workflow
[https://gitee.com/yangxf98/workflow-netdisk](https://gitee.com/yangxf98/workflow-netdisk)

1. 安装源码
1. 安装依赖 cmake
1. 生成makefile文件  
```bash
make  
sudo make install
sudo ldconfig
```
在链接时加上 `-lworkflow` 

<a name="o0PIo"></a>
#### C++ 服务端框架

异步   连接池

1. 客户端 ： http  、 redis  、MySQL
1. 服务端 ： http    ( 很容易实现新功能 )
1. 基于workflow可以构建分布式应用    ( rpc  -->  srpc )

<a name="bflx3"></a>
#### workflow是异步框架
抽象机制 ：  “ 任务 ” 一段将要异步执行的代码<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657199050351-2c062719-5fa9-45c2-859f-a5a3e78efbe4.png#clientId=ua343532e-298f-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=433&id=ua680ad9a&margin=%5Bobject%20Object%5D&name=image.png&originHeight=595&originWidth=909&originalType=binary&ratio=1&rotation=0&showTitle=false&size=96870&status=done&style=none&taskId=uee93e7e4-9aee-4e18-bfaa-d9e246b62a5&title=&width=661.0909090909091)<br />机制 ： 异步 + 回调

<a name="bYUh2"></a>
#### 任务的 “ 串并联 ”
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657199070308-2cfcd4f8-3ffa-459e-8009-092fd0c59dbb.png#clientId=ua343532e-298f-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=460&id=ue644ed4e&margin=%5Bobject%20Object%5D&name=image.png&originHeight=632&originWidth=1023&originalType=binary&ratio=1&rotation=0&showTitle=false&size=79902&status=done&style=none&taskId=u8d0e2117-cbae-417a-a0ab-e767e45de5b&title=&width=744)<br />workflow 提供了将任务串联（先后）和并联（并发）


基本代码：** 阻塞主线程**
```cpp
#include <signal.h>
#include <workflow/WFFacilities.h>

static WFFacilities::WaitGroup waitgroup(1);

void singHander(int num) {
    waitgroup.done();
    fprintf(stderr, "wait group is done");
}

int main() {
    // 注册 Ctrl + C 信号
    signal(SIGINT, singHander);

    // 阻塞主线程
    // wait方法当存在至少一个任务未完成时，线程阻塞。
    waitgroup.wait();

    return 0;
}
```


<a name="EGjZW"></a>
### 1. 任务
<a name="ZhRcr"></a>
### http任务：

1. 创建任务  ： 工厂模式
```cpp
class WFTaskFactory
{
public:
	static WFHttpTask *create_http_task(const std::string& url,
										int redirect_max,
										int retry_max,
										http_callback_t callback);
    
http_callback_t callback    /* 回调函数 */
```

2. 设置任务属性
2. 启动任务

异步执行，先执行基本工作，再执行回调函数

请求报文对象和响应报文对象
```cpp
// WFTask.h
template<class REQ, class RESP>
class WFNetworkTask : public CommRequest
{
public:


// WFTaskFactory.h
using WFHttpTask = WFNetworkTask<protocol::HttpRequest,
								 protocol::HttpResponse>;
                                 
// WFTask.h                                
public:
	REQ *get_req() { return &this->req; }
	RESP *get_resp() { return &this->resp; }
```

<a name="iHu0w"></a>
#### 在回调函数中获取任务的状态
```cpp
// WFTaskFactory.h
using http_callback_t = std::function<void (WFHttpTask *)>;

http_callback_t callback;


// WFTask.h
public:
	int get_state() const { return this->state; }
	int get_error() const { return this->error; }
```

<a name="LcLiO"></a>
#### 遍历所有首部字段的迭代器
```cpp
// HttpUtil.h
class HttpHeaderCursor
{
public:
	HttpHeaderCursor(const HttpMessage *message);
	virtual ~HttpHeaderCursor();

public:
    
    // 找到下一对首部字段键值对
    // 若全部解析完成，就会返回 false
	bool next(std::string& name, std::string& value);
	
    // find 会根据首部字段的键，找到对应的值
    // 注意: find 方法会修改迭代器的位置。
    bool find(const std::string& name, std::string& value);
```


```cpp
// httpTask.cc
#include <signal.h>
#include <workflow/HttpMessage.h>
#include <workflow/HttpUtil.h>
#include <workflow/WFFacilities.h>

#include <string>

static WFFacilities::WaitGroup waitgroup(1);

void signHandler(int num) {
    waitgroup.done();
    fprintf(stderr, "wait group is done\n");
}

void callback(WFHttpTask *httpTask) {
    // 在回调函数中可以获取任务的所有信息
    protocol::HttpRequest *req = httpTask->get_req();
    protocol::HttpResponse *resp = httpTask->get_resp();
    int state = httpTask->get_state();
    int error = httpTask->get_error();
    switch (state) {
        case WFT_STATE_SYS_ERROR:
            fprintf(stderr, "system error: %s\n", strerror(error));
            break;

        case WFT_STATE_DNS_ERROR:
            fprintf(stderr, "dns error: %s\n", gai_strerror(error));
            break;

        case WFT_STATE_SUCCESS:
            break;
    }

    if (state != WFT_STATE_SUCCESS) {
        fprintf(stderr, "Failed! \n");
        return;
    } else {
        fprintf(stderr, "Success! \n");
    }

    /*  GET / HTTP/1.1  */
    fprintf(stderr, "request\r\n %s %s %s \r\n",
            req->get_method(),
            req->get_request_uri(),
            req->get_http_version());

    // 使用迭代器模式遍历首部字段
    std::string name;
    std::string value;
    protocol::HttpHeaderCursor reqCursor(req);

    /*
    Host:192.168.4.28:6789
    Accept: * *
    User-Agent:myHttpTask
    Connection:close
    */
    while (reqCursor.next(name, value)) {
        fprintf(stderr, "%s:%s\r\n", name.c_str(), value.c_str());
    }
    fprintf(stderr, "\r\n");

    /*
    response
    HTTP/1.1 200 OK
    */
    fprintf(stderr, "response\r\n %s %s %s\r\n",
            resp->get_http_version(),
            resp->get_status_code(),
            resp->get_reason_phrase());

    protocol::HttpHeaderCursor respCursor(resp);

    /*
    Content-Type:text/plain
    Content-Length:5
    */
    while (respCursor.next(name, value)) {
        fprintf(stderr, "%s:%s\r\n", name.c_str(), value.c_str());
    }

    // print reponse body
    const void *body;
    size_t size;
    // 传入传出参数  底层的cosnt
    // get_parsed_body方法会修改 指针变量body的指向,指向报文体
    resp->get_parsed_body(&body, &size);
    // fwrite(body, 1, size, stderr);
    fprintf(stderr, "%s", (const char *)body);
}

// 异步 + 回调
int main() {
    signal(SIGINT, signHandler);

    WFHttpTask *httpTask = WFTaskFactory::create_http_task("http://192.168.4.28:6789", 0, 0, callback);
    protocol::HttpRequest *req = httpTask->get_req();
    req->add_header_pair("Accept", "*/*");
    req->add_header_pair("User-Agent", "myHttpTask");
    req->add_header_pair("Connection", "close");

    httpTask->start();

    waitgroup.wait();

    return 0;
}
```



<a name="YmUoM"></a>
### redis任务
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657200490324-641293d8-5279-4c9b-a84b-4c28e79043ba.png#clientId=ua343532e-298f-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=364&id=u0e4999ec&margin=%5Bobject%20Object%5D&name=image.png&originHeight=501&originWidth=668&originalType=binary&ratio=1&rotation=0&showTitle=false&size=68184&status=done&style=none&taskId=ua052ffec-7ec5-420c-9446-bac80bb2613&title=&width=485.8181818181818)


<a name="nscBV"></a>
#### lambda表达式
匿名函数对象
```cpp
[ 携带的属性 ] ( 参数列表 )  { 函数体 }
携带的属性 -> 对应类的普通成员 /* 值传递  捕获 */
```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657200510951-14c10339-f687-4bbd-8400-c93931c877f7.png#clientId=ua343532e-298f-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=268&id=ud5651eca&margin=%5Bobject%20Object%5D&name=image.png&originHeight=368&originWidth=679&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46913&status=done&style=none&taskId=ub1e140a4-94f4-467b-9d54-86acb4eb0f7&title=&width=493.8181818181818)

```cpp
// redisTask.cc
#include <signal.h>
#include <workflow/WFFacilities.h>

static WFFacilities::WaitGroup waitgroup(1);

void callback() {}

void signHandler(int num) {
    waitgroup.done();
    fprintf(stderr, "wait group is done\n");
}

int main() {
    signal(SIGINT, signHandler);

    WFRedisTask* redisTask = WFTaskFactory::create_redis_task("redis://127.0.0.1:6379", 0, [](WFRedisTask* redisTask) {
        protocol::RedisRequest* req = redisTask->get_req();
        protocol::RedisResponse* resp = redisTask->get_resp();
        int state = redisTask->get_state();
        int error = redisTask->get_error();
        // 专门 存储redis任务的结果
        protocol::RedisValue value;

        switch (state) {
            case WFT_STATE_SYS_ERROR:
                fprintf(stderr, "system error: %s\n", strerror(error));
                break;

            case WFT_STATE_DNS_ERROR:
                fprintf(stderr, "dns error: %s\n", gai_strerror(error));
                break;
            // 如果redis语法有问题 , 会进入 SUCESS
            case WFT_STATE_SUCCESS:
                resp->get_result(value);
                if (value.is_error()) {
                    fprintf(stderr, "redis syntax error\n");
                    state = WFT_STATE_TASK_ERROR;
                }
                break;
        }

        if (state != WFT_STATE_SUCCESS) {
            fprintf(stderr, "redis Failed !\n");
            state = WFT_STATE_TASK_ERROR;
        }

        std::string cmd;
        req->get_command(cmd);
        fprintf(stderr, "redis request, cmd = %s\n", cmd.c_str());
        if (value.is_string()) {
            fprintf(stderr, "value is a string , value = %s\n", value.string_value().c_str());

        } else if (value.is_array()) {
            fprintf(stderr, "value is string array \n");
            for (size_t i = 0; i < value.arr_size(); ++i) {
                fprintf(stderr, "value at %lu = %s", i, value.arr_at(i).string_value().c_str());
            }
        }
    });
    
    protocol::RedisRequest* req = redisTask->get_req();
    // string   vector<string>
    // req->set_request("SET", {"43key","100"});
    req->set_request("HGETALL", {"43t"});

    // 启动redis任务
    redisTask->start();

    waitgroup.wait();

    return 0;
}
```

<a name="a6nUT"></a>
### 2. 序列 （串行任务 )   serieswork类
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657200530665-6c560171-73f2-4509-accf-ba2c52dfe7bb.png#clientId=ua343532e-298f-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=397&id=uec1bf43a&margin=%5Bobject%20Object%5D&name=image.png&originHeight=546&originWidth=750&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53319&status=done&style=none&taskId=u634ceb9d-269b-4027-8a9f-04ed39335ff&title=&width=545.4545454545455)


创建序列 : `task -> start()`
```cpp
void start(){  
    // 只有客户端才可以调用start方法。
    // start方法的底层逻辑就是根据本任务对象创建一个序列
    // 其中本任务是序列当中的第一个任务，随后启动该任务。
    assert(!series_of(this));
	Workflow::start_series_work(this, nullptr);
}
```
series_of 找到一个执行中的任务所在的序列。

1、 只有客户端才可以调用start方法。<br />2、 start方法的底层逻辑就是根据本任务对象创建一个序列<br />3、其中本任务是序列当中的第一个任务，随后启动该任务。

```cpp
// workflow.h
class SeriesWork
{
public:
	void start()
	{
		assert(!this->in_parallel);
		this->first->dispatch();
	}
    

public:
	void push_back(SubTask *task);
	// void push_front(SubTask *task); /*插入当前任务的后一个*/

public:
	void *get_context() const { return this->context; }
	void set_context(void *context) { this->context = context; }
    
public:
	void set_callback(series_callback_t callback)
	{
		this->callback = std::move(callback);
	}
```


```cpp
// series.cc
#include <signal.h>
#include <unistd.h> /* sleep() */
#include <workflow/WFFacilities.h>

static WFFacilities::WaitGroup waitgroup(1);

void signHandler(int num) {
    waitgroup.done();
    fprintf(stderr, "wait group is done\n");
}

void seriesCallback(const SeriesWork* series) {
    fprintf(stderr, "series callback , free pkey\n");
    std::string* pkey = static_cast<std::string*>(series->get_context());
    delete pkey;
}

void redisCallback(WFRedisTask* redisTask) {
    protocol::RedisRequest* req = redisTask->get_req();
    protocol::RedisResponse* resp = redisTask->get_resp();
    int state = redisTask->get_state();
    int error = redisTask->get_error();

    // 专门 存储redis任务的结果
    protocol::RedisValue value;

    switch (state) {
        case WFT_STATE_SYS_ERROR:
            fprintf(stderr, "system error: %s\n", strerror(error));
            break;

        case WFT_STATE_DNS_ERROR:
            fprintf(stderr, "dns error: %s\n", gai_strerror(error));
            break;
        // 如果redis语法有问题 , 会进入 SUCESS
        case WFT_STATE_SUCCESS:
            resp->get_result(value);
            if (value.is_error()) {
                fprintf(stderr, "redis syntax error\n");
                state = WFT_STATE_TASK_ERROR;
            }
            break;
    }

    if (state != WFT_STATE_SUCCESS) {
        fprintf(stderr, "redis task Failed!\n");
        state = WFT_STATE_TASK_ERROR;
        return;
    } else {
        fprintf(stderr, "redis task Success!\n");
    }

    std::string cmd;
    req->get_command(cmd);
    if (cmd == "SET") {
        // firstTask的基本任务做完了
        // 创建新任务，加入序列末尾
        fprintf(stderr, "first task callback begins\n");

        std::string* pkey = static_cast<std::string*>(redisTask->user_data);

        WFRedisTask* secondTask = WFTaskFactory::create_redis_task("redis://127.0.0.1:6379", 0, redisCallback);
        protocol::RedisRequest* req = secondTask->get_req();
        req->set_request("GET", {*pkey});

        // series_of 找到一个执行中的任务所在的序列
        SeriesWork* series = series_of(redisTask);

        series->set_context(static_cast<void*>(pkey));

        // 设置清理堆空间回调函数
        series->set_callback(seriesCallback);

        series->push_back(secondTask);
        
        // 先执行完成
        sleep(10);

        fprintf(stderr, "first task callback ends\n");
    } else  /* if (cmd == "GET") */ {
        // secondTask 基本工作做完了

        fprintf(stderr, "second task callback begins\n");

        fprintf(stderr, "redis request, cmd = %s\n", cmd.c_str());
        if (value.is_string()) {
            fprintf(stderr, "value is a string , value = %s\n", value.string_value().c_str());

        } else if (value.is_array()) {
            fprintf(stderr, "value is string array \n");
            for (size_t i = 0; i < value.arr_size(); ++i) {
                fprintf(stderr, "value at %lu = %s", i, value.arr_at(i).string_value().c_str());
            }
        }

        fprintf(stderr, "second task callback ends\n");
    }
}

int main() {
    signal(SIGINT, signHandler);

    std::string* pkey = new std::string("43key2");

    WFRedisTask* firstTask = WFTaskFactory::create_redis_task("redis://127.0.0.1:6379", 0, redisCallback);
    protocol::RedisRequest* req = firstTask->get_req();
    // // string   vector<string>
    // req->set_request("SET", {"43key","100"});
    // req->set_request("HGETALL", {"43t"});
    // req->set_request("SET", {"43key1", "200"});
    req->set_request("SET", {*pkey, "200"});
    firstTask->user_data = static_cast<void*>(pkey);

    // 启动series任务
    firstTask->start();

    waitgroup.wait();

    return 0;
}
```

 整个程序的流程执行如下：  

- 首先创建了一个redis任务，这个任务将要完成的事情是连接到redis服务端，随后执行一个SET指 令； 
- redis调用start方法启动任务，相当于启动了它在的一个序列； 
- 当第一个任务的redis指令即任务的基本工作完成之后，就开始调用回调函数； 
- 回调函数获取了任务的user_data属性，user_data分配在main函数的栈帧之中，在多个任务执行过程中，它在内存中持续存在； 
- 回调函数执行中存在一个选择结构，如果本次任务是SET指令，那么就用相同的回调创建一个新的 redis任务，去执行SET操作； 
- 创建的新redis任务并不是调用start来异步启动，而是通过series_of函数获取当前任务的序列，并将新任务加入到序列的末尾中； 
- 当第一个任务的回调执行完成之后，序列中的下一个任务就会执行了。 

至此，我们就可以总结出使用序列的一般规律： 

-  创建若干任务，可以在首个任务启动之前创建，也可以在某个任务的回调函数执行过程中动态创建； 
- 对于想要第一个执行的任务，调用其start方法； 
- 每当想要任务之间串行执行的时候，就将后面执行任务通过序列的 push_back 加入到序列中。  

<a name="Er4SQ"></a>
#### 序列总结
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657202800802-83c058b8-dcac-451b-a1dd-e6f0b6491c96.png#clientId=ua343532e-298f-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=287&id=ufe78b1fa&margin=%5Bobject%20Object%5D&name=image.png&originHeight=395&originWidth=597&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33781&status=done&style=none&taskId=uf5465506-69da-4b0e-916e-46d0075632d&title=&width=434.1818181818182)

<a name="epHky"></a>
#### 在序列中使用context（ user_data属性 )共享数据
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657202831394-d43f16e4-0f80-4a24-bbc4-74192282355d.png#clientId=ua343532e-298f-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=296&id=u2484a28b&margin=%5Bobject%20Object%5D&name=image.png&originHeight=407&originWidth=546&originalType=binary&ratio=1&rotation=0&showTitle=false&size=54468&status=done&style=none&taskId=u2302cbf3-0f6a-44d3-90c6-7a1100fdecb&title=&width=397.09090909090907)

 1、需要在任务之间设置明确的先后依赖关系，此时可以采用**系列**将这些任务串联起来，系列可以认为是任务构成的队列，队列内部的任务按照先进先出的方式执行。<br />2、系列内部可以设置 **context**属性，用于在系列内部的任务之间传递数据；<br />3、系列还可以传入一个**callback**，这个callback会在系列中所有的任务完成之后调用。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657281212397-0ab201d3-364b-4aa4-8cca-03942488cd06.png#clientId=ua343532e-298f-4&crop=0.0146&crop=0.0043&crop=0.9834&crop=0.9744&from=paste&height=273&id=uc2d427ed&margin=%5Bobject%20Object%5D&name=image.png&originHeight=388&originWidth=796&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24816&status=done&style=none&taskId=ud6c450c9-3004-49cc-afa8-b04262e3ee0&title=&width=561)

不同的系列之间是可以并行执行，**每个任务**单独启动的时候会**创建一 个系列**，所以任务之间的并行执行其本质就是系列之间的并行执行。  



复习<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657286110627-39cb42b4-1420-453b-befd-12e5b9d18b40.png#clientId=ud72be29f-e2c9-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=353&id=u72af54d0&margin=%5Bobject%20Object%5D&name=image.png&originHeight=485&originWidth=708&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57216&status=done&style=none&taskId=u0c0f80ac-0744-4a33-a0ad-02c27192320&title=&width=514.9090909090909)

<a name="NUGvF"></a>
### 3. 并行任务   ParallelWork 
 与SeriesWork对应的ParallelWork类，描述了一个并行任务，并行任务由序列构成，代表**若干个序列**的**并行执行**。所有序列结束，则这个并行任务的基本工作结束，随后执行这个并行任务所在序列相应的回调函数。<br />需要特别注意的是，ParallelWork本身也是一种任务，所以它可以加入到其他序列中——（而这个 序列又可以用来构建更加复杂的并行任务）  


 使用并行任务的基本流程 

- 首先，使用工厂函数创建了一个ParallelWork类对象； 
- 随后，创建了若干个任务（比如http任务或者redis任务），每个任务创建之后并没有马上启动，而 是根据该任务创建了一个序列； 
   - 可以为每个序列的context申请内存空间以便保存状态； 再将每个序列都加入到并行任务当中； 
- 可以为该并行任务设置回调函数，一般在该回调函数当中会回收所申请的内存空间； 
- 最后，调用Workflow::start_series_work，为该并行任务创建一个序列并启动之。 

下面是涉及到的接口： <br />首先是创建任务所需要的工厂函数： <br />当创建一个任务之后，可以使用Workflow::create_series_work函数在不执行的情况下创建序列。
```cpp
#include<workflow/Workflow.h>
using series_callback_t = std::function<void (const SeriesWork *)>;
static SeriesWork *create_series_work(SubTask *first, 
                          series_callback_t callback);
```
 <br />并行任务类ParallelWork中，存在add_series方法，可以将某个序列加入到并行任务中。  
```cpp
class ParallelWork : public ParallelTask {
    //...
    public:
    void add_series(SeriesWork *series);
}
```

 Workflow::start_series_work函数根据一个任务创建一个序列，然后启动之。  
```cpp
class Workflow {
    public:
    //...
    static void
    start_series_work(SubTask *first, series_callback_t callback);
}
```

 并行任务类ParallelWork中，存在series_at方法，可以获取并行任务当中某个序列的详细信息（比如 context）。  
```cpp
class ParallelWork : public ParallelTask {
    public:
    // ...
    const SeriesWork *series_at(size_t index) const;
}

```


<a name="US8Ay"></a>
#### 一个较复杂的并行的例子
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657286597288-cc1e03ee-de80-4335-84b2-a3cb8dece110.png#clientId=ud72be29f-e2c9-4&crop=0.027&crop=0.2169&crop=0.9834&crop=1&from=paste&height=466&id=u7dd241d1&margin=%5Bobject%20Object%5D&name=image.png&originHeight=670&originWidth=822&originalType=binary&ratio=1&rotation=0&showTitle=false&size=84920&status=done&style=none&taskId=u4fa56a99-bd70-47e6-99ec-f52c21891ea&title=&width=572)

```cpp
// parallelWork.cc
#include <signal.h>
#include <workflow/HttpUtil.h>
#include <workflow/WFFacilities.h>
#include <workflow/Workflow.h>

#include <string>
#include <vector>

static WFFacilities::WaitGroup waitgroup(1);

struct SeriesContext {
    std::string url;
    int state;
    int error;
    protocol::HttpResponse resp;  // 响应报文的完整内容，不是指针
};

void signHandler(int num) {
    waitgroup.done();
    fprintf(stderr, "wait group is done\n");
}

void httpCallback(WFHttpTask *httpTask) {
    fprintf(stderr, "httpTask callback\n");

    SeriesContext *context = static_cast<SeriesContext *>(series_of(httpTask)->get_context());
    fprintf(stderr, "httpTask callback, url = %s\n", context->url.c_str());

    context->state = httpTask->get_state();
    context->error = httpTask->get_error();
    context->resp = std::move(*httpTask->get_resp());
}
void parallelCallback(const ParallelWork *pWork) {
    fprintf(stderr, "ParallelTask callback\n");

    SeriesContext *context;
    for (size_t i = 0; i != pWork->size(); ++i) {
        context = static_cast<SeriesContext *>(pWork->series_at(i)->get_context());

        fprintf(stderr, "url = %s\n", context->url.c_str());
        if (context->state == WFT_STATE_SUCCESS) {
            // print reponse body
            const void *body;
            size_t size;
            // 传入传出参数  底层的cosnt
            // get_parsed_body 方法会修改 指针变量body的指向
            context->resp.get_parsed_body(&body, &size);
            // fwrite(body, 1, size, stderr);
            fprintf(stderr, "%s", (const char *)body);
        } else {
            fprintf(stderr, "state = %d ,error = %d\n", context->state, context->error);
        }

        delete context;
    }
}

int main() {
    // 注册 Ctrl + C 信号
    signal(SIGINT, signHandler);

    // 使用工厂函数创建一个并行任务
    // Workflow::create_parallel_work();
    ParallelWork *pWork = Workflow::create_parallel_work(parallelCallback);

    std::vector<std::string> urlVec = {"http://www.baidu.com",
                                       "http://192.168.4.28:6789",
                                       "http://127.0.0.1:6789"};

    for (size_t i = 0; i != urlVec.size(); ++i) {
        // // 创建若干任务
        // WFTaskFactory::create_http_task();
        std::string url = urlVec[i];
        auto httpTask = WFTaskFactory::create_http_task(url, 0, 0, httpCallback);

        // 修改任务属性
        // protocol::HttpRequest *req = httpTask->get_req();
        auto req = httpTask->get_req();
        req->add_header_pair("Accept", "*/*");
        req->add_header_pair("User-Agent", "myHttpTask");
        req->add_header_pair("Connection", "close");

        // 为响应内容申请堆空间
        SeriesContext *context = new SeriesContext;
        context->url = std::move(url);

        // // 为每个任务创建了一个序列
        // create_series_work();
        // auto series = Workflow::create_series_work(httpTask, nullptr);
        SeriesWork *series = Workflow::create_series_work(httpTask, nullptr);
        // 把存储响应内容的指针 拷贝到序列的context中
        series->set_context(context);

        // // 把序列加入到并行任务中
        // add_series();
        pWork->add_series(series);
    }

    //启动并行任务
    Workflow::start_series_work(pWork, nullptr);

    // 阻塞主线程(wait方法当存在至少一个任务未完成时，线程阻塞。)
    waitgroup.wait();

    return 0;
}
```


WorkFlow 的设计特点：

1. 任何任务放入序列中才能执行   `task->start() 创建序列并执行`
1. 序列之间 是并行的 （序列内部 是串行的 ）；
1. 若 某件事情 需要等待 序列 （ 并行任务 ） 都完成 ；
1. 并行任务也是任务，也可以放在序列中。

<a name="RWHpF"></a>
## 用workflow实现http服务端

<a name="xmk8B"></a>
### 1、简单的http服务器
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657286719949-17d56d83-a6f9-47a4-91e0-e8dc27c2931d.png#clientId=ud72be29f-e2c9-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=407&id=u6003657c&margin=%5Bobject%20Object%5D&name=image.png&originHeight=559&originWidth=787&originalType=binary&ratio=1&rotation=0&showTitle=false&size=85073&status=done&style=none&taskId=u03c47cd0-9d4f-4072-852c-ef323601362&title=&width=572.3636363636364)<br />服务端任务 ：客户端接入后，服务端框架生成的任务


<a name="Xb25y"></a>
#### process函数对象 ( 用户设计的 )
作用：去找到serverTask<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657286746656-9caf8c41-8c51-475f-9b06-7e87ba58cad3.png#clientId=ud72be29f-e2c9-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=335&id=u3e49a7d7&margin=%5Bobject%20Object%5D&name=image.png&originHeight=461&originWidth=680&originalType=binary&ratio=1&rotation=0&showTitle=false&size=62579&status=done&style=none&taskId=u7f9dbae8-db0d-46d2-b489-792582a2630&title=&width=494.54545454545456)<br />每当客户端接入，框架解析完请求时，process就调用<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657287529461-59f749d4-2adf-473c-b90c-410bb285620f.png#clientId=ud72be29f-e2c9-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=73&id=ub2bd82e0&margin=%5Bobject%20Object%5D&name=image.png&originHeight=100&originWidth=474&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13653&status=done&style=none&taskId=ubfab5f82-d2c8-4c74-b77f-224a6fe9700&title=&width=344.72727272727275)

```cpp
void (WFHttpTask *httpTask)
 httpTask /* 服务端任务 */
```

```cpp
// server_01.cc
#include <arpa/inet.h> /* inet_ntoa */
#include <netinet/in.h>
#include <signal.h>
#include <stdio.h>
#include <workflow/HttpUtil.h>
#include <workflow/WFFacilities.h>
#include <workflow/WFHttpServer.h>

static WFFacilities::WaitGroup waitGroup(1);

void sigHandler(int num) {
    waitGroup.done();
    fprintf(stderr, "wait group is done\n");
}

void process(WFHttpTask *serverTask) {
    // 服务端基本工作
    auto resp = serverTask->get_resp();
    resp->set_http_version("HTTP/1.1");
    resp->set_status_code("200");
    resp->set_reason_phrase("OK");
    resp->set_header_pair("Content-Type", "text/plain");
    resp->append_output_body("hello");
    serverTask->set_callback([](WFHttpTask *serverTask) {
        fprintf(stderr, "serverTask Callback is running!\n");
    });
    fprintf(stderr, "process is running!\n");

    // 获取对端
    auto req = serverTask->get_req();
    fprintf(stderr, "%s %s %s\n", req->get_method(),
            req->get_request_uri(),
            req->get_http_version());
    protocol::HttpHeaderCursor cursor(req);
    std::string name;
    std::string value;
    while (cursor.next(name, value)) {
        fprintf(stderr, "%s:%s\n", name.c_str(), value.c_str());
    }

    struct sockaddr_in addr;
    socklen_t len = sizeof(addr);
    serverTask->get_peer_addr((sockaddr *)&addr, &len);
    if (addr.sin_family == AF_INET) {
        fprintf(stderr, "sin_family:AF_INET\n");
        fprintf(stderr, "ip:%s\n", inet_ntoa(addr.sin_addr));
        fprintf(stderr, "port:%d\n", ntohs(addr.sin_port));
    }

}

int main() {
    signal(SIGINT, sigHandler);
    WFHttpServer server(process);
    if (server.start(6789) == 0) {
        waitGroup.wait();
        server.stop();
    } else {
        perror("server start failed\n");
        return -1;
    }
    
    return 0;
}
```


<a name="sM6OB"></a>
### 2、服务器登陆业务

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657292118477-7e808dfb-59f2-477f-a04f-9b37e01f74d0.png#clientId=ud72be29f-e2c9-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=329&id=u435657c8&margin=%5Bobject%20Object%5D&name=image.png&originHeight=453&originWidth=662&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52664&status=done&style=none&taskId=u0bdff82c-9edc-48c6-aaf3-8e8a1ee8d79&title=&width=481.45454545454544)

```cpp
// server_02.cc
#include <arpa/inet.h> /* inet_ntoa */
#include <netinet/in.h>
#include <signal.h>
#include <stdio.h>
#include <workflow/HttpUtil.h>
#include <workflow/WFFacilities.h>
#include <workflow/WFHttpServer.h>

static WFFacilities::WaitGroup waitGroup(1);

struct SeriesContext {
    WFHttpTask *serverTask;
    std::string name;
    std::string key;
};

void sigHandler(int num) {
    waitGroup.done();
    fprintf(stderr, "wait group is done\n");
}

void redisCallback(WFRedisTask *redisTask) {
    protocol::RedisRequest *req = redisTask->get_req();
    protocol::RedisResponse *resp = redisTask->get_resp();
    int state = redisTask->get_state();
    int error = redisTask->get_error();
    /* value对象专门用来存储redis任务的结果 */
    protocol::RedisValue value;
    switch (state) {
        case WFT_STATE_SYS_ERROR:
            fprintf(stderr, "system error: %s\n", strerror(error));
            break;
        case WFT_STATE_DNS_ERROR:
            fprintf(stderr, "dns error: %s\n", gai_strerror(error));
            break;
        case WFT_STATE_SUCCESS:
            resp->get_result(value);
            if (value.is_error()) {
                fprintf(stderr, "redis syntax error\n");
                state = WFT_STATE_TASK_ERROR;
            }
            break;
    }
    if (state != WFT_STATE_SUCCESS) {
        fprintf(stderr, "redis task Failed\n");
        return;
    } else {
        fprintf(stderr, "redis task Success!\n");
    }
    SeriesContext *context = static_cast<SeriesContext *>(series_of(redisTask)->get_context());
    std::string name = context->name;
    std::string key = context->key;
    WFHttpTask *serverTask = context->serverTask;
    if (value.is_nil()) {
        auto resp2client = serverTask->get_resp();
        resp2client->add_header_pair("Content-Type", "text/plain");
        resp2client->append_output_body("you are not login yet!");
    } else {
        std::string storedKey = value.string_value();
        if (storedKey == key) {
            auto resp2client = serverTask->get_resp();
            resp2client->add_header_pair("Content-Type", "text/plain");
            resp2client->append_output_body("login check success!");
        } else {
            auto resp2client = serverTask->get_resp();
            resp2client->add_header_pair("Content-Type", "text/plain");
            resp2client->append_output_body("login check fail!");
        }
    }
    //delete context;
    fprintf(stderr, "redis callback is done\n");
}
void process(WFHttpTask *serverTask) {
    auto resp = serverTask->get_resp();
    auto req = serverTask->get_req();
    //解析客户端的请求
    std::string requestUri = req->get_request_uri();
    // /login?name=test&key=123
    // /login ?name=test&key=123
    std::string query = requestUri.substr(requestUri.find("?") + 1);
    //fprintf(stderr,"query = %s\n", query.c_str());
    std::string nameKV = query.substr(0, query.find("&"));
    std::string keyKV = query.substr(query.find("&") + 1);
    //fprintf(stderr,"nameKV = %s, keyKV = %s\n", nameKV.c_str(), keyKV.c_str());
    std::string name = nameKV.substr(nameKV.find("=") + 1);
    std::string key = keyKV.substr(keyKV.find("=") + 1);
    //fprintf(stderr,"name = %s, key = %s\n", name.c_str(), key.c_str());

    //创建redis任务
    WFRedisTask *redisTask = WFTaskFactory::create_redis_task("redis://127.0.0.1:6379", 0, redisCallback);
    auto redisReq = redisTask->get_req();
    redisReq->set_request("GET", {name});

    //把redisTask加入到serverTask所在的序列
    series_of(serverTask)->push_back(redisTask);
    SeriesContext *context = new SeriesContext;
    context->serverTask = serverTask;
    context->name = name;
    context->key = key;
    series_of(serverTask)->set_context(context);

    serverTask->set_callback([context](WFHttpTask *serverTask) {
        fprintf(stderr, "server callback is done\n");
        delete context;
    });
}

int main() {
    signal(SIGINT, sigHandler);
    WFHttpServer server(process);
    if (server.start(6789) == 0) {
        waitGroup.wait();
        server.stop();
    } else {
        perror("server start failed\n");
        return -1;
    }

    return 0;
}
```

serverTask 对客户端总是通过 serverTask->resp 来设置<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657293734826-537934fe-0409-44f7-993e-7a495bfd5d04.png#clientId=ud72be29f-e2c9-4&crop=0&crop=0.1091&crop=1&crop=0.9855&from=paste&height=292&id=uc739ebd3&margin=%5Bobject%20Object%5D&name=image.png&originHeight=379&originWidth=226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33788&status=done&style=none&taskId=u15584103-0911-4632-a12a-cd9c142b04b&title=&width=174)

<a name="cVrM8"></a>
#### 利用workflow实现反向代理
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657293798954-c3861c61-ceeb-4d0f-9f5d-2add1b981a1e.png#clientId=ud72be29f-e2c9-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=233&id=ubd613283&margin=%5Bobject%20Object%5D&name=image.png&originHeight=296&originWidth=545&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25418&status=done&style=none&taskId=ue896966b-1c8b-4725-96e8-dd3c7ce20ce&title=&width=428.3636474609375)

```cpp
// server_03.cc
#include <arpa/inet.h> /* inet_ntoa */
#include <netinet/in.h>
#include <signal.h>
#include <stdio.h>
#include <workflow/HttpUtil.h>
#include <workflow/WFFacilities.h>
#include <workflow/WFHttpServer.h>

static WFFacilities::WaitGroup waitGroup(1);

void sigHandler(int num) {
    waitGroup.done();
    fprintf(stderr, "wait group is done\n");
}

struct SeriesContext {
    WFHttpTask *serverTask;
};

void httpCallback(WFHttpTask *httpTask) {
    protocol::HttpRequest *req = httpTask->get_req();
    protocol::HttpResponse *resp = httpTask->get_resp();
    int state = httpTask->get_state();
    int error = httpTask->get_error();
    switch (state) {
        case WFT_STATE_SYS_ERROR:
            fprintf(stderr, "system error: %s\n", strerror(error));
            break;
        case WFT_STATE_DNS_ERROR:
            fprintf(stderr, "dns error: %s\n", gai_strerror(error));
            break;
        case WFT_STATE_SUCCESS:
            break;
    }
    if (state != WFT_STATE_SUCCESS) {
        fprintf(stderr, "Failed\n");
        return;
    } else {
        fprintf(stderr, "Success!\n");
    }

    const void *body;
    size_t size;
    resp->get_parsed_body(&body, &size);

    //干脆用resp去赋值serverTask->resp
    resp->append_output_body(body, size);
    SeriesContext *context = static_cast<SeriesContext *>(series_of(httpTask)->get_context());
    protocol::HttpResponse *resp2client = context->serverTask->get_resp();
    *resp2client = std::move(*resp);
}
void process(WFHttpTask *serverTask) {
    auto httpTask = WFTaskFactory::create_http_task("http://47.94.147.94", 0, 0, httpCallback);
    series_of(serverTask)->push_back(httpTask);
    SeriesContext *context = new SeriesContext;
    context->serverTask = serverTask;
    series_of(serverTask)->set_context(context);
    serverTask->set_callback([](WFHttpTask *serverTask) {
        fprintf(stderr, "server task callback\n");
    });
    series_of(serverTask)->set_callback([](const SeriesWork *series) {
        fprintf(stderr, "series callback\n");
        SeriesContext *context = static_cast<SeriesContext *>(series->get_context());
        delete context;
    });
}

int main() {
    signal(SIGINT, sigHandler);
    WFHttpServer server(process);
    if (server.start(1234) == 0) {
        waitGroup.wait();
        server.stop();
    } else {
        perror("server start failed\n");
        return -1;
    }

    return 0;
}
```


<a name="Iz2qf"></a>
#### serverTask
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657293787476-681699e5-c54a-4596-8ae6-bdb3eeac6e14.png#clientId=ud72be29f-e2c9-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=271&id=u0cef5a2e&margin=%5Bobject%20Object%5D&name=image.png&originHeight=373&originWidth=691&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34741&status=done&style=none&taskId=u15c98bae-b786-4f60-983f-65f304b0cde&title=&width=502.54545454545456)




磁盘 稳定（单线程和多线程 速度相同，宜采用 单线程 ）<br />所有线程都会被**操作系统**维持进**一个队列**。<br />**顺序写** 速度比较快   磁臂

网络 不稳定，受带宽和网络状况限制（多线程 保证较高速度，不易断联） 多线程 提升带宽的利用率，保证连接稳定性。<br />顺序写 、 随机写 几乎无差别。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657354494655-5cd50283-db9f-4783-9878-b3a387d436d6.png#clientId=ud72be29f-e2c9-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=394&id=ub942db32&margin=%5Bobject%20Object%5D&name=image.png&originHeight=542&originWidth=592&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55461&status=done&style=none&taskId=ua132483a-de62-4d67-8619-98856b4cca9&title=&width=430.54545454545456)

```c
#include <unistd.h>

ssize_t pread(int fd, void *buf, size_t count, off_t offset);

ssize_t pwrite(int fd, const void *buf, size_t count, off_t offset);
```

```cpp
// WFTaskFactory.h
class WFTaskFactory
{
public:
	static WFHttpTask *create_http_task(const std::string& url,
										int redirect_max,
										int retry_max,
										http_callback_t callback);

	static WFHttpTask *create_http_task(const ParsedURI& uri,
										int redirect_max,
										int retry_max,
										http_callback_t callback);
```


![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657354522728-c0ed4c5e-108f-4f10-ba3e-36294089ef7b.png#clientId=ud72be29f-e2c9-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=381&id=u560d7cbe&margin=%5Bobject%20Object%5D&name=image.png&originHeight=524&originWidth=656&originalType=binary&ratio=1&rotation=0&showTitle=false&size=108942&status=done&style=none&taskId=u36c66430-382f-4e16-858e-d52cc9de549&title=&width=477.09090909090907)

```bash
$ man aio
aio - POSIX asynchronous I/O overview
```

`I/O`多路复用  （ Reactor ）：  有数据了，再去处理<br />异步  （ proactor ）：   处理完数据了 再使用 **回调函数 **通知<br />理论上，异步 更快 ，测试，二者基本相同。( Windows 没有多路复用 )

```cpp
// ioTask.cc
#include <fcntl.h>
#include <signal.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#include <workflow/WFFacilities.h>

static WFFacilities::WaitGroup waitGroup(1);

struct FileData {
    char *buf;
    int fd;
};

void sigHandler(int num) {
    waitGroup.done();
    fprintf(stderr, "wait group is done\n");
}

void callback(WFFileIOTask *IOTask) {
    FileData *filedata = static_cast<FileData *>(IOTask->user_data);
    fprintf(stderr, "buf = %s\n", filedata->buf);
    delete[] filedata->buf;
    close(filedata->fd);
    delete filedata;
}

int main() {
    signal(SIGINT, sigHandler);
    int fd = open("file1", O_RDONLY);

    char *buf = new char[1024];
    FileData *filedata = new FileData;
    filedata->buf = buf;
    filedata->fd = fd;
    WFFileIOTask *IOTask = WFTaskFactory::create_pread_task(fd, buf, 5, 0, callback);
    IOTask->user_data = filedata;

    IOTask->start();

    waitGroup.wait();

    return 0;
}
```



```cpp
// static_server.cc
#include <fcntl.h>
#include <signal.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#include <workflow/HttpUtil.h>
#include <workflow/WFFacilities.h>
#include <workflow/WFHttpServer.h>

static WFFacilities::WaitGroup waitGroup(1);

struct SeriesContext {
    WFHttpTask *serverTask;
    int fd;
    char *buf;
    size_t filesize;
};

void sigHandler(int num) {
    waitGroup.done();
    fprintf(stderr, "wait group is done\n");
}

void IOCallback(WFFileIOTask *IOTask) {
    SeriesContext *context = static_cast<SeriesContext *>(series_of(IOTask)->get_context());
    auto resp2client = context->serverTask->get_resp();
    resp2client->add_header_pair("Content-Type", "text/html");
    resp2client->append_output_body(context->buf, context->filesize);
}
void process(WFHttpTask *serverTask) {
    // 1 创建文件IO任务
    size_t filesize = 614;
    int fd = open("postform.html", O_RDONLY);
    char *buf = new char[filesize];
    auto IOTask = WFTaskFactory::create_pread_task(fd, buf, filesize, 0, IOCallback);
    // 2 把文件IO任务加入到序列中
    series_of(serverTask)->push_back(IOTask);
    // 3 创建传递给IOTask的context
    SeriesContext *context = new SeriesContext;
    context->serverTask = serverTask;
    context->fd = fd;
    context->buf = buf;
    context->filesize = filesize;
    series_of(serverTask)->set_context(context);
    // 4 设置序列的回调函数，释放所有资源
    series_of(serverTask)->set_callback([](const SeriesWork *series) {
        fprintf(stderr, "series callback\n");
        SeriesContext *context = static_cast<SeriesContext *>(series->get_context());
        delete[] context->buf;
        close(context->fd);
        delete context;
    });
}

int main() {
    signal(SIGINT, sigHandler);
    WFHttpServer server(process);
    if (server.start(6789) == 0) {
        waitGroup.wait();
        server.stop();
    } else {
        perror("server start failed\n");
        return -1;
    }

    return 0;
}
```




day08<br />复习<br />workflow  异步+回调<br />客户端任务：

   1. 创建任务 （ http任务 / redis任务 / IO任务 )
   1. 设置任务属性
   1. 组织任务的执行 （satrt  / series->push_back )

服务端任务

   1. 创建WFHttpserver  ,  start
   1. 每当有client连接时，框架会创建任务 （ serverTask )
   1. serverTask = 基本工作 --> process --> 序列中其他任务 --> serverTask回调 --> 序列回调函数
   1. 在serverTask所在序列结束时，响应回复给client。响应内容是 serverTask->resp


<a name="pbsA9"></a>
### 实现一个登陆过程
1、打开网页   GET

2、操作网页元素   POST


优雅化的改造思路：
```cpp
struct MethodHandler{
    std::string method;
    std::function<void (WFHttpTask * serverTask> callback;
}

std::list<MethodHandler>  -> push_back
std::map<std::string, std::shared_ptr<MethodHandler>
```



<a name="Tj7Gu"></a>
### 小项目： 超大文件多片上传 
分块上传思路 ：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657519516333-68e87fab-d364-46ca-a686-73fb7fcf16b8.png#clientId=u04588451-34ea-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=348&id=ub7a52573&margin=%5Bobject%20Object%5D&name=image.png&originHeight=479&originWidth=677&originalType=binary&ratio=1&rotation=0&showTitle=false&size=74402&status=done&style=none&taskId=u4b708b6c-68b1-4c5d-b6c3-531487b0940&title=&width=492.3636363636364)

<a name="bmo9V"></a>
#### 具体步骤：
1、客户端给 /file/mupload/init 发请求
```json
{ filename:xxx, filehash:xxx, filesize:xxx }
```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657519567410-122a46c8-f716-43ba-a80f-4db16d02fb3b.png#clientId=u04588451-34ea-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=127&id=ub81f8cf1&margin=%5Bobject%20Object%5D&name=image.png&originHeight=174&originWidth=799&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46960&status=done&style=none&taskId=u0a40ef96-d9cd-4290-a645-a9025d7d17a&title=&width=581.0909090909091)

服务端：

1. 存入缓存    
```json
HSET MP_file:11:25 chunkCount 4
                   fileName 1.txt
                   chunkSize 12345
```

2. 响应   uploadID 、 chunkCount

2、uppart  ( 不符合RESTful接口标准 ）<br />/file/mupload/uppart?uploadID=xxx&chkidx=02<br />报文体 存放文件内容

1. 解析uploadID 和chkidx
1. 存储  /tmp/1.txt/01

HGET uploadID filename

3. 保存进度到redis

HSET uploadID chkidx_00  1


3、complete<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657519725456-d8dd3d46-e4e7-431a-b378-cfd5f72ec806.png#clientId=u04588451-34ea-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=74&id=u73d4c925&margin=%5Bobject%20Object%5D&name=image.png&originHeight=88&originWidth=452&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16109&status=done&style=none&taskId=u573fa436-b97e-48dd-9d32-0ec4c428306&title=&width=380.727294921875)

1. 解析 uploadID
1. 判断上传是否完成

HGETALL uploadID   统计前缀为chkidx_ 的键的数目<br />找到chunkCount 对应的值<br />二者相比较，相等则上传完成，否则，上传尚未完成

3. 服务端合并分块 （ 可选 )
   1. 创建fileSize大小的空文件
   1. 先pread(0) , 再pwrite(offset)   idx chunkSize
   1. 并行的pread/pwrite 执行完成，文件合并成功

多线程上传、断点续传

```cpp
// mupload.cc
#include <fcntl.h>
#include <signal.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <workflow/HttpUtil.h>
#include <workflow/WFFacilities.h>
#include <workflow/WFHttpServer.h>

#include <iostream>
#include <nlohmann/json.hpp>
#include <string>
using Json = nlohmann::json;

static WFFacilities::WaitGroup waitGroup(1);

void sigHandler(int num) {
    waitGroup.done();
    fprintf(stderr, "wait group is done\n");
}

void process(WFHttpTask *serverTask) {
    // 解析url，分派任务
    auto req = serverTask->get_req();
    auto resp = serverTask->get_resp();
    // 路径 + 查询
    std::string uri = req->get_request_uri();
    std::string path = uri.substr(0, uri.find("?"));
    std::string query = uri.substr(uri.find("?") + 1);
    std::string method = req->get_method();    
    
    /* 创建指定大小空文件： truncate -s 10M testfile */

    if (method == "POST" && path == "/file/mupload/init") {
        /* http://192.168.4.28:6789/file/mupload/init */
        /* body -> {"filename":"testfile","filehash":"a4facea496613c6178e97358aa74198665f3ce87","filesize":10485760} ,*/

        // 初始化
        // 1 读取请求报文，获取请求报文体
        const void *body;
        size_t size;
        req->get_parsed_body(&body, &size);

        // 2 将报文体解析成json对象
        Json fileInfo = Json::parse(static_cast<const char *>(body));
        std::string filename = fileInfo["filename"];
        std::string filehash = fileInfo["filehash"];
        int filesize = fileInfo["filesize"];
        // printf("filename = %s\n filehash = %s\n filesize = %d\n", filename.c_str(),filehash.c_str(),filesize);

        // 3 初始化分块信息 uploadID 分块
        // uploadID = username + time
        std::string uploadID = "username";
        time_t now = time(nullptr);
        struct tm *ptm = localtime(&now);
        char timeStamp[20] = {0};
        snprintf(timeStamp, 20, "%02d:%02d", ptm->tm_hour, ptm->tm_min);
        uploadID += timeStamp;
        //fprintf(stderr,"uploadID = %s\n", uploadID.c_str());

        // 生成分块的信息
        int chunkcount;
        int chunksize = 5 * 1024 * 1024;
        chunkcount = filesize / chunksize + (filesize % chunksize != 0);
        //fprintf(stderr,"chunkcount = %d, chunksize = %d\n", chunkcount,chunksize);

        // 4 生成对客户端的响应
        Json uppartInfo;
        uppartInfo["status"] = "OK";
        uppartInfo["uploadID"] = uploadID;
        uppartInfo["chunkcount"] = chunkcount;
        uppartInfo["filesize"] = filesize;
        uppartInfo["chunksize"] = chunksize;
        uppartInfo["filehash"] = filehash;

        // 5 将一些信息写入缓存
        std::vector<std::vector<std::string>> argsVec = {
            {"MP_" + uploadID, "chunkcount", std::to_string(chunkcount)},
            {"MP_" + uploadID, "filehash", filehash},
            {"MP_" + uploadID, "filesize", std::to_string(filesize)}};
        for (int i = 0; i < 3; ++i) {
            auto redisTask = WFTaskFactory::create_redis_task("redis://127.0.0.1:6379", 2, nullptr);
            redisTask->get_req()->set_request("HSET", argsVec[i]);
            redisTask->start();
        }
        resp->append_output_body(uppartInfo.dump());

    } else if (method == "POST" && path == "/file/mupload/uppart") {
        /* http://192.168.4.28:6789/file/mupload/uppart?uploadID=MP_username15:33&chkidx=1 */
        /* body ->  file_part1 */

        //上传单个分块
        // 1 解析用户请求 提取出 uploadID和chkidx
        // uploadID=MP_username15:33&chkidx=1
        std::string uploadIDKV = query.substr(0, query.find("&"));
        std::string chkidxKV = query.substr(query.find("&") + 1);
        std::string uploadID = uploadIDKV.substr(uploadIDKV.find("=") + 1);
        std::string chkidx = chkidxKV.substr(chkidxKV.find("=") + 1);
        // 2 获取文件的hash，创建目录，写入分块
        // HGET uploadID filehash
        auto redisTaskHGET = WFTaskFactory::create_redis_task("redis://127.0.0.1:6379", 2, [chkidx, req](WFRedisTask *redisTask) {
            protocol::RedisRequest *redisReq = redisTask->get_req();
            protocol::RedisResponse *redisResp = redisTask->get_resp();
            protocol::RedisValue value;
            redisResp->get_result(value);
            // 用hash值 创建空文件
            std::string filehash = value.string_value();
            mkdir(filehash.c_str(), 0777);
            std::string filepath = filehash + "/" + chkidx;
            int fd = open(filepath.c_str(), O_RDWR | O_CREAT, 0666);
            //将文件内容进行写入
            const void *body;
            size_t size;
            req->get_parsed_body(&body, &size);
            fprintf(stderr, "body = %s\nsize = %lu\n", (char *)body, size);
            write(fd, body, size);
            close(fd);
        });
        redisTaskHGET->get_req()->set_request("HGET", {uploadID, "filehash"});
        /* 不push_back()，生命周期结束，会写入空内容 */
        series_of(serverTask)->push_back(redisTaskHGET);
        // 3 写入分块完成之后，将上传的进度存入缓存中
        auto redisTaskHSET = WFTaskFactory::create_redis_task("redis://127.0.0.1:6379", 2, nullptr);
        redisTaskHSET->get_req()->set_request("HSET", {uploadID, "chkidx_" + chkidx , "1"});
        /* 不push_back()，生命周期结束，会写入空内容 */
        series_of(serverTask)->push_back(redisTaskHSET);
        // 4 回复响应
        resp->append_output_body("chkidx_" + chkidx + " is OK !\n");
    } else if (method == "GET" && path == "/file/mupload/complete") {
        /* http://192.168.4.28:6789/file/mupload/complete?uploadID=MP_username15:33 */

        //合并分块
        // 1 解析用户请求 提取出uploadID
        std::string uploadID = query.substr(query.find("=") + 1);

        // 2 根据uploadID查询进度 HGETALL uploadID
        auto redisTask = WFTaskFactory::create_redis_task("redis://127.0.0.1:6379", 2, [resp](WFRedisTask *redisTask) {
            protocol::RedisRequest *redisReq = redisTask->get_req();
            protocol::RedisResponse *redisResp = redisTask->get_resp();
            protocol::RedisValue value;
            redisResp->get_result(value);
            // 3 chunkcount chkidx_*
            int chunkcount;
            int chunknow = 0;
            for (size_t i = 0; i < value.arr_size(); i += 2) {
                std::string key = value.arr_at(i).string_value();
                std::string val = value.arr_at(i + 1).string_value();
                if (key == "chunkcount") {
                    chunkcount = std::stoi(val);
                } else if (key.substr(0, 7) == "chkidx_") {
                    ++chunknow;
                }
            }
            fprintf(stderr, "chunkcount = %d\nchunknow = %d\n", chunkcount, chunknow);
            // 4 比较大小
            if (chunknow == chunkcount) {
                resp->append_output_body("mupload SUCCESS\n");
            } else {
                resp->append_output_body("mupload FAIL\n");
            }
        });
        redisTask->get_req()->set_request("HGETALL", {uploadID});
        series_of(serverTask)->push_back(redisTask);
    }
}
int main() {
    signal(SIGINT, sigHandler);
    WFHttpServer server(process);
    if (server.start(6789) == 0) {
        waitGroup.wait();
        server.stop();
    } else {
        perror("server start failed\n");
        return -1;
    }
    return 0;
}
```


pimpel  第一次编译好以后，不会再次全量编译<br />std::chrono C++11时间库





<a name="bHjXV"></a>
## MySQL 任务

读任务  show / select   `MYSQL_STATUS_OK` <br />写任务   `MYSQL_STATE_GET_RESULT`

创建任务 -> 设置任务属性 -> 启动任务 ->  执行回调      

```cpp
// MySQLTask.cc
#include <signal.h>
#include <workflow/MySQLResult.h>
#include <workflow/MySQLUtil.h>
#include <workflow/WFFacilities.h>

static WFFacilities::WaitGroup waitGroup(1);

void sigHandler(int num) {
    waitGroup.done();
    fprintf(stderr, "wait group is done\n");
}

void callback(WFMySQLTask *mysqlTask) {
    // 检查连接错误
    if (mysqlTask->get_state() != WFT_STATE_SUCCESS) {
        fprintf(stderr, "error msg:%s\n", WFGlobal::get_error_string(mysqlTask->get_state(), mysqlTask->get_error()));
        return;
    }

    protocol::MySQLResponse *resp = mysqlTask->get_resp();
    protocol::MySQLResultCursor cursor(resp);

    // 检查语法错误
    if (resp->get_packet_type() == MYSQL_PACKET_ERROR) {
        fprintf(stderr, "error_code = %d msg = %s\n", resp->get_error_code(), resp->get_error_msg().c_str());
    }

    if (cursor.get_cursor_status() == MYSQL_STATUS_OK) {
        //写指令，执行成功
        fprintf(stderr, "OK. %llu rows affected. %d warnings. insert_id = %llu.\n",
                cursor.get_affected_rows(), cursor.get_warnings(), cursor.get_insert_id());
    }
}

int main() {
    signal(SIGINT, sigHandler);

    auto mysqlTask = WFTaskFactory::create_mysql_task("mysql://root:123456@127.0.0.1:3306", 0, callback);
    /* 需要告知表所属的数据库 */
    std::string sql = "insert into cloudisk.tbl_user_token (user_name,user_token) values ('test5','abc');";
    auto req = mysqlTask->get_req();
    req->set_query(sql);

    mysqlTask->start();

    waitGroup.wait();

    return 0;
}
```
  

读类型的MySQL任务<br />1、域的数量（列数）、名字、类型<br />2、若干个cell -> 一行     若干行 ->  表

访问cell

1. 访问一行
1. 全部取出  `vector<vector<cell>>`




<a name="F76qI"></a>
#### 定时任务
```cpp
#include <signal.h>
#include <sys/time.h>
#include <workflow/WFFacilities.h>

static WFFacilities::WaitGroup waitgroup(1);

void signHandler(int num) {
    waitgroup.done();
    fprintf(stderr, "wait group is done\n");
}

void callback(WFTimerTask *timerTask) {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    printf("callback %ld.%06ld \n", tv.tv_sec, tv.tv_usec);
    /* 循环调用 callback，实现每秒 */
    WFTimerTask *nextTask = WFTaskFactory::create_timer_task(2 * 1000000, callback);
    series_of(timerTask)->push_back(nextTask);
}

int main() {
    // 注册 Ctrl + C 信号
    signal(SIGINT, signHandler);

    WFTimerTask *timerTask = WFTaskFactory::create_timer_task(2 * 1000000, callback);

    timerTask->start();

    struct timeval tv;
    gettimeofday(&tv, NULL);
    printf("main %ld.%06ld\n", tv.tv_sec, tv.tv_usec);

    // 阻塞主线程(wait方法当存在至少一个任务未完成时，线程阻塞。)
    waitgroup.wait();

    return 0;
}
```



<a name="PwZCo"></a>
### wfrest
把workflow的服务端使用方法封装了一下 ( gin )

wfrest的方便之处：

1. 完全支持workflow  (  任务 、序列  )
1. 支持大量的解析工作 
   1. query  /test？key=xxx&value=xxx
   1. post的urlencoded解析
   1. post的form-data解析
3. 直接把方法和path ——> Handler


```cpp
#include <signal.h>
#include <wfrest/HttpServer.h>
#include <workflow/MySQLMessage.h>
#include <workflow/MySQLResult.h>
#include <workflow/WFFacilities.h>

#include <wfrest/json.hpp>
using Json = nlohmann::json;

static WFFacilities::WaitGroup waitGroup(1);

void signHandler(int num) {
    waitGroup.done();
    fprintf(stderr, "wait group is done\n");
}

void callback(WFMySQLTask *mysqlTask) {
    // 检查连接错误
    if (mysqlTask->get_state() != WFT_STATE_SUCCESS) {
        fprintf(stderr, "error msg:%s\n", WFGlobal::get_error_string(mysqlTask->get_state(), mysqlTask->get_error()));
        return;
    }

    protocol::MySQLResponse *resp = mysqlTask->get_resp();
    protocol::MySQLResultCursor cursor(resp);

    // 检查语法错误
    if (resp->get_packet_type() == MYSQL_PACKET_ERROR) {
        fprintf(stderr, "error_code = %d msg = %s\n", resp->get_error_code(), resp->get_error_msg().c_str());
    }

    do {
        if (cursor.get_cursor_status() == MYSQL_STATUS_OK) {
            //写指令，执行成功
            fprintf(stderr, "OK. %llu rows affected. %d warnings. insert_id = %llu.\n",
                    cursor.get_affected_rows(), cursor.get_warnings(), cursor.get_insert_id());
        } else if (cursor.get_cursor_status() == MYSQL_STATUS_GET_RESULT) {
            //读指令，执行成功
            //把所有域信息构成一个数组
            const protocol::MySQLField *const *fields = cursor.fetch_fields();
            for (int i = 0; i < cursor.get_field_count(); ++i) {
                // db table name type
                fprintf(stderr, "db = %s, table = %s, name = %s, type = %s\n", fields[i]->get_db().c_str(),
                        fields[i]->get_table().c_str(),
                        fields[i]->get_name().c_str(),
                        datatype2str(fields[i]->get_data_type()));
            }
            std::vector<std::vector<protocol::MySQLCell>> rows;
            cursor.fetch_all(rows);
            for (auto &row : rows) {
                for (auto &cell : row) {
                    if (cell.is_int()) {
                        printf("[%d]", cell.as_int());
                    } else if (cell.is_ulonglong()) {
                        printf("[%llu]", cell.as_ulonglong());
                    } else if (cell.is_string()) {
                        printf("[%s]", cell.as_string().c_str());
                    } else if (cell.is_datetime()) {
                        printf("[%s]", cell.as_datetime().c_str());
                    }
                }
                printf("\n");
            }
            //cursor.fetch_row()
        }
    } while (cursor.next_result_set());
    wfrest::HttpResp *resp2client = static_cast<wfrest::HttpResp *>(series_of(mysqlTask)->get_context());
    resp2client->String("Mysql OK");
}

int main() {
    signal(SIGINT, signHandler);

    wfrest::HttpServer server;

    server.GET("/test", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        resp->String("Hello");
    });

    server.POST("/test", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        resp->String("Hello");
    });

    server.GET("/redirect", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        resp->set_status_code("302");
        // resp->add_header_pair("Location", "/test");
        resp->headers["Location"] = "/test";
    });

    server.GET("/test1", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        std::map<std::string, std::string> queryMap = req->query_list();
        for (auto it : queryMap) {
            fprintf(stderr, "first = %s, second = %s\n", it.first.c_str(), it.second.c_str());
        }
    });

    server.POST("/login", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        const std::string &username = req->query("username");
        const std::string &password = req->query("password");
        fprintf(stderr, "username = %s, password = %s\n", username.c_str(), password.c_str());
    });

    server.POST("/login1", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        /* application/x-www-form-urlencoded */
        if (req->content_type() != wfrest::APPLICATION_URLENCODED) {
            resp->set_status_code("500");
            return;
        }
        std::map<std::string, std::string> formMap = req->form_kv();
        for (auto it : formMap) {
            fprintf(stderr, "first = %s, second = %s\n", it.first.c_str(), it.second.c_str());
        }
    });

    server.POST("/formdata", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        /* multipart/form-data */
        if (req->content_type() != wfrest::MULTIPART_FORM_DATA) {
            resp->set_status_code("500");
            return;
        }
        using Form = std::map<std::string, std::pair<std::string, std::string>>;
        const Form &form = req->form();
        for (auto it : form) {
            fprintf(stderr, "it.first = %s, it.second.first = %s, it.second.second = %s\n", it.first.c_str(),
                    it.second.first.c_str(),
                    it.second.second.c_str());
        }
    });

    server.GET("/upload.html", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        int fd = open("upload.html", O_RDONLY);
        std::unique_ptr<char[]> buf(new char[6939]);
        read(fd, buf.get(), 6939);
        resp->append_output_body(buf.get(), 6939);
        resp->headers["Content-Type"] = "text/html";
    });

    server.POST("/upload.html", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        if (req->content_type() != wfrest::MULTIPART_FORM_DATA) {
            resp->set_status_code("500");
            return;
        }
        using Form = std::map<std::string, std::pair<std::string, std::string>>;
        const Form &form = req->form();
        for (auto it : form) {
            fprintf(stderr, "it.first = %s, it.second.first = %s, it.second.second = %s\n", it.first.c_str(),
                    it.second.first.c_str(),
                    it.second.second.c_str());
        }
    });

    server.GET("/series", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp, SeriesWork *series) {
        // series就是服务端任务所在的序列
        auto timerTask = WFTaskFactory::create_timer_task(5 * 1000000, [resp](WFTimerTask *timerTask) {
            resp->String("time is over");
        });
        series->push_back(timerTask);
        /* timerTask->start();  // 并行，serverTask没有等待 */
    });

    server.GET("/mysql0", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp, SeriesWork *series) {
        auto mysqlTask = WFTaskFactory::create_mysql_task("mysql://root:123456@127.0.0.1:3306", 0, callback);
        std::string sql =
            "insert into database1.table1 (user_name,user_token) values ('test8','abc');"
            "select * from database1.table1;";
        auto mysqlReq = mysqlTask->get_req();
        mysqlReq->set_query(sql);
        series->push_back(mysqlTask);
        series->set_context(resp);
    });

    server.GET("/mysql1", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        resp->MySQL("mysql://root:123456@127.0.0.1:3306", "SHOW DATABASES;SELECT * FROM database1.table1;");
    });

    server.GET("/mysql2", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        std::string url = "mysql://root:123456@127.0.0.1:3306";
        std::string sql = "SHOW DATABASES;SELECT * FROM database1.table1;";
        resp->MySQL(url, sql, [resp](Json *pjson) {
            // pjson 指向搜集结果的json对象
            std::string info = (*pjson)["result_set"][0]["database"];
            resp->String(info);
        });
    });

    server.GET("/mysql3", [](const wfrest::HttpReq *req, wfrest::HttpResp *resp) {
        std::string url = "mysql://root:123456@127.0.0.1:3306";
        std::string sql = "SHOW DATABASES;";
        resp->MySQL(url, sql, [](protocol::MySQLResultCursor *cursor) {
            std::vector<std::vector<protocol::MySQLCell>> rows;
            cursor->fetch_all(rows);
            for (auto &row : rows) {
                for (auto &cell : row) {
                    if (cell.is_int()) {
                        printf("[%d]", cell.as_int());
                    } else if (cell.is_ulonglong()) {
                        printf("[%llu]", cell.as_ulonglong());
                    } else if (cell.is_string()) {
                        printf("[%s]", cell.as_string().c_str());
                    } else if (cell.is_datetime()) {
                        printf("[%s]", cell.as_datetime().c_str());
                    }
                }
                printf("\n");
            }
        });
    });

    /* track() // 打印出请求 */
    if (server.track().start(6789) == 0) {
        /* .list_routes() 列出服务端支持的方法和路径 */
        server.list_routes();
        waitGroup.wait();
        server.stop();
    } else {
        fprintf(stderr, "can not start server!\n");
        return -1;
    }

    return 0;
}
```



引用与指针的区别 ： 面试暖场问题 <br />C++黄金反向： 推荐      广告      搜索            分布式数据库<br />计算机视觉 好发论文，能早实习     ~~  NLP  ~~

薪水有关 ：名校光环   、 工作年限 、 上份年薪






