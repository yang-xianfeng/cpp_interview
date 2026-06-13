### 容器与虚拟机的区别
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657893156752-28600bce-bc65-418d-b152-ece824489f01.png)

轻量级的虚拟机 -> docker 事实上的容器标准
隔离性 (sandbox 沙盒 ）
把运行应用所需要的代码、库、依赖、配置、运行时环境 打包在一起成为一个标准单元   --> **镜像**
通过镜像启动的应用  -->  容器

#### 镜像
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934146379-a91ae423-cda2-4e7f-b46b-313177a51acf.png)

### docker（容器）基本命令

#### 运行容器
```bash
$ docker run
$ docker run nginx:latest echo hello
hello
$ docker ps
$ docker ps -a

$ docker stop  # 停止
$ docker start # 恢复
```

#### 运行容器的终端
```bash
$ docker  run -it nginx /bin/bash
```
Ctrl+d  退出容器、容器停止
Ctrl+p，Ctrl+q 退出容器、容器保持运行

#### 以守护进程启动容器
```bash
$ docker run -d nginx
```

#### 附加到现有的 停止的容器
```bash
$ docker exec  -it id /bin/bash
```

####  批量删除停止的容器：
```bash
docker rm $(docker ps -a -q -f status=exited)
```

#### 端口映射

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934356457-62478834-77f7-4099-9775-ba24d1fdf6d9.png)

```bash
$ docker run -d -p [0.0.0.0:]8080:80 nginx
```
默认只支持TCP转发

#### 容器内容的持久化
**挂载  mount **
**Linux下加新的盘，可以通过**`**mount**`** 命令，挂载 到 挂载点上**

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934384466-7e2e8d55-3d7b-477c-9a2c-d464b9d8fe6d.png)

```bash
$ docker run -v /tmp/test:/usr/share/nginx/html nginx 持久化
```

#### 打包镜像：
```bash
$ docker commit  容器name/容器id  仓库name:tag

$ docker build   （docker file）
```

运维 使用docker较多  Devops反向    kubernetes 云原生开发  （高级版运维  Go/Java ）

### 消息队列 消息代理
一种异步通信机制
producer -> broker -> consumer
相对于producer -> consumer ，使用MQ的优势 ：

- 逻辑解耦（ 同步 -> 异步 )
- 消息持久化
- 瞬时数据量过大，削峰    ->  集群

#### 实现一个消息队列，需要考虑的事情：

- 网络模型 （ 如何建立连接、协议 ）
- 主动拉取 VS  推送消费
- 削峰 （ 限流 ）
- 路由规则

#### rabbitMQ
高可靠 基于**AMQP （ Advanced Message Queuing Protocol)**的消息中间件
AMQP定义了若干的组件 :

- 交换器 Exchange   决定消息怎么样路由到队列中
- 队列  Queue
- 绑定  Binding  一套用于告诉交换器应该将消息存入哪个队列中

交换器+绑定 可以实现单播、组播、广播
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934525716-c06bba20-17ce-4a7c-a53f-d6441319f832.png)

#### 交换器的消息路由模式
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934549360-c5a6987b-7cb0-40cc-834b-7f2fe4b01579.png)

1、direct 模式 ：只要queue的binding key和消息的rounting key完全一致，exchange就会转发     多用来实现单播
2、fanout模式 ：交换器不做任何路由处理，直接广播（消息的rounting key没用）
3、topic 模式 ： 通配符匹配  组播
3、 headers  ： 根据消息内的headers做路由

#### 使用rabbitMQ

1、通过docker部署rabbitMQ
-p 端口映射
-v 持久化
```dockerfile
docker run -d --hostname rabbitsvr --name rabbit -p 5672:5672 -p 15672:15672 -p 25672:25672 -v /data/rabbitmq:/var/lib/rabbitmq rabbitmq:management
```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657935069555-11b7a0eb-8001-476c-88e8-287afbde77e0.png)

1、创建应该exchange  direct模式
2、创建若干个queue
3、为每个queue设置binding key
在exchange里可以public message

#### 将rabbit引入项目

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657935175380-f3aee3a0-ad11-40f9-b163-230c97689edf.png)

#### 生产者
```cpp
//producer.cc
#include <SimpleAmqpClient/SimpleAmqpClient.h>
#include <string>
struct RabbitMqInfo{
    std::string RabbitURL = "amqp://guest:guest@127.0.0.1:5672";
    std::string TransExchangeName = "uploadserver.trans";
    std::string TransQueueName = "uploadserver.trans.oss";
    std::string TransRoutingKey = "oss";
};

int main(){
    // 指定mq的一些信息
    RabbitMqInfo MqInfo;
    // 创建一条和mq的连接
    AmqpClient::Channel::ptr_t channel = AmqpClient::Channel::Create();
    // pause();
    // 创建消息
    AmqpClient::BasicMessage::ptr_t message = AmqpClient::BasicMessage::Create("Hello");
    // 发布消息
    channel->BasicPublish(MqInfo.TransExchangeName,MqInfo.TransRoutingKey,message);
}
```

#### 消费者
两种方式

- 消息队列 主动推送给消费者
- 消费者 主动拉取

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657935206894-26ff002c-c49e-451e-ac39-26751e98377f.png)

- BasicGet  非阻塞
- BasicConsume  定时 阻塞

网络通信  阻塞比非阻塞的性能好

```cpp
// consumer.cc
#include <SimpleAmqpClient/SimpleAmqpClient.h>
#include <string>
struct RabbitMqInfo{
    std::string RabbitURL = "amqp://guest:guest@127.0.0.1:5672";
    std::string TransExchangeName = "uploadserver.trans";
    std::string TransQueueName = "uploadserver.trans.oss";
    std::string TransRoutingKey = "oss";
};

int main(){
    // 指定mq的一些信息
    RabbitMqInfo MqInfo;
    // 创建一条和mq的连接
    AmqpClient::Channel::ptr_t channel = AmqpClient::Channel::Create();
    // 从mq中提取消息
    channel->BasicConsume(MqInfo.TransQueueName,MqInfo.TransQueueName);

    AmqpClient::Envelope::ptr_t envelope;
    bool isNotTimeout = channel->BasicConsumeMessage(envelope,5000);
    if(isNotTimeout == false){
        fprintf(stderr,"timeout\n");
        return -1;
    }

    fprintf(stderr,"message = %s\n", envelope->Message()->Body().c_str());

    return 0;
}
```

#### 总结: 单体应用的缺陷
1、开发    需要了解所有技术栈
2、性能 表现不佳
3、运维

单体应用 架构  -->   微服务架构( IBM )
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137634313-07107260-5369-4a99-a504-e25c6594621c.png)

低耦合、高内聚

简单应用 、对性能和延迟要求高的应用  不会使用 微服务
粒度
tradeoff   权衡、取舍

#### 把函数调用改造成网络通信
RESTful 风格API设计
1、使用HTTP
2、对象  -->  资源 URL
3、成员函数/方法  -->  方法
增   -->   不幂等的行为
4、参数 和 返回值  -->  报文体  Json/XML

问题：
1、HTTP协议比较复杂，内网多使用私有协议
2、使用函数 复杂
3、效率低

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137707938-224bedd3-28eb-435d-8673-c0b40b644ddb.png)
A可以调用位于另一台机器B的函数

远程过程调用  （ RPC ）

REST区别：

- RESTful是一种接口设计风格  RPC是一种具体技术
- 解决同一类问题（单体应用 --> 微服务 ），优势不同
   - 优缺点

#### 代理模式
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137739027-e9d3d3d9-134c-45fa-9791-3317259aaadf.png)

#### 序列化和反序列化
序列化 ： 对象 --> 字节流
反序列化 ： 字节流 --> 对象
序列化 : json.dump()
反序列化 ：json::parse()

json的问题
1、效率
2、向前兼容向后兼容

protobuf （ Google )
专用于RPC的序列化方案
1、二进制
2、支持向前向后兼容
3、跨语言
4、特别适合 RPC

#### 安装protobuf
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137760683-5e0b867b-b7b4-499b-ab55-f46a20627566.png)

#### 使用protobuf
1、写IDL文件 （ Interface Description Language ) 接口描述语言

**反射**：通过方法找到对象 （ 与常规的 先对象，后方法相反 ）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137808325-e951a45e-f040-4e2f-a560-3af74839b3a7.png)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137819341-1d02ab97-4e23-4976-9cc0-4525d8b24598.png)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137843051-aee7e48d-7c8c-4df4-85f4-6aac73d121a3.png)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137874892-9a70e5dc-ddee-43d7-8262-a88f789ffe09.png)

向前兼容 ： 旧代码处理新消息
1、新字段 使用新编号
2、旧代码遇到新编号，忽略新字段
3、删除字段要保留编号
4、可以随意更换字段名，不能更改字段类型

向后兼容 ： 新代码处理旧消息
1、任何新加的字段属性是optional

RPC ：
1、网络通信
2、代理模式
3、序列化和反序列化  protobuf

thrift (facebook) / GRPC (google http2.0) / BRPC (baidu 协程)/ TARS（tengxu ）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136842387-8aa35cd0-81d0-480f-adeb-948eba7d5ece.png)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136861015-e8e6c562-e154-4fe0-b387-8386a93924c6.png)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136881888-d51125a6-9c54-410a-8787-b2a059c96250.png)

```bash
protoc signup.proto --cpp_out=. --proto_path=.
```
pb.h  pb.cc  消息的接口和实现

```bash
srpc_generator protobuf signup.proto
```
srpc.h  rpc的接口与设计
client_skeleton.cc   server_skeleton.cc

#### 客户端的逻辑
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136904829-6647f1cb-d6a0-4273-8420-8a9abb7ea464.png)

使用rpc的形式 和 普通函数调用 一样

#### 服务端的逻辑
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136922544-a2831f1c-2ab4-4c40-9473-cedd94ef663a.png)

使用SRPC改造注册的过程
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136941234-a2ca7e71-6e8c-4906-ab0e-a507f99262e2.png)

client   -- admin,1234--> server  --> 数据库

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136959632-57b5da74-a3a9-4c03-94d8-a81aba8dfac2.png)

#### 一：代理模式

#### 二：使用任务的形式来使用客户端

总结：
srpc 基于workflow 、protobuf
1、生成IDL文件
2、protoc 、 生成参数&响应的消息的接口
3、srpc_generator  生成服务端和客户端 skeleton
服务端  继承service 、 重写rpc的方法 、 创建派生类对象 、 注册到服务端中
客户端 : 根据ip : port 生成服务端代理  、调用rpc 就是调用代理对象的方法

#### 网盘项目的微服务化改造
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137004871-3f570bc7-43ab-41fe-b5ef-d4707bb89521.png)

#### 微服务的好处
1、开发和治理分离
2、高内聚、低耦合
3、独立部署，升级
4、容错性
5、异构系统

#### 注册中心 （ 流量集中点 服务瓶颈 ）
1、加机器 （水平拓展 —）
2、去中心化 （下一代产品）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137033168-90a8c190-d6f1-477f-89dc-485dc68f1673.png)

### consul
使用go语言，基于 raft共识算法
不管使用什么语言，使用docker部署即可

其他产品 ：
Java    zookeeper   Zab共识算法( 各方面都较差 )   Kafka自带集群
Go      Etcd      raft共识算法   kubernetes管理
C++   braft ( baidu )      raft共识算法

#### 部署一个consul集群
```bash
# 主节点
$ docker run --name consul1 -d -p 8500:8500 -p 8301:8301 -p 8302:8302 consul agent -server -bootstrap-expect 2 -ui -bind=0.0.0.0 -client=0.0.0.0
# 查看主节点
$ docker inspect --format '{{.NetworkSettings.IPAddress}}' consul1
172.18.0.2

# 从节点
$ docker run --name consul2 -d -p 8501:8501 consul agent -server -bind=0.0.0.0 -client=0.0.0.0 -join=172.18.0.2

$ docker run --name consul3 -d -p 8502:8502 consul agent -server -bind=0.0.0.0 -client=0.0.0.0 -join=172.18.0.2
```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137070810-cb7bda3b-cccb-4926-80f4-452908776be7.png)

#### consul支持的操作
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137102325-22508c3d-8cb0-4837-b203-2ee7c6a44113.png)
如果ip:port变了，再重新向consul发一次请求

consul 支持 RESTful API
使用第三方库 / SDK

```cpp
#include <ppconsul/agent.h>

-lppconsul
```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137314580-fd254582-2272-403f-a078-3548caadca0a.png)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137325005-c85a8bf8-8743-40df-a543-293383b1217e.png)

wfrest（ http ） --> rpc ( 私有协议 ）

总结：
注册中心  KV( 键值对 )数据库    “SignupService” ——> { 127.0.0.1:412}
服务端   register   servicePass
客户端  读

Leslie Lamport    分布式之父
有迫不得已的理由（ 性能差、延迟高），才会使用分布式
