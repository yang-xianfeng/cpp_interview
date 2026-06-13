<a name="qXPFK"></a>
## 
<a name="PZgVM"></a>
## 数据库分类

- 关系型的数据库 
   - 学生的信息 学号 姓名 性别 联系方式 语文 数学
   - **Oracle **
   - **MySQL **
   - SQL Server
   - Access
   - SQL lite  
- 非关系型的数据库NoSQL(Not Only SQL) 
   - **Redis** 键值对 key - value 缓存系统 
   - MongoDB 文档 
   - LevelDB 

<a name="bNiKK"></a>
## SQL(Structured Query Language 结构化查询语句)

- DDL（Data Definition Language 数据定义语言）

允许用户定义数据，即创建表、删除表、修改表结构这些操作。通常,DDL由数据库管理员执行

- DML（Data Manipulation Language 数据控制语言）

DML为用户提供添加、删除、更新数据的能力，这些是应用程序对数据库的日常操作。

- DQL（Data Query Language 数据查询语言）

DQL允许用户查询数据，这也是通常最频繁的数据库日常操作。

概念区分：<br />数据库服务器（管理软件） DB Server

- DB Server
- DB  -> 多张 table

<a name="lyLXx"></a>
## 数据库的 备份 和 恢复(需要新建一个空的数据库 )
```sql
// backup
mysqldump -u root -p old>bak

// 两种恢复方法：

create database new;
mysql -u root -p new<bak

create database new;
use new;
source bak;
```


<a name="sconn"></a>
## DDL(Data Definition Language）
查看数据库 ：mysql> show databases;<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1651146097484-6af5465c-ba67-49b5-bbaf-799bc53fdf9c.png#clientId=u2b96946b-0734-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=197&id=u5264e5ba&margin=%5Bobject%20Object%5D&name=image.png&originHeight=245&originWidth=292&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40856&status=done&style=none&taskId=u13576b75-c953-4047-97cc-70832e2fdff&title=&width=235.3636474609375)<br />创建数据库 ：mysql> create database Dbname;<br />删除数据库 ：mysql> drop database Dbname;

<a name="pd2F2"></a>
#### 字符集：
修改数据库字符集：<br />mysql> alter database DbName default chharacter set gbk;<br />字符校对集：<br />mysql> show character set; // 查看数据库支持的字符集<br />mysql> show collation; // 查看相应字符集的校对规则

- utf8_**general_ci**  忽略大小写 
- utf8_**bin**  	不会忽略大小写

查看表中所有列的字符集：<br /> mysql > **show full columns from test_info;**

注意：

1. table 首先会参考所属database的字符集，所以可以在建database时指定字符集 `default character set utf8`；
1. 设定字符集，系统默认设置一个对应的 校对集，也可以自行修改；


mysql常用数据类型<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1651305299419-94754dc8-f4f6-4645-bd86-f77af030d6b9.png#clientId=u5afe0057-d611-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=391&id=u6b650203&margin=%5Bobject%20Object%5D&name=image.png&originHeight=489&originWidth=1060&originalType=binary&ratio=1&rotation=0&showTitle=false&size=47121&status=done&style=none&taskId=u13d044bb-c17b-4d12-ba8c-2b08ee91f0d&title=&width=848)<br />** TIMESTAMP 在进行insert/update 自动记录  **

创建表
```sql
create table tablename{
    field1 datatype,
    field2 datatype,
    ...
};
```

 查看表结构 ：<br />mysql> show create table tName;  <br />mysql> desc tablename;<br /> 修改表结构 

1. 添加列(字段) : mysql> alter table tablename **add** field datatype;
1.  对字段名进行修改: mysql> alter table tablename **change** field1 fied2 datatype;    
1.  对字段名的类型进行修改: mysql> alter table tablename **modify **field datatype;

使用modify修改field的相对位置：

   - mysql> alter table tablename **modify **field1 datatype1  first;
   - mysql> alter table tablename **modify **field1 datatype1  after field2;
4. 删除一个字段: mysql> alter table tablename **drop** field;

 删除表结构 : mysql> drop table tName;  

清空表数据（保留表结构） ：mysql> truncate table Tname;

重命名 ： rename

<a name="J1bPH"></a>
##  DML(Data Manipulation Language) 

1. 在表中插入记录   **insert** 
1. 修改某些列的数据    ** update **
1. 删除某一些数据     **delete **

在表中插入数据

1. 对**指定列**进行数据的添加 **一行**<br />• insert into TName(field1, field2,...) values(fiedl1Value, field2Value,...);
1. 对**所有列**都进行数据的添加 **一行**<br />insert into TName values(field1Value, field2Value, ...)
```sql
MySQL命令行清屏操作: Ctrl + l
```

在表中插入多条数据 （ 效率是要高于每次都使用一条insert语句  ）

1. 对指定列进行数据的添加 (多行)
```sql
insert into TName(field1, field2,...) 
    values(fiedl1Value, field2Value)，
    (filed1Value, field2Value)，
    ...
    ...;
```

2. 对所有列都进行数据的添加 （多行）
```sql
insert into TName values(field1Value, field2Value, ...)
    (filed1Value, field2Value),
    ...
    ...;
```

修改数据 <br />update tName set field1=xxx [Where ...] 

- 带where子句的只作用于相应行；
- 不带where子句，作用于所有行  

 复制表 

1. 复制表结构（**并不复制数据**） 

create table newTName like oldTNa  

2.  复制表结构和数据 

create table newTName select * from old  

删除表中的数据 <br />delete from TName [Where condition];  

<a name="QtzI1"></a>
## DQL(Data Query Language)
查询命令 
```sql
select [*] |{field1, field2,...} from TName 
[where condition] 
[Order by field];  
```

**显示**时**去除**重复的数据 （ 使用 **distinct** 关键字 ）

- 当distinct作用于单个字段时，显示时去除重复的列即可 
- 当distinct作用于多个字段时，显示时表示的是多个字段都相同时，才会去除
- distinct关键字必须要放在**第一个字段**前面，否则会报错。  

<a name="lhHpU"></a>
###  select的表达式 
select语句选择的列可以进行运算<br />使用as还可以对某些列取别名  

select 语句中出现的** 列 **不一定真的存在数据表中<br />相关接口：<br />mysql > select database();<br />mysql > select  name, chinese + 10 as chinese, curdata(） from student ；<br />mysql > select  curdata( );

<a name="U9Zik"></a>
#### where子句

- 比较运算符 ：where   >  /  =   /  <
- 范围查找： where  between ...  and ...
- 枚举： where  in ( val1, val2, ... )
- 模糊查询 where  like :     _  任意一个字符        %  0个或多个字符
- 判空查询： where  **is(不能直接用 =) **null

order by field : 默认情况下是**升序**排序

- ASC    升序
- DESC  降序

先使用第一个field排序，相同再使用后一个field排序，以此类推<br />select * from student order by math, english, chinese[asc/desc]

按总成绩进行降序<br />mysql -> select id, name, chinese + english + math as total from student  order by total DESC;

<a name="XkmHi"></a>
###  ！分页查询 limit   常考  ( Oracal   sock? )
limit num      一页几行数据

偏移量 与 查看行数<br />limit  num1 num2    从num1开始（不含第num1行）继续查看num2行<br />limit  num1 offset num2     从num2开始不含第num2行）查看num1行


约束 ：<br />非空约束 : not  null<br />保证数据完整性：

<a name="WxRgp"></a>
#### 三种数据完整性：

1. 实体完整性：表中的每一行数据都是唯一的，不能重复出现，
   - 通过**主键**实现 primary key
```sql
mysql> create table Student (
    -> s_id int,
    -> s_name varchar(20),
    -> s_birth datatime,
    -> s_sex varchar(6));

alter table Student add primary key(s_id);
```

   - 设置字段自动增长： auto_increment

注意： **主键**必须设置 **AUTO_INCREMENT**

删除主键约束：<br />一般情况下，一张表只有一个主键<br />需要先解除 自动增长 约束，才能 删除 primary key

   1. alter table tablename **modify** field datatype;
   1. alter table tablename **drop** primary key;

2. field（域）完整性： 每一列必须要符合某种特点的数据类型或约束
   - not null   非空约束
   - unique   唯一约束，不允许重复，**允许为空**
      - 删除唯一约束  
         - 先获取唯一约束的名字，然后drop
         - alter table tablename  drop ** INDEX **filedname
3. 参照完整性
   - foreign key  外键约束   : **外键 **是另一张表的 **主键**
- 表已经存在的情况下，需要使用alter
```sql
alter table tablename     
    add consteraint fk_1 foreign key (s_id) feferences student(id);
      
```

- 表不存在的情况下，设置外键
```sql
creat table tablename ( id int auto_increment primary key,
                       p_name varchar(20),
                       s_id int not null,
                       foreign key(s_id) references student(id)
                       );
```

删除外键

1. 先查找外键的名字
1. 直接删除
```sql
1. 找到：
consteraint 'torder_ibfk_1' foreign key ('s_id') references 'student' ('id')
2. 删除
alter table torder drop foreign key torder_ibfk_1;
```

补充：
```sql
ALTER TABLE students
  ADD CONSTRAINT fk_class_id  //外键约束的名称 fk_class_id 可以任意
  FOREIGN KEY (class_id)	 	//FOREIGN KEY (class_id)指定了class_id作为外键
  REFERENCES classes (id);	//REFERENCES classes (id)指定了这个外键将关联到
                              classes表的id列（即classes表的主键）
```

|  | **定义** | **作用** | **个数** |
| --- | --- | --- | --- |
| 主键 | 唯一标识一条记录，不能重复，不允许为空 | 保证数据完整性 | 一个表主键只能有一个 |
| 外键 | 另一表的主键, 外键可以重复, 可以为空值 | 和其他表建立联系 | 一个表可以有多个外键 |
| 索引 | 该字段没有重复值，但可以有一个空值 | 提高查询排序的速度 | 一个表可以有多个唯一索引 |

**主键**是关系表中记录的唯一标识。主键的选取非常重要：

- 主键不要带有业务含义，而应该使用BIGINT自增或者GUID类型；
- 主键也不应该允许NULL；
- 可以使用多个列作为联合主键，但联合主键并不常用。

关系数据库通过**外键**可以实现一对多、多对多和一对一的关系；<br />外键既可以通过数据库来约束，也可以不设置约束，仅依靠应用程序的逻辑来保证。<br />通过对数据库表创建**索引**，可以提高查询速度。<br />通过创建唯一索引，可以保证某一列的值具有唯一性；<br />数据库索引对于用户和应用程序来说都是透明的。<br />[参考：MySQL 主键、外键、索引](https://zhuanlan.zhihu.com/p/64368422)

联合主键<br />为了避免数据冗余<br />没有必要的情况下，我们尽量不使用联合主键，因为它给关系表带来了复杂度的上升。


<a name="wyNMk"></a>
#### DQL复杂查询 
![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1651305453968-322b49ba-f04f-4f09-87bd-a06929955425.png#clientId=u5afe0057-d611-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=664&id=u36e9d558&margin=%5Bobject%20Object%5D&name=image.png&originHeight=830&originWidth=1293&originalType=binary&ratio=1&rotation=0&showTitle=false&size=216201&status=done&style=none&taskId=u096b2863-c1f4-4626-a34a-ff81fffc8d6&title=&width=1034.4)

- 连接查询 涉及到多张表 
   - 交叉连接（笛卡尔积） 
   - 内连接 
   - 外连接
      - 左外连接
      - 右外连接  

1. 交叉连接 :   cross join （ 笛卡尔积 ） ：
- select * from leftTable **cross join** rightTable  ( 笛卡尔积 ）
- select * from leftTable  **jion** rightTable
- select * from leftTable **, ** rightTable  (  隐式写法  ）

2. 内连接：inner join 
-  不加 on子句 的效果与 交叉连接 效果相同
-  +  **on**

select * from person inner join sorder on person.id= sorder.s_id;

3. 外连接

3.1 左外连接： left outer join    **on**<br />左表中的数据全部出现， 当右表中没有与之对应的记录时，全部用 NULL代替。 <br />3.2 右外连接： right outer join    **on**<br />右表中的数据全部出现， 当左表中没有与之对应的记录时，全部用 NULL代替。 

子查询 （ 嵌套查询 ）：

- 在where子句或from子句中又嵌入 ( select语句 )
```sql
select * from person where id in (select  id from person where id < 4) ;

select * from ( select  id, name, score from student where name like 'k%' as k ;
```

- IN 子查询   很多情况下，IN 列表项的值是通过一个子查询得到的：
```c
SELECT * FROM article WHERE uid IN(SELECT uid FROM user WHERE status=0)
在这个 SQL 例子里，我们实现了查出所有状态为 0 的用户（可能是被禁止）的所有文章。
然后将查询结果作为 IN 的列表项以实现最终的查询结果。
 in 后面必须是一个字段列表项。

```


联合查询：union  并集<br />合并两条查询语句的查询结果，**去掉其中的重复数据行**， 返回没有重复数据行的查询结果。
```sql
select * from person where chineese > 80 UNION
select * from person where math > 80 ;
```

报表查询：group by ...    按照...分组, **往往是 为了使用聚合函数**

-  当**分组之后**， 还需要对记录进行过滤，只能使用  having子句（筛选后再选择）
- 不能使用where子句，where子句在**没有分组之前**使用 。
```sql
select count(*)  from student group by chinese;

select count(*) , chinese from student group by chinese;

select count(*) , chinese from student 
       group by chinese
       having chinese > 80 ;
```
count(*)  计数，若重复则递增

整型数据的统计函数：
```sql
select count(*)  from student group by chinese;

select sum( chinese ) from student ;

select avg( math ) from student ;

select max( english ) from student ;

select min( chinese )  from student ;
```

C语言常用接口<br />http://www.mysql.com

```c
mysql_init()  分配成功初始化一个mysql对象

mysql_real_connect() 连接mysql服务器，完成三次握手 

mysql_query() 		对connect结果集查询
mysql_real_query() 	对connect结果集查询 

//返回查询结果集，不会获取数据，mysql_fetch_row() 才真正获取数据
mysql_use_result() 
//返回查询结果集，获取到数据且存储在本地
mysql_store_result() 

mysql_num_row()    获取结果集的行数
mysql_num_fields() 获取结果集的字段数

mysql_fetch_row() 	  获取结果集下一行
mysql_fetch_fields()  获取结果集下一列


mysql_free_result()  释放结果集
mysql_close()        关闭mysql连接
```

C语言测试数据库连接
```c
#include <stdio.h>
#include <mysql/mysql.h>

int main(void){
    MYSQL *conn = NULL;
    char *host = "localhost";
    char *user = "root";    
    char *passwd = "123456";    
    char *db = "class";    
    
    // 1.初始化mysql的连接句柄
    conn = mysql_init(NULL);
    
    // 2.建立连接
    if(mysql_real_connect(conn, host, user, passwd, db, 0, NULL, 0) == NULL){
        printf(" error:%s\n",mysql_error(conn));
        return EXIT_FAILURE;
    }
    // 设置编码字符集
    mysql_query(conn,"set names'utf8'");
    
    
    // 3. 执行查询
    char *query = "select * from Student";
    int ret = mysql_query(conn,query);
    if(ret != 0){
        printf(" error query1:%s\n",mysql_error(conn));
        return EXIT_FAILURE;
    }
    
    // 4. 获取结果集，执行数据
    MYSQL *RES result = mysql_store_result(conn);
    if(result == NULL){
        printf(" error query2:%s\n",mysql_error(conn));
        return EXIT_FAILURE;
    }
    
    int rows = mysql_num_rows(result);
    int cols = mysql_num_fields(result);
    printf("rows:%d,cols:%d\n",rows,cols);    
    
    // 5. 获取每一行数据
    MYSQL_ROW row;
    while(row = mysql_fetch_row(result) != NULL){
        for(int i = 0; i < cols; ++i){
            printf("%10s ",row[i];
        }
        printf("\n");
    }
    
    // 6. 释放结果集，关闭连接
    mysql_free_result(result);
    mysql_close(conn);
                   
    return 0;
}
    
gcc test.c -o test -lmysqlclient
```
