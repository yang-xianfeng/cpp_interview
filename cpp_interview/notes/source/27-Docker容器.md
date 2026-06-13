<a name="B2RHO"></a>
### 容器与虚拟机的区别
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657893156752-28600bce-bc65-418d-b152-ece824489f01.png#clientId=u91b69003-f95f-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=218&id=ua0e72921&margin=%5Bobject%20Object%5D&name=image.png&originHeight=300&originWidth=710&originalType=binary&ratio=1&rotation=0&showTitle=false&size=98982&status=done&style=none&taskId=u5a5e3e7e-79f4-47a5-9cdb-f4bc708f782&title=&width=516.3636363636364)

轻量级的虚拟机 -> docker 事实上的容器标准<br />隔离性 (sandbox 沙盒 ）<br />把运行应用所需要的代码、库、依赖、配置、运行时环境 打包在一起成为一个标准单元   --> **镜像**<br />通过镜像启动的应用  -->  容器 

<a name="NEDnc"></a>
#### 镜像
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934146379-a91ae423-cda2-4e7f-b46b-313177a51acf.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=326&id=u1cc3c0f8&margin=%5Bobject%20Object%5D&name=image.png&originHeight=448&originWidth=645&originalType=binary&ratio=1&rotation=0&showTitle=false&size=78557&status=done&style=none&taskId=uc39d2b26-4b31-4a9e-ae27-4bceb2859d4&title=&width=469.09090909090907)

<a name="g77r5"></a>
### docker（容器）基本命令

<a name="fFV2v"></a>
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


<a name="TpTuq"></a>
#### 运行容器的终端
```bash
$ docker  run -it nginx /bin/bash
```
Ctrl+d  退出容器、容器停止<br />Ctrl+p，Ctrl+q 退出容器、容器保持运行

<a name="fcw7X"></a>
#### 以守护进程启动容器
```bash
$ docker run -d nginx
```


<a name="oUVJR"></a>
#### 附加到现有的 停止的容器
```bash
$ docker exec  -it id /bin/bash
```

<a name="V2oUa"></a>
####  批量删除停止的容器：  
```bash
docker rm $(docker ps -a -q -f status=exited)
```

<a name="TPDvr"></a>
#### 端口映射

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934356457-62478834-77f7-4099-9775-ba24d1fdf6d9.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=204&id=u6ad0dc31&margin=%5Bobject%20Object%5D&name=image.png&originHeight=280&originWidth=683&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24794&status=done&style=none&taskId=ua536edf1-fc24-4175-887f-0644f2e8db7&title=&width=496.72727272727275)

```bash
$ docker run -d -p [0.0.0.0:]8080:80 nginx
```
默认只支持TCP转发


<a name="P4sFd"></a>
#### 容器内容的持久化
**挂载  mount **<br />**Linux下加新的盘，可以通过**`**mount**`** 命令，挂载 到 挂载点上**

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934384466-7e2e8d55-3d7b-477c-9a2c-d464b9d8fe6d.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=196&id=u0386c7b8&margin=%5Bobject%20Object%5D&name=image.png&originHeight=270&originWidth=518&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24105&status=done&style=none&taskId=u4435d57a-f99a-4703-b82b-733b854d1ce&title=&width=376.72727272727275)

```bash
$ docker run -v /tmp/test:/usr/share/nginx/html nginx 持久化
```



<a name="Sp17n"></a>
#### 打包镜像：
```bash
$ docker commit  容器name/容器id  仓库name:tag

$ docker build   （docker file）
```

运维 使用docker较多  Devops反向    kubernetes 云原生开发  （高级版运维  Go/Java ）


<a name="D4C5m"></a>
### 消息队列 消息代理
一种异步通信机制<br />producer -> broker -> consumer<br />相对于producer -> consumer ，使用MQ的优势 ：

- 逻辑解耦（ 同步 -> 异步 )
- 消息持久化
- 瞬时数据量过大，削峰    ->  集群

<a name="N1WQB"></a>
#### 实现一个消息队列，需要考虑的事情：

- 网络模型 （ 如何建立连接、协议 ）
- 主动拉取 VS  推送消费
- 削峰 （ 限流 ）
- 路由规则

<a name="eeJEF"></a>
#### rabbitMQ 
高可靠 基于**AMQP （ Advanced Message Queuing Protocol)**的消息中间件<br />AMQP定义了若干的组件 :

- 交换器 Exchange   决定消息怎么样路由到队列中
- 队列  Queue
- 绑定  Binding  一套用于告诉交换器应该将消息存入哪个队列中

交换器+绑定 可以实现单播、组播、广播<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934525716-c06bba20-17ce-4a7c-a53f-d6441319f832.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=104&id=u848cc080&margin=%5Bobject%20Object%5D&name=image.png&originHeight=143&originWidth=627&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24264&status=done&style=none&taskId=u256f2ec9-9cda-422c-8669-33553fb7cc7&title=&width=456)

<a name="A6Tra"></a>
#### 交换器的消息路由模式
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934549360-c5a6987b-7cb0-40cc-834b-7f2fe4b01579.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=357&id=u482fd695&margin=%5Bobject%20Object%5D&name=image.png&originHeight=491&originWidth=697&originalType=binary&ratio=1&rotation=0&showTitle=false&size=88503&status=done&style=none&taskId=u0da87b2f-ba09-4347-80f6-fefeffdb4b9&title=&width=506.90909090909093)

1、direct 模式 ：只要queue的binding key和消息的rounting key完全一致，exchange就会转发     多用来实现单播<br />2、fanout模式 ：交换器不做任何路由处理，直接广播（消息的rounting key没用）<br />3、topic 模式 ： 通配符匹配  组播<br />3、 headers  ： 根据消息内的headers做路由

<a name="hWfx5"></a>
#### 使用rabbitMQ

1、通过docker部署rabbitMQ<br />-p 端口映射<br />-v 持久化
```dockerfile
docker run -d --hostname rabbitsvr --name rabbit -p 5672:5672 -p 15672:15672 -p 25672:25672 -v /data/rabbitmq:/var/lib/rabbitmq rabbitmq:management
```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657935069555-11b7a0eb-8001-476c-88e8-287afbde77e0.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=401&id=C3o5U&margin=%5Bobject%20Object%5D&name=image.png&originHeight=551&originWidth=1019&originalType=binary&ratio=1&rotation=0&showTitle=false&size=155272&status=done&style=none&taskId=u13282eaa-2f66-4280-be65-06b869e315c&title=&width=741.0909090909091)

1、创建应该exchange  direct模式<br />2、创建若干个queue<br />3、为每个queue设置binding key<br />在exchange里可以public message


<a name="WKJew"></a>
#### 将rabbit引入项目

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657935175380-f3aee3a0-ad11-40f9-b163-230c97689edf.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=268&id=u29637aa7&margin=%5Bobject%20Object%5D&name=image.png&originHeight=369&originWidth=634&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43581&status=done&style=none&taskId=u27a92e9d-cf3b-4ba6-b0f9-f338e8f9b56&title=&width=461.09090909090907)



<a name="j4KR1"></a>
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


<a name="Nu9Lt"></a>
#### 消费者 
两种方式

- 消息队列 主动推送给消费者
- 消费者 主动拉取

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657935206894-26ff002c-c49e-451e-ac39-26751e98377f.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=295&id=ue324d758&margin=%5Bobject%20Object%5D&name=image.png&originHeight=406&originWidth=632&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34036&status=done&style=none&taskId=uaefdcd0b-a2ce-4896-b063-3eb2aa93956&title=&width=459.6363636363636)

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



<a name="eW04c"></a>
#### 总结: 单体应用的缺陷
1、开发    需要了解所有技术栈<br />2、性能 表现不佳<br />3、运维

单体应用 架构  -->   微服务架构( IBM )<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137634313-07107260-5369-4a99-a504-e25c6594621c.png#clientId=u230ba7de-7d2d-4&crop=0.0092&crop=0.0508&crop=1&crop=0.9797&from=paste&height=195&id=uf389a86a&margin=%5Bobject%20Object%5D&name=image.png&originHeight=271&originWidth=597&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28114&status=done&style=none&taskId=uf362b439-07e4-4593-87b2-0a4daec53ed&title=&width=430)

低耦合、高内聚

简单应用 、对性能和延迟要求高的应用  不会使用 微服务<br />粒度<br />tradeoff   权衡、取舍

<a name="smArn"></a>
#### 把函数调用改造成网络通信
RESTful 风格API设计<br />1、使用HTTP<br />2、对象  -->  资源 URL<br />3、成员函数/方法  -->  方法<br />增   -->   不幂等的行为<br />4、参数 和 返回值  -->  报文体  Json/XML

问题：<br />1、HTTP协议比较复杂，内网多使用私有协议<br />2、使用函数 复杂<br />3、效率低

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137707938-224bedd3-28eb-435d-8673-c0b40b644ddb.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0.053&crop=1&crop=1&from=paste&height=76&id=swxTu&margin=%5Bobject%20Object%5D&name=image.png&originHeight=104&originWidth=402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10963&status=done&style=none&taskId=ua76f92aa-234f-4187-aa15-174431b824d&title=&width=292)<br />A可以调用位于另一台机器B的函数


远程过程调用  （ RPC ）

REST区别：

- RESTful是一种接口设计风格  RPC是一种具体技术
- 解决同一类问题（单体应用 --> 微服务 ），优势不同
   - 优缺点


<a name="u9wfy"></a>
#### 代理模式
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137739027-e9d3d3d9-134c-45fa-9791-3317259aaadf.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=288&id=ub8279d37&margin=%5Bobject%20Object%5D&name=image.png&originHeight=396&originWidth=656&originalType=binary&ratio=1&rotation=0&showTitle=false&size=47936&status=done&style=none&taskId=uada0e9af-7904-4d0e-8d07-81694bdf561&title=&width=477.09090909090907)


<a name="kBztB"></a>
#### 序列化和反序列化
序列化 ： 对象 --> 字节流<br />反序列化 ： 字节流 --> 对象<br />序列化 : json.dump()<br />反序列化 ：json::parse()

json的问题<br />1、效率<br />2、向前兼容向后兼容

protobuf （ Google )<br />专用于RPC的序列化方案<br />1、二进制<br />2、支持向前向后兼容<br />3、跨语言<br />4、特别适合 RPC


<a name="Alvld"></a>
#### 安装protobuf
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137760683-5e0b867b-b7b4-499b-ab55-f46a20627566.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=235&id=u240e940a&margin=%5Bobject%20Object%5D&name=image.png&originHeight=323&originWidth=533&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35198&status=done&style=none&taskId=u9d5b1099-2136-44cf-a607-833a50290af&title=&width=387.6363636363636)

<a name="cz3Up"></a>
#### 使用protobuf
1、写IDL文件 （ Interface Description Language ) 接口描述语言

**反射**：通过方法找到对象 （ 与常规的 先对象，后方法相反 ）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137808325-e951a45e-f040-4e2f-a560-3af74839b3a7.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=252&id=uc205edc7&margin=%5Bobject%20Object%5D&name=image.png&originHeight=347&originWidth=599&originalType=binary&ratio=1&rotation=0&showTitle=false&size=78023&status=done&style=none&taskId=u4334bfd4-be71-4316-892f-859490f01ef&title=&width=435.6363636363636)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137819341-1d02ab97-4e23-4976-9cc0-4525d8b24598.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=179&id=u75581870&margin=%5Bobject%20Object%5D&name=image.png&originHeight=224&originWidth=341&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24921&status=done&style=none&taskId=u2cce4ebf-4455-4b1b-826e-fddebcf89d2&title=&width=272)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137843051-aee7e48d-7c8c-4df4-85f4-6aac73d121a3.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=153&id=ua3edd5de&margin=%5Bobject%20Object%5D&name=image.png&originHeight=210&originWidth=691&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59094&status=done&style=none&taskId=uf9b278ef-d1ce-4970-a997-79430965e33&title=&width=502.54545454545456)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137874892-9a70e5dc-ddee-43d7-8262-a88f789ffe09.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=289&id=u90013164&margin=%5Bobject%20Object%5D&name=image.png&originHeight=398&originWidth=582&originalType=binary&ratio=1&rotation=0&showTitle=false&size=84588&status=done&style=none&taskId=udaae1d01-1800-4152-be36-17b0cabc30e&title=&width=423.27272727272725)

向前兼容 ： 旧代码处理新消息<br />1、新字段 使用新编号<br />2、旧代码遇到新编号，忽略新字段<br />3、删除字段要保留编号<br />4、可以随意更换字段名，不能更改字段类型

向后兼容 ： 新代码处理旧消息<br />1、任何新加的字段属性是optional



RPC ：<br />1、网络通信<br />2、代理模式<br />3、序列化和反序列化  protobuf

thrift (facebook) / GRPC (google http2.0) / BRPC (baidu 协程)/ TARS（tengxu ）


![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136842387-8aa35cd0-81d0-480f-adeb-948eba7d5ece.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=350&id=u51ccc524&margin=%5Bobject%20Object%5D&name=image.png&originHeight=481&originWidth=584&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46544&status=done&style=none&taskId=u523c8f38-1a30-46d0-b3ec-a1715a77af6&title=&width=424.72727272727275)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136861015-e8e6c562-e154-4fe0-b387-8386a93924c6.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=265&id=u8c6d7ceb&margin=%5Bobject%20Object%5D&name=image.png&originHeight=364&originWidth=520&originalType=binary&ratio=1&rotation=0&showTitle=false&size=61302&status=done&style=none&taskId=u00ae62b8-5f29-4170-a959-7e5c7850fb8&title=&width=378.1818181818182)


![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136881888-d51125a6-9c54-410a-8787-b2a059c96250.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=388&id=u054e7df9&margin=%5Bobject%20Object%5D&name=image.png&originHeight=534&originWidth=813&originalType=binary&ratio=1&rotation=0&showTitle=false&size=136607&status=done&style=none&taskId=u2678492c-7c58-465f-b3e6-673eaae7551&title=&width=591.2727272727273)

```bash
protoc signup.proto --cpp_out=. --proto_path=.
```
pb.h  pb.cc  消息的接口和实现

```bash
srpc_generator protobuf signup.proto
```
srpc.h  rpc的接口与设计<br />client_skeleton.cc   server_skeleton.cc


<a name="jkrht"></a>
#### 客户端的逻辑
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136904829-6647f1cb-d6a0-4273-8420-8a9abb7ea464.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=371&id=ucd896e17&margin=%5Bobject%20Object%5D&name=image.png&originHeight=510&originWidth=770&originalType=binary&ratio=1&rotation=0&showTitle=false&size=131585&status=done&style=none&taskId=u2dc1a3e1-4cb2-4848-a87d-de689d4f79c&title=&width=560)

使用rpc的形式 和 普通函数调用 一样



<a name="F28fB"></a>
#### 服务端的逻辑
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136922544-a2831f1c-2ab4-4c40-9473-cedd94ef663a.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=391&id=u45207622&margin=%5Bobject%20Object%5D&name=image.png&originHeight=537&originWidth=711&originalType=binary&ratio=1&rotation=0&showTitle=false&size=97183&status=done&style=none&taskId=u366c8c29-ad6f-4807-a764-032f74b30ab&title=&width=517.0909090909091)


使用SRPC改造注册的过程<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136941234-a2ca7e71-6e8c-4906-ab0e-a507f99262e2.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=396&id=u55f250df&margin=%5Bobject%20Object%5D&name=image.png&originHeight=544&originWidth=816&originalType=binary&ratio=1&rotation=0&showTitle=false&size=135344&status=done&style=none&taskId=u426ee468-1a4d-4e84-8668-ab41b58a1d4&title=&width=593.4545454545455)

client   -- admin,1234--> server  --> 数据库


![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658136959632-57b5da74-a3a9-4c03-94d8-a81aba8dfac2.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=190&id=u09b13e85&margin=%5Bobject%20Object%5D&name=image.png&originHeight=261&originWidth=591&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59205&status=done&style=none&taskId=u2a091d9c-5ddb-4c93-86e4-cfa697adebb&title=&width=429.8181818181818)

<a name="UQTby"></a>
#### 一：代理模式


<a name="e0Cid"></a>
#### 二：使用任务的形式来使用客户端


总结：<br />srpc 基于workflow 、protobuf<br />1、生成IDL文件<br />2、protoc 、 生成参数&响应的消息的接口<br />3、srpc_generator  生成服务端和客户端 skeleton<br />服务端  继承service 、 重写rpc的方法 、 创建派生类对象 、 注册到服务端中<br />客户端 : 根据ip : port 生成服务端代理  、调用rpc 就是调用代理对象的方法 




<a name="j0ISh"></a>
#### 网盘项目的微服务化改造
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137004871-3f570bc7-43ab-41fe-b5ef-d4707bb89521.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=333&id=ua23d8bb5&margin=%5Bobject%20Object%5D&name=image.png&originHeight=458&originWidth=762&originalType=binary&ratio=1&rotation=0&showTitle=false&size=60635&status=done&style=none&taskId=u693c72dd-8c06-4a36-b0f8-1384e3b7952&title=&width=554.1818181818181)


<a name="YQDXy"></a>
#### 微服务的好处
1、开发和治理分离<br />2、高内聚、低耦合<br />3、独立部署，升级<br />4、容错性<br />5、异构系统

<a name="KhjmP"></a>
#### 注册中心 （ 流量集中点 服务瓶颈 ）
1、加机器 （水平拓展 —）<br />2、去中心化 （下一代产品）<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137033168-90a8c190-d6f1-477f-89dc-485dc68f1673.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=255&id=uea623023&margin=%5Bobject%20Object%5D&name=image.png&originHeight=350&originWidth=825&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46583&status=done&style=none&taskId=uffc82a68-d9b0-4e69-b3cc-aec305b9db6&title=&width=600)

<a name="Olccn"></a>
### consul   
使用go语言，基于 raft共识算法<br />不管使用什么语言，使用docker部署即可

其他产品 ： <br />Java    zookeeper   Zab共识算法( 各方面都较差 )   Kafka自带集群<br />Go      Etcd      raft共识算法   kubernetes管理<br />C++   braft ( baidu )      raft共识算法



<a name="LroFG"></a>
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

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137070810-cb7bda3b-cccb-4926-80f4-452908776be7.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=332&id=u6d746a12&margin=%5Bobject%20Object%5D&name=image.png&originHeight=456&originWidth=738&originalType=binary&ratio=1&rotation=0&showTitle=false&size=78741&status=done&style=none&taskId=ue77724d6-fddb-4123-b35f-ba0c57d7435&title=&width=536.7272727272727)

<a name="hbrQW"></a>
#### consul支持的操作
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137102325-22508c3d-8cb0-4837-b203-2ee7c6a44113.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=201&id=u20303498&margin=%5Bobject%20Object%5D&name=image.png&originHeight=277&originWidth=570&originalType=binary&ratio=1&rotation=0&showTitle=false&size=41797&status=done&style=none&taskId=u0c1acaac-b8d6-4024-ba76-f27f2b9fe9a&title=&width=414.54545454545456)<br />如果ip:port变了，再重新向consul发一次请求

consul 支持 RESTful API<br />使用第三方库 / SDK

```cpp
#include <ppconsul/agent.h>

-lppconsul
```


![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137314580-fd254582-2272-403f-a078-3548caadca0a.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=403&id=u9865b3b0&margin=%5Bobject%20Object%5D&name=image.png&originHeight=554&originWidth=712&originalType=binary&ratio=1&rotation=0&showTitle=false&size=157578&status=done&style=none&taskId=uf951c8c2-b800-4818-9525-1cb3636236a&title=&width=517.8181818181819)


![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658137325005-c85a8bf8-8743-40df-a543-293383b1217e.png#clientId=u230ba7de-7d2d-4&crop=0&crop=0.2777&crop=1&crop=1&from=paste&height=80&id=u303786c8&margin=%5Bobject%20Object%5D&name=image.png&originHeight=110&originWidth=773&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32280&status=done&style=none&taskId=u1a6865b0-f96e-4efa-bfc1-8beccb2e15e&title=&width=562)


wfrest（ http ） --> rpc ( 私有协议 ）



总结：<br />注册中心  KV( 键值对 )数据库    “SignupService” ——> { 127.0.0.1:412}<br />服务端   register   servicePass<br />客户端  读




Leslie Lamport    分布式之父<br />有迫不得已的理由（ 性能差、延迟高），才会使用分布式
