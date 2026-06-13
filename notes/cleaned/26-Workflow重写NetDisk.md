## 私有存储网盘 第一版：
#### 文件模块 ：
/file/upload       GET 显示网页    POST 上传文件
/file/upload       GET  下载文件

#### 用户模块 ：
/user/singup  	GET     POST 注册
/user/singin    登陆
/user/info      获取登陆信息

client可以是任何浏览器
主服务端 ： 用户、注册登陆   文件上传
静态资源服务器 ： 下载
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657619809028-752ef9b3-70de-4705-8c60-2cee69a859a0.png)
由之前的 单体 到 上传、下载分离

token 有效时间  一星期  一个月   /  一天   一小时

主从复制：提升读性能 ； 保证稳定性、可靠性。
#### 数据库的分库 分表
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657682524288-3c889fca-d661-4b2d-91f8-f30808e25df8.png)

可以使用 hash值（唯一键约束） 末尾数字 来分表

多用MySQL存储，支持事务

确保 客户端上传到服务器 与 客户端发送出去的  文件一致，hash

## 不要在头文件 `using namespace`

### 总结/复习
网盘项目 基于HTTP协议

#### 用户
/user/signup   GET 静态资源
/usr/signup POST
1、解析请求  2、插入数据库  3、重定向
/user/signin   POST
1、解析请求 2、查询数据库  3、生成token
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657933787824-badec6ef-d2f1-4c87-a929-fc618ac31dc3.png)
/user/info POST
1、解析，得到username和token  2、检查token 3、根据用户名查询用户信息

#### 文件
#### /file/upload   POST

   1. URL的query部分  username=xxx&token=xxx
   1. multipart/form-data
      1. 文件名
      1. 内容

1、解析请求 -> 2、 校验token -> 3、解析form-data  -> 4、保存文件 -> 5、存储信息 （全局文件表 tbl_file   用户文件表 tbl_user_file )
/file/query
1、解析请求 -> 2、 校验token -> 3、查询用户文件表 -> 4、返回Json给前端

OSS备份
1、upload
2、/file/downloadurl

   - nginx
   - OSS

#### 解耦
备份到OSS   与    回复响应  分离

 同步 变成  异步     消息队列
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934010770-177c990f-dae3-4b88-b1c0-dd931e0e9d5f.png)

网络   nginx
~~消息   RabbitMQ(Erlang)    Kafka           java   ~~
缓存
存储
