<a name="KUCNp"></a>
## 私有存储网盘 第一版：
<a name="PdSmM"></a>
#### 文件模块 ： 
/file/upload       GET 显示网页    POST 上传文件<br />/file/upload       GET  下载文件

<a name="UAPUI"></a>
#### 用户模块 ：
/user/singup  	GET     POST 注册<br />/user/singin    登陆<br />/user/info      获取登陆信息


client可以是任何浏览器  <br />主服务端 ： 用户、注册登陆   文件上传<br />静态资源服务器 ： 下载<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657619809028-752ef9b3-70de-4705-8c60-2cee69a859a0.png#clientId=u11b1d79d-5bc8-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=212&id=ubf1d5e33&margin=%5Bobject%20Object%5D&name=image.png&originHeight=291&originWidth=586&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53170&status=done&style=none&taskId=uf067bb38-3bdd-4152-80c7-7abadf54332&title=&width=426.1818181818182)<br />由之前的 单体 到 上传、下载分离  



token 有效时间  一星期  一个月   /  一天   一小时

主从复制：提升读性能 ； 保证稳定性、可靠性。
<a name="l94Uc"></a>
#### 数据库的分库 分表
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657682524288-3c889fca-d661-4b2d-91f8-f30808e25df8.png#clientId=u11b1d79d-5bc8-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=348&id=u8b11c789&margin=%5Bobject%20Object%5D&name=image.png&originHeight=479&originWidth=783&originalType=binary&ratio=1&rotation=0&showTitle=false&size=191479&status=done&style=none&taskId=u7c8b065f-125c-4176-8c7c-72dba928f62&title=&width=569.4545454545455)

可以使用 hash值（唯一键约束） 末尾数字 来分表

多用MySQL存储，支持事务  

确保 客户端上传到服务器 与 客户端发送出去的  文件一致，hash


<a name="ntoAT"></a>
## 不要在头文件 `using namespace`


<a name="QQ2We"></a>
### 总结/复习
网盘项目 基于HTTP协议

<a name="pTB23"></a>
#### 用户 
/user/signup   GET 静态资源<br />/usr/signup POST<br />1、解析请求  2、插入数据库  3、重定向<br />/user/signin   POST <br />1、解析请求 2、查询数据库  3、生成token<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657933787824-badec6ef-d2f1-4c87-a929-fc618ac31dc3.png#clientId=ufd822bcb-56ed-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=84&id=u99c68a55&margin=%5Bobject%20Object%5D&name=image.png&originHeight=116&originWidth=915&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22683&status=done&style=none&taskId=ucdc7e45d-6ce7-4c37-8755-0b7f7e13314&title=&width=665.4545454545455)<br />/user/info POST <br />1、解析，得到username和token  2、检查token 3、根据用户名查询用户信息

<a name="Q4rIf"></a>
#### 文件  
<a name="gEgF4"></a>
#### /file/upload   POST 

   1. URL的query部分  username=xxx&token=xxx
   1. multipart/form-data
      1. 文件名
      1. 内容

1、解析请求 -> 2、 校验token -> 3、解析form-data  -> 4、保存文件 -> 5、存储信息 （全局文件表 tbl_file   用户文件表 tbl_user_file )<br />/file/query  <br />1、解析请求 -> 2、 校验token -> 3、查询用户文件表 -> 4、返回Json给前端


OSS备份<br />1、upload<br />2、/file/downloadurl 

   - nginx
   - OSS

<a name="R9iGc"></a>
#### 解耦
备份到OSS   与    回复响应  分离

 同步 变成  异步     消息队列 <br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1657934010770-177c990f-dae3-4b88-b1c0-dd931e0e9d5f.png#clientId=ufd822bcb-56ed-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=279&id=u84e8978d&margin=%5Bobject%20Object%5D&name=image.png&originHeight=383&originWidth=637&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35863&status=done&style=none&taskId=u385fe3a5-b592-4238-bced-ec9131d9a2a&title=&width=463.27272727272725)


网络   nginx<br />~~消息   RabbitMQ(Erlang)    Kafka           java   ~~<br />缓存 <br />存储
