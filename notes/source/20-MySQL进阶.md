
<a name="DBDay01"></a>
## DBDay01

<a name="788c6d30"></a>
### 一、事务
<a name="b59c9e0f"></a>
#### 概念
构成单一逻辑工作单元的操作集合（一组命令的集合）。
<a name="bb7674f6"></a>
#### 性质（ACID）
原子性：事务要么全部不发生，要么全部都发生。<br />一致性：事务开始前后，状态是一致性（事务开始之前，数据库处于一个一致性的状态，事务执行完毕之后，也会处于一个一致性的状态）<br />隔离性：对于任何一对事务Ti和Tj ,在Ti看来， Tj要么在Ti开始之前已经完成，要么在Ti完成之后才开始执行。（事务是串行执行的）<br />与后面的**隔离级别**有关。不可能达到100%隔离。<br />持久性：一个事务成功完成后，它对数据库的改变必须是永久的，即使出现系统故障。

<a name="56c56563"></a>
#### 安装mycli  ( mycli可以自动补全 )
![image-20220610095739097.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860659600-a59f5ff5-96dc-4a86-9acc-bf7deb0ee209.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ubef494c9&name=image-20220610095739097.png&originHeight=719&originWidth=703&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35301&status=done&style=none&taskId=u820fea05-c9d6-4df5-9b06-c0df8770094&title=)

查看数据库表的结构
```sql
mysql> show create table member;

mysql> desc member;
```

查看数据表的行数
```sql
mysql> select count(*) from member;
+----------+
| count(*) |
+----------+
|        6 |
+----------+
1 row in set (0.06 sec)


mysql> select count(1) from member;
```

<a name="6cb7cf9d"></a>
#### 事务的操作命令
```sql
#开启事务
begin/start transaction;

#提交事务  （认为事务执行过程中的操作都执行完成了，并且生效了）
commit

#事务异常断开的时候，事务可以体现原子性，认为事务中的操作都没有发生

#事务的回滚
rollback   #默认会回到开启事务的位置

#回滚点的设置
savepoint  sp1;  #sp1是回滚点名字

#回到执行回滚点
rollback to  sp1;#回滚点的名字
```

<a name="0fb84cd7"></a>
#### 并发与并行的区别
在**同一时刻**，只有一个线程可以运行，并发。<br />在**同一时刻**，多个线程可以同时运行，并行。

<a name="a81eb8be"></a>
### 二、并发可能产生的四个问题
<a name="1a8b1ff5"></a>
#### 1、脏写
脏写是指当多个事务并发写同一数据时，**先执行的事务所写的数据会被后写的数据覆盖**。<br />![image-20220610105016025.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860705266-a641141e-b408-4455-9110-07f899dfd6bb.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u272a0f26&name=image-20220610105016025.png&originHeight=584&originWidth=1127&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57003&status=done&style=none&taskId=uea8dd937-57cd-4b14-9dc1-3b46c0bde35&title=)

<a name="4b9d4e2b"></a>
#### 2、脏读
B事务读取A事务一个**没有提交或者终止**的中间值，所以对于B事务而言，就是脏读。<br />![image-20220610105059619.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860717666-bc291b03-47b8-4b24-a7cf-fcb7472cb3d4.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uf4f1ba6a&name=image-20220610105059619.png&originHeight=569&originWidth=1106&originalType=binary&ratio=1&rotation=0&showTitle=false&size=71702&status=done&style=none&taskId=u1fbfcc78-e52d-4528-9d67-35e7069fa60&title=)

<a name="f7635dd5"></a>
#### 3、不可重复读
一个事务有对同一个数据项的多次读取，但是在某前后两次读取之间，另一个事务**更新该数据项**，并且**提交**了。在后一次读取时，感知到了提交的更新。<br />![image-20220610110058193.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860743949-8e41af7f-ae8b-4442-b8dc-1f905c0d5e1c.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ud48c9f4a&name=image-20220610110058193.png&originHeight=595&originWidth=1193&originalType=binary&ratio=1&rotation=0&showTitle=false&size=68648&status=done&style=none&taskId=ufa310ebe-6628-4c9f-b3c4-97db7c10f46&title=)

<a name="e7cf74b4"></a>
#### 4、幻读
一个事务需要进行前后两次统计，在这两次统计期间，另一个事务插入了新的符合统计条件的记录，并且**提交**了。导致前后两次统计的数据不一致。这种现象，我们称之为幻读。<br />![image-20220610110353679.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860756210-38da01a0-00dd-466c-87a3-de6f9b1e33bd.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u8e63f056&name=image-20220610110353679.png&originHeight=593&originWidth=1190&originalType=binary&ratio=1&rotation=0&showTitle=false&size=79328&status=done&style=none&taskId=u6b3fbb55-2eb2-4b12-bd60-fa1e19985ae&title=)


<a name="41cf8a0c"></a>
### 三、四种不同隔离级别的演示
读未提交、读已提交、可重复读、可串行化。<br />隔离级别越来越高，说明串行能力越来越强，但是并发能力越来越弱

```sql
#查看当前事务的隔离级别
select @@ [session|global] transaction_isolation;
select @@tx_isolation;

#查询当前隔离级别
select @@session.transaction_isolation;

#设置当前隔离级别为读未提交
set session transaction isolation level read uncommitted;

#设置当前隔离级别为读已提交
set session transaction isolation level read committed;

#设置当前隔离级别为可重复读
set session transaction isolation level repeatable read;

#设置当前隔离级别为可串行化
set session transaction isolation level serializable;
```

<a name="2355f851"></a>
#### 1、读未提交
可以避免脏写。<br />![image-20220610111559434.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860778418-88b15a4f-0f33-4d7c-bf76-a0ac436cba45.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u31234e51&name=image-20220610111559434.png&originHeight=632&originWidth=1801&originalType=binary&ratio=1&rotation=0&showTitle=false&size=80707&status=done&style=none&taskId=u34152e16-bec7-41e4-8f51-3d325e55bab&title=)

可以产生脏读<br />![image-20220610111820433.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860790758-19990da4-527c-4673-85d7-7685fce60416.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u4c969495&name=image-20220610111820433.png&originHeight=535&originWidth=1869&originalType=binary&ratio=1&rotation=0&showTitle=false&size=62633&status=done&style=none&taskId=u7b3916d2-2598-4447-8c87-5c492023cf2&title=)<br />既然可以读一个没有提交的数据，不可重复读（前后两次读操作的结果会是不一样的）也是可以直接产生的

可以产生幻读<br />![image-20220610112429836.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860802972-49b65d69-7643-49ae-919d-ff88639cd120.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u52cae240&name=image-20220610112429836.png&originHeight=656&originWidth=1856&originalType=binary&ratio=1&rotation=0&showTitle=false&size=81536&status=done&style=none&taskId=u7d69bd92-917d-41ef-ac57-d4acf70ef70&title=)

![image-20220610112458351.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860825056-f876263b-766e-474d-959f-48e2b978ad15.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ua824147a&name=image-20220610112458351.png&originHeight=386&originWidth=852&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28729&status=done&style=none&taskId=u5c96e335-d5c2-4f91-b2c8-47a71ff8e8a&title=)

<a name="b8ae4e73"></a>
#### 2、读已提交

A 、B都开启事务，A 、B都进行select，此时数据是一致的。

在A 会话更新一条数据，B会话也去更新同一条数据，发现卡死了（不能更新），**避免了脏写**；<br />接着B会话再去进行select操作，发现A会话更新的数据看不到，所以也可以**避免脏读**；<br />接着A会话执行提交操作，然后在B会话进行select，发现A会话更新的数据可以看到，所以对B会话而言，就是不可重复读，就**产生了不可重复读**的现象。

A 、B两边都开启事务，B 进行读数据，在A会话去插入一条数据，并且提交，B会话在进行读，发现多产生了一条数据，对于B会话而言，就是一个**幻读现象**。

<a name="49f99c72"></a>
#### 3、可重复读

**不可以产生脏写、脏读、不可重复读**，但是**幻读是可以产生**的。<br />![image-20220610114752719.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860884495-790ee73f-7d55-4958-b887-377ee4bcc6b6.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ue0890322&name=image-20220610114752719.png&originHeight=598&originWidth=1845&originalType=binary&ratio=1&rotation=0&showTitle=false&size=68196&status=done&style=none&taskId=u8d980a7d-d6e5-4d63-a45d-7fb8618c5ab&title=)

![image-20220610114934629.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860892165-d4fa207f-aa34-40f5-898b-1dda9b1be0b3.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ue407059e&name=image-20220610114934629.png&originHeight=589&originWidth=1849&originalType=binary&ratio=1&rotation=0&showTitle=false&size=97906&status=done&style=none&taskId=u1efffaab-7c5e-40a4-80ac-4c2fe308a8e&title=)<br />此时，没有显示幻读，但是实际插入发现表中暗含新增数据，这是特殊的幻读，因为数据库隐藏了。

<a name="b51af01e"></a>
#### 4、可串行化
![image-20220610143700826.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654860897717-8c2b5142-8215-46b2-a2d8-a8ba28146cb6.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ubdb5b2e1&name=image-20220610143700826.png&originHeight=733&originWidth=1881&originalType=binary&ratio=1&rotation=0&showTitle=false&size=92215&status=done&style=none&taskId=ud7120d7e-aae9-49dc-8b21-ae3443bbd6d&title=)<br />此时已经不允许其他事务写操作了，此时所有的问题都能得到解决。

|  | 脏写 | 脏读 | 不可重复读 | 幻读 |
| --- | --- | --- | --- | --- |
| read uncommitted | × | √ | √ | √ |
| read committed | × | × | √ | √ |
| repeatable read | × | × | × | √ |
| serializable | × | × | × | × |

以上所有隔离级别都不允许脏写(dirty write)，即如果有一个数据项已经被另一个尚未提交或中止的事务写入，则该事务不能对该数据项执行写操作。

注意：<br />MySQL 支持4种隔离级别，默认为 RR (repeatable read)，MySQL的RR隔离级别，在一定程度上避免了幻读问题;<br />Oracle 只支持 read committed 和 serializable 两种隔离级别，默认为 read committed.


<a name="21573afa"></a>
### 四、索引
<a name="46b032ab"></a>
#### 1、概念
索引（Index）是帮助MySQL**高效获取数据**的**数据结构**

<a name="964c7a64"></a>
#### 2、索引使用的数据结构

**磁盘**`**I/O**`**读取次数  约等于 比较次数。**

顺序存储：需要大段连续的空间。时间复杂度O(N)。<br />二分查找：时间复杂度O(logN)。需要大段连续的空间。<br />二叉树：时间复杂度O(logN)，不需要连续的空间，树的高度是比较高的。此时将索引加载到内存，需要进行多次的磁盘IO，而磁盘IO的速度是比较慢的。<br />哈希表：时间复杂度比较低O(1)，不需要连续的空间。哈希会有哈希冲突，哈希不利于范围查找。<br />B树：结点中需要存索引与value值，还要存指针的大小，所以会在一定程度上会限制一个节点中存放索引的数目，会增加树的高度，从而增加磁盘IO的次数。<br />B+树：节点中不存放value值，在某种程度上面，可以将一个节点中的索引的数目存储的更多，可以降低树的高度，从而减少磁盘IO的次数。

考虑的几个维度：时间复杂度、内存的要求（是不是需要连续空间）、磁盘IO的次数、范围查找

```sql
#查看一个节点的大小
mysql> show variables like 'innodb_page_size';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| innodb_page_size | 16384 |
+------------------+-------+
1 row in set (0.04 sec)

```

**一般情况下，索引底层使用的是B+树。**


<a name="81eacd72"></a>
#### 3、B+树的特点

- 非叶子节点不存储data，只存储key
- 所有的叶子节点存储完整的一份key信息以及key对应的data ( 可以是一条完整的数据或者是该条数据对应的地址值 )
- 每一个父节点都出现在子节点中，是子节点的最大或者最小的元素
- 每个叶子节点都有一个指针，指向下一个节点，形成一个链表

数据是存在磁盘上面了，如果建立的索引之后，会产生索引树（B+），也是存在磁盘上面。用索引进行查询的时候，需要将索引树加载到内存中，树的高度等同于磁盘IO的次数。

<a name="7a7e69d5"></a>
#### 4、索引的分类
主键索引：以主键建立的索引，称为主键索引。<br />非主键索引：以非主键建立的索引，非主键索引。唯一索引、普通索引、全文索引、组合索引。<br />索引往往使用 ` a_b_c ` 命名。

<a name="5151f442"></a>
#### 5、索引的创建
```sql
#查看表的索引
show index from member;
```

<a name="ea0453b6"></a>
##### 主键的创建
特点：主键是唯一的，并且不能为空。
```sql
#创建表以及表的列（此时是没有主键）
mysql> create table test1 (id int, age int, name char(20));
Query OK, 0 rows affected (0.08 sec)

#再用alter给表创建主键
mysql> alter table test1 add primary key(id);
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql>


#在创建表的同时，创建主键
mysql> create table test2 (id int, age int, name varchar(20), primary key(id));
Query OK, 0 rows affected (0.02 sec)

mysql>
```

<a name="6285aadb"></a>
##### 唯一索引的创建
该列的值是唯一的，可以为空。
```sql
mysql> create unique index age_idx on test2(age);
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> 

#也可以使用alter的方法进行创建
```

<a name="a251e21d"></a>
##### 普通索引
该列没有什么特殊要求
```sql
mysql> create index age_idx on test2(age);
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> 

#也可以使用alter的方法进行创建
```

<a name="c2c483dd"></a>
##### 组合索引
由多个列组成索引
```sql
mysql> create index name_math_idx on test3(name, math);
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql>  show create table test3;
test3 | CREATE TABLE `test3` (
  `id` int(11) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `math` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name_math_idx` (`name`,`math`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

mysql>
```

<a name="509f555a"></a>
#### 6、索引的删除
```sql
#删除索引的方法1
ALTER TABLE table_name DROP INDEX index_name;
ALTER TABLE test3 DROP INDEX name_math_idx;

#删除索引的方法2
DORP INDEX IndexName ON TableName;
DORP INDEX name_math_idx ON test3;
```

<a name="bd255bb1"></a>
#### 7、最左前缀
对于组合索引而言，查询的时候有可能用不到索引。每次进行查询的时候，在查询条件中需要把组合索引最左边的列带上，不然查询的时候就用不到索引。<br />![image-20220610164358544.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654862323946-c1e03960-526f-44e8-9af3-ac4146bb18a7.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u922f5770&name=image-20220610164358544.png&originHeight=432&originWidth=1102&originalType=binary&ratio=1&rotation=0&showTitle=false&size=62955&status=done&style=none&taskId=u50388775-c26c-4076-957b-1de48df9daf&title=)

<a name="98f00535"></a>
#### 8、索引的好处与坏处
好处：<br />提高数据检索的效率，降低数据库的IO成本

坏处：<br />1、索引也会占用空间<br />2、更新索引也会花费时间

索引不是越多越好，要控制在合理范围（ 4 ~ 5个 ）。

<a name="fb433d3d"></a>
### 五、逻辑架构
```sql
#查看数据库的版本
mysql> select version();
+-------------------------+
| version()               |
+-------------------------+
| 5.7.37-0ubuntu0.18.04.1 |
+-------------------------+
1 row in set (0.00 sec)

mysql>
```

大体来说，MySQL可以分为 **Server 层和存储引擎层**。<br />Server 层包括连接器、查询缓存、解析器、优化器和执行器等，涵盖了 MySQL 大多数核心服务功能。

存储引擎层负责**数据的存储和提取**。其架构模式是插件式的，支持 InnoDB、MyISAM、Memory 等多个存储引擎

<a name="da15be97"></a>
### 六、存储引擎
存储引擎层负责**数据的存储和提取**,插件式的，即插即用
```sql
# 查看MySQL支持哪些存储引擎
SHOW ENGINES;

# 查看默认存储引擎
SHOW VARIABLES LIKE ‘%storage_engine%’;
```

<a name="eb6ad7dc"></a>
#### MyISAM存储引擎
MySQL 5.5 之前默认的存储引擎。<br />特点：<br />a. 查询速度很快<br />b. **支持表锁**<br />c. 支持全文索引(正排索引、倒排索引)<br />d. **不支持事务**

粒度

使用 MyISAM 存储表，会生成三个文件.<br />.frm # 存储表结构，是任何存储引擎都有的<br />.myd # 存放数据<br />.myi # 存放索引

<a name="52320c72"></a>
#### InnoDB存储引擎
MySQL 5.5 以及以后版本默认的存储引擎。没有特殊应用，推荐使用InnoDB引擎。<br />特点：<br />a. **支持事务**<br />b. 支持**行锁**和表锁（默认支持行锁）<br />c. 支持MVCC(多版本并发控制)<br />d. 支持崩溃恢复<br />e. 支持外键一致性约束

使用 InnoDB 存储表，会生成两个文件.<br />.frm # 存储表结构，是任何存储引擎都有的<br />.ibd # 存放数据和索引<br />![image-20220610175916397.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654862379891-aec032d6-45d0-45af-82bb-7c6133734f86.png#clientId=u0e59dea5-33de-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u60285af4&name=image-20220610175916397.png&originHeight=254&originWidth=1075&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29380&status=done&style=none&taskId=u643284d7-0f46-4976-a07f-7b30de42fd1&title=)<br />`mysql`文件 ： `/ var/ lib / mysql /`

<a name="501acedb"></a>
#### 从结构划分索引类型
索引和数据是分开存放的，这样的索引叫**非聚集索引**<br />索引和数据存放在一起，这样的索引叫**聚集索引**。


<a name="1cbed4ee"></a>
#### memory存储引擎

特点：<br />a. 所有数据都存放在**内存**中，因此数据库重启后会丢失<br />b. 支持表锁<br />c. 支持Hash和BTree索引<br />d. 不支持Blob（大的二进制信息）和Text（支持的是大文本）字段

<a name="8a9cdde9"></a>
#### 存储引擎是memory表与临时表的区别

```sql
#临时表的创建
mysql> create temporary table test1 (id int, age int, name varchar(20), primary key(id));
Query OK, 0 rows affected (0.04 sec)

mysql>
#特点，创建完成之后，看不到表的名字；
#默认的存储引擎还是InnoDB;
#可以进行正常的SQL（insert、update、delete、select）；
#只会存在于当前会话，当会话关闭之后，临时表就消失了。


#存储引擎是memory的表
mysql> create table test2 (id int, age int, name varchar(20), primary key(id)) ENGINE=memory;

#存储引擎是memory的表，在创建之后，可以使用show tables看到表的名字；
#仅仅是存储引擎被指定为memory；
#也是可以进行正常的SQL语句（insert、update、delete、select）的；
#关闭当前会话，存储引擎是memory可以进行正常的SQL操作；
#断电重启之后，存储引擎是memory中的数据丢失。
```

<a name="5a068227"></a>
### 三者drop、delete、truncate的区别

1、drop可以删除数据库或者表，删除之后，数据库是不存在，删除表的时候，会将表中内容与结构都删除。<br />2、delete只能删除表中的数据，删除的时候是一条一条数据的删除。<br />3、truncate可以删除表中的数据，可以一次将数据与结构全部删除，然后在重新生成表以及表的结构，等价执行truncate时候，先执行drop命令，然后执行create

<a name="f637ae4c"></a>
#### 外键

一个表A的某列是关联到另外一个表B的主键。<br />![image-20220611101931301.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654947372452-3bc9cf71-fb82-48b5-8bf3-60220b4d548a.png#clientId=uf92f8c2f-1624-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u05880306&name=image-20220611101931301.png&originHeight=399&originWidth=1291&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35927&status=done&style=none&taskId=ub02356f5-62f9-47ed-8374-4e8e00df015&title=)

![image-20220611101857325.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654947409623-2caa97fc-93bb-49b4-8bad-e98a84ea6d60.png#clientId=uf92f8c2f-1624-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u7beb8850&name=image-20220611101857325.png&originHeight=284&originWidth=1885&originalType=binary&ratio=1&rotation=0&showTitle=false&size=80779&status=done&style=none&taskId=ue1511ca2-df1d-463c-a337-c3a3e7ada62&title=)

<a name="82d60153"></a>
#### 不同存储引擎的特征
| 功能 | MyISAM | MEMORY | InnoDB |
| --- | --- | --- | --- |
| 存储限制 | 256TB | RAM | 64TB |
| 支持事务 | × | × | √ |
| 支持全文索引 | √ | × | √ |
| 支持树索引 | √ | √ | √ |
| 支持Hash索引 | × | √ | √ |
| 支持数据索引 | × |  | √ |
| 支持外键 | × | × | √ |


![image-20220611110358073.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654947390101-4fa14186-eb5c-4427-bbb9-48de3a0a5df8.png#clientId=uf92f8c2f-1624-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u874ac0e8&name=image-20220611110358073.png&originHeight=468&originWidth=1819&originalType=binary&ratio=1&rotation=0&showTitle=false&size=81147&status=done&style=none&taskId=u0f8c3b42-0113-4528-8834-70fe16411b4&title=)

<a name="DBDay02"></a>
## DBDay02
<a name="9e17ecdb"></a>
### 一、问题回顾
1、事务的四大基本特征是什么？<br />ACID<br />2、事务的常用命令有哪些？<br />begin/start transaction   commit    rollback  savepoint<br />3、什么是脏写、脏读、不可重复读、幻读？

4、索引的基本概念是什么？<br />提高查询速率  数据结构<br />5、索引的底层数据结构是用什么？<br />B+<br />6、索引的分类？有哪些类型的索引？索引如何查询、创建、删除？

7、最左前缀是什么，怎么理解？

8、MyISAM存储引擎的特点是什么？InnoDB存储引擎的特点是什么？

9、什么是聚集索引，什么是非聚集索引？

<a name="c3b62441"></a>
### 二、锁机制
<a name="812b2f53"></a>
#### 锁的分类
从对数据操作的**粒度**划分：（粒度可以看成是范围）<br />表级锁：开销小，加锁快；不会出现死锁；锁定粒度大，发生锁冲突的概率最高，并发度最低。<br />行级锁：开销大，加锁慢；会出现死锁；锁定粒度最小，发生锁冲突的概率最低，并发度也最高。

从对数据操作的类型划分：<br />读锁（共享锁）：同一份数据，多个读操作可以同时进行而互不影响。<br />写锁（排它锁）：当前操作没有完成之前，它会阻断其他读锁和写锁。

<a name="51030f8c"></a>
#### MyISAM的表锁
```sql
lock table 表名  read; (加读锁)
lock table 表名  write; (加写锁)
```
1、读与读之间是共享的，但是读与写之间是不能同时存在的（对一张表加了读锁之前，其他的所有写操作都是不允许）<br />![image-20220611110358073.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654947504308-7d07a7c3-609a-47a7-998e-682aa202cfbe.png#clientId=uf92f8c2f-1624-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u862391a4&name=image-20220611110358073.png&originHeight=468&originWidth=1819&originalType=binary&ratio=1&rotation=0&showTitle=false&size=81147&status=done&style=none&taskId=u2e26e712-c974-41d2-b0d6-c684cffef05&title=)

2、某个会话，对某个表加了读锁之后，不允许该会话读其他的表。<br />![image-20220611110900629.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654947517333-53554528-9e1f-4df6-aafe-e2b9deb161dc.png#clientId=uf92f8c2f-1624-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u6787f5c1&name=image-20220611110900629.png&originHeight=98&originWidth=918&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8159&status=done&style=none&taskId=ubf13342f-05ba-46cb-8233-41cbb457412&title=)

如果想读其他的表，可以先将其他表进行锁定，然后在去进行读操作<br />![image-20220611111046652.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654947523286-30bbae3c-1ff3-414d-a840-af79b94b04b0.png#clientId=uf92f8c2f-1624-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uad0a16ad&name=image-20220611111046652.png&originHeight=486&originWidth=831&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27744&status=done&style=none&taskId=u983f54e4-5e4b-4c7b-acea-a315eeb9200&title=)

3、读与读之间的共享<br />![image-20220611111515039.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654947535238-39abd2e4-41a8-4fa0-9113-c4871fe9f671.png#clientId=uf92f8c2f-1624-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u725fe480&name=image-20220611111515039.png&originHeight=514&originWidth=1593&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67052&status=done&style=none&taskId=u213a79f4-5437-48b5-8ce9-576863a0c97&title=)

![image-20220611111803739.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654947542366-7a18fd56-ec53-40f9-b041-ccd8b04aae97.png#clientId=uf92f8c2f-1624-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u035acfdb&name=image-20220611111803739.png&originHeight=185&originWidth=1397&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21086&status=done&style=none&taskId=u760dbcb4-37b2-4fc9-a849-7959c6f27c7&title=)

4、对某张表加了写锁之后<br />![image-20220611112306301.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654947560038-eaefb8e0-98fc-41b8-9c19-ead88e474b55.png#clientId=uf92f8c2f-1624-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ub6aa6c91&name=image-20220611112306301.png&originHeight=643&originWidth=1569&originalType=binary&ratio=1&rotation=0&showTitle=false&size=107805&status=done&style=none&taskId=u64eb0b4c-6008-4b83-bdd0-790c27b0948&title=)

总结：读与读之间是属于共享的，不存在更改；但是写锁是属于排他的，不允许写与读或者写与写同时存在。

<a name="4e44a7ac"></a>
#### InnoDB行锁
```sql
SELECT ... LOCK IN SHARE MODE;
SELECT ... FOR UPDATE;
```
innoDB是行级锁，每次锁的单位是行，所以不论对改行加读锁还是写锁，其他事务都是可以对其他行加读锁或者写锁，或者读其他行或者写其他行。

<a name="4d38bbae"></a>
#### 间隙锁
![image-20220611114851453.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654947575805-5093e9b9-b20a-49ce-af12-814d91bdf8b5.png#clientId=uf92f8c2f-1624-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u6ee4cd60&name=image-20220611114851453.png&originHeight=418&originWidth=1877&originalType=binary&ratio=1&rotation=0&showTitle=false&size=95921&status=done&style=none&taskId=ubfc6c318-fe62-42ba-a036-08761520006&title=)<br />原理：还是读锁与写锁之间是不能共存的，是排斥的。


InnoDB的共享锁和排他锁都只有在事务中才生效，为什么会这样？<br />innoDB是支持事务的，事务具有原子性，你的select操作在执行时相当于加了读锁，update,insert,delete在执行的时候相当于加了写锁，所以每一步是原子的，如果不用事务来演示，那执行完成后整个命令就结束了，而如果用了事务，开启事务后加锁，只要没有提交，那么就等同于该操作还没结束，一直对某行加锁，那么其他事务在写该行时，锁还没释放，当然就不能写了。



<a name="DBDay03"></a>
## DBDay03

<a name="oqrsr"></a>
### 一、问题回顾
1、锁的分类？MyISAM的表锁？InnoDB的行锁？间隙锁？

<a name="ec5d6aad"></a>
### 二、业务设计（了解）
<a name="db2a2830"></a>
#### 1、逻辑设计
<a name="87a85787"></a>
##### 范式设计
范式：就是设计数据库的时候的**规则**<br />第一范式：保证每一列都是原子的。<br />第二范式：确保表中的每一列都与主键相关。<br />第三范式：确保每列都和主键列直接相关,而不是间接相关

范式化设计的优缺点：<br />优点：<br />1）可以尽量得减少数据冗余<br />2）范式化的表通常比反范式化的表更小<br />3）范式化的数据库更新起来更加快；<br />不足：<br />1）范式化的表，在查询的时候经常需要很多join关联,增加让查询的代价。<br />2）更难进行索引优化

<a name="a035217d"></a>
##### 反范式设计
允许存在**少量得冗余**，换句话来说反范式化就是使用**空间来换取时间**

反范式化设计的优缺点：<br />优点：<br />1）可以减少表的关联<br />2）可以更好的进行索引优化<br />缺点：<br />1）存在数据冗余及数据维护异常<br />2）对数据的修改需要更多的成本

范式设计与反范式设计没有绝对的，需要根据具体的需求进行选择，如果表的更新非常频繁的话，此时尽量满足范式设计，因为范式的表往往比较简单，更新起来比较容易；如果表更多的在与查询的时候，而不是更新，此时可以尽量满足反范式设计，减少连表查询的消耗。

<a name="b02bcc13"></a>
#### 2、物理设计
命名规范、存储引擎选择、数据类型选择

<a name="f81833ab"></a>
### 三、索引再探（重点）
主键索引：以主键作为的索引。<br />非主键索引（辅助索引）：不是以主键作为的索引，普通索引、唯一索引、全文索引、组合索引。<br />聚集索引（聚簇索引）：数据与索引是存在一起的，InnoDB为例，两个文件，frm 和ibd<br />非聚集索引（非聚簇索引）：数据与索引是分开存放的，MyISAM为例，三个文件frm、myd、myi

如果是InnoDB，再去以主键或者非主键创建索引。

如果**存储引擎是InnoDB的表**，并且是以主键创建的索引树，就会在叶子结点下面存放该条数据的完整信息。

如果是以非主键创建的索引树，就会在叶子结点下面存放对应主键索引，就不会将该条数据的完整信息全部存在辅助索引树上。

如果**存储引擎是MyISAM的表**，不管是以主键创建的主键索引树还是以非主键创建的索引树，在叶子结点里面存放的都是该条数据对应的地址值。

对于InnoDB存储引擎而言，如果在辅助索引树上进行查找某些列，并且在辅助索引树上找到了该列，那么就是称为**索引覆盖**；如果在辅助索引树上查找某些列A、B，这些列在辅助索引树上找不到，此时可以在辅助索引树上找到对应的主键，然后通过主键索引树找到那些列A、B，这称为**回表**。

```sql
id(primary key)   age  name   phone  address      #InnoDB

#创建辅助索引    age（index）      name（index）
#age（index）辅助索引树 叶子结点下会存主键id
select name from member where  age = 10;;  #回表
select address from member where  age = 10;;  #回表,辅助索引树，主键索引树
select address from member where age = 10;  #回表,辅助索引树，主键索引树
select * from member where age = 10;  #回表,辅助索引树，主键索引树
select age from member where  age = 10;; #索引覆盖
select id from member where  age = 10;; #索引覆盖
select age,id from member where  age = 10;; #索引覆盖

#name（index）辅助索引树 叶子结点下会存主键id
select name from member where  name = 'wangdao';  #索引覆盖
select id from member where  name = 'wangdao';  #索引覆盖
select name,id from member where  name = 'wangdao';  #索引覆盖
select age from member where  name = 'wangdao';  #回表
select phone from member where  name = 'wangdao';  #回表
select phone,id from member where  name = 'wangdao';  #回表
```

<a name="a1d6876a"></a>
### 四、慢查询日志

就是记录了查询比较慢（执行时间长）的SQL的日志。

```sql
#查询慢查询日志的时间
mysql> show variables like 'long_query_time';
+-----------------+-----------+
| Variable_name   | Value     |
+-----------------+-----------+
| long_query_time | 10.000000 |
+-----------------+-----------+
1 row in set (0.00 sec)

#查询慢查询日志的相关信息（慢查询日志的开关、对应的文件名字与路径）
mysql> show variables like '%slow%';
+---------------------------+---------------------------------+
| Variable_name             | Value                           |
+---------------------------+---------------------------------+
| log_slow_admin_statements | OFF                             |
| log_slow_slave_statements | OFF                             |
| slow_launch_time          | 2                               |
| slow_query_log            | OFF                             |
| slow_query_log_file       | /var/lib/mysql/wangdao-slow.log |
+---------------------------+---------------------------------+
5 rows in set (0.00 sec)

ERROR: 
No query specified

mysql>
```

<a name="76984737"></a>
### 五、执行计划（重点）

可以查看官方文档：

mysql.com->[DOCUMENTATION](https://dev.mysql.com/doc/)->[MySQL 5.7 Reference Manual](https://dev.mysql.com/doc/refman/5.7/en/)->[Optimization](https://dev.mysql.com/doc/refman/5.7/en/optimization.html)->[Understanding the Query Execution Plan](https://dev.mysql.com/doc/refman/5.7/en/execution-plan-information.html) ->[EXPLAIN Output Format](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html)

| **Column** | **JSON Name** | **Meaning** |
| --- | --- | --- |
| [id](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_id) | select_id | The SELECT identifier |
| [select_type](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_select_type) | None | The SELECT type |
| [table](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_table) | table_name | The table for the output row |
| [partitions](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_partitions) | partitions | The matching partitions |
| [type](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_type) | access_type | The join type |
| [possible_keys](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_possible_keys) | possible_keys | The possible indexes to choose |
| [key](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_key) | key | The index actually chosen |
| [key_len](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_key_len) | key_length | The length of the chosen key |
| [ref](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_ref) | ref | The columns compared to the index |
| [rows](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_rows) | rows | Estimate of rows to be examined |
| [filtered](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_filtered) | filtered | Percentage of rows filtered by table condition |
| [Extra](https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain_extra) | None | Additional information |



可以使用explain + SQL语句。<br />![image-20220613145200779.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655122625555-909265c7-8341-4e4d-9f7f-2fd98d7ddb5d.png#clientId=u175d98d2-db7a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uc847a2a8&name=image-20220613145200779.png&originHeight=278&originWidth=1599&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18505&status=done&style=none&taskId=ua5d2fdf8-6003-4ed5-9728-361d4c25af0&title=)

![036d1593-e394-4e1c-b2c6-475844fe46b0.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655122660934-46826415-1f86-477d-8dc6-2dafc065aa1b.png#clientId=u175d98d2-db7a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u0948cf62&name=036d1593-e394-4e1c-b2c6-475844fe46b0.png&originHeight=615&originWidth=826&originalType=binary&ratio=1&rotation=0&showTitle=false&size=97599&status=done&style=none&taskId=u267afca1-b100-4185-81dd-ebfe225a6dc&title=)

<a name="459c66df"></a>
#### 1、id列
从id的大小，可以判别那张表先执行，那张表后执行，间接可以推测出SQL的执行顺序。

规则：当id相同的时候，从上向下依次执行；当id不同的时候，先执行id大的对应的表，然后在执行id小的对应的表；当id既有相同也有不同的时候，先执行id大的对应的表，然后在id相同情况下，从上往下执行。

![image-20220613151232790.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655122703949-defb622b-6166-4832-a17b-a46b902c257e.png#clientId=u175d98d2-db7a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u20a170a4&name=image-20220613151232790.png&originHeight=540&originWidth=1540&originalType=binary&ratio=1&rotation=0&showTitle=false&size=112910&status=done&style=none&taskId=u6ec7110b-761b-4361-bad5-01e5cc8383e&title=)

![image-20220613151359289.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655122717849-f8b80d69-35a2-40a2-ae1d-78b1090a2248.png#clientId=u175d98d2-db7a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u20cd601f&name=image-20220613151359289.png&originHeight=408&originWidth=1602&originalType=binary&ratio=1&rotation=0&showTitle=false&size=111734&status=done&style=none&taskId=ub2ff7c65-da43-40c7-a5a8-bf2a40a1353&title=)

<a name="nrBiZ"></a>
#### 2、select_type
![image-20220613151933558.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655122780150-1976fc80-bd78-4125-a26c-6d7bb501e681.png#clientId=u175d98d2-db7a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u2cf9b079&name=image-20220613151933558.png&originHeight=471&originWidth=1031&originalType=binary&ratio=1&rotation=0&showTitle=false&size=112060&status=done&style=none&taskId=udff8d07c-c4b4-4610-bd46-068c75e8790&title=)

<a name="45fb22e5"></a>
#### 3、type列（最重要）
用到索引的类型与等级<br />system > const > eq_ref > ref > range > index > ALL


主键索引   eq_ref及以上<br />普通索引   ref及以下

<a name="XR9xK"></a>
#### 总结：
system 最快：不进行磁盘 IO<br />const：PK 或者 unique 上的等值查询<br />eq_ref：PK 或者 unique 上的 join 查询，等值匹配，对于前表的每一行，后表只有一行命中<br />ref：非唯一索引，等值匹配，可能有多行命中<br />range：索引上的范围扫描，例如：between、in、><br />index：索引上的全集扫描，例如：InnoDB 的 count<br />ALL 最慢：全表扫描

<a name="2670175a"></a>
#### 4、possible_keys、key、ken_len

possible_keys：可能用到的索引<br />key：实际用到的索引<br />ken_len：用到索引的最大可能长度

- 每个字符占用的字节：utf8mb4=4,utf8=3,gbk=2,latin1=1 ;
- varchar会额外占用两个字节大小;
- NULL会额外占用一个字节大小。

`**key_len = n (utf8mb4=4,utf8=3,gbk=2,latin1=1) + 1(NULL)/0(not NULL) + 2（varchar）/0(char)**`

**datetime类型在5.6中字段长度是5个字节，datetime类型在5.5中字段长度是8个字节**
<a name="pf4P3"></a>
#### <br />
```sql
#查看当前表是属于哪个数据库
mysql> select database();
+------------+
| database() |
+------------+
| xxx        |
+------------+
1 row in set (0.00 sec)



#查看当前数据库版本
mysql> select version();
```

<a name="4e539020"></a>
#### 5、extra
![image-20220613171058478.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655123106530-e1765955-f63c-4259-839c-c6e85ec7fc18.png#clientId=u175d98d2-db7a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ub5cf957e&name=image-20220613171058478.png&originHeight=643&originWidth=888&originalType=binary&ratio=1&rotation=0&showTitle=false&size=136610&status=done&style=none&taskId=ufcb83676-5dfe-4570-b4a8-767d48386a4&title=)

![image-20220613171424927.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655123111821-b801f32a-95e7-4362-80b5-682f0329af7e.png#clientId=u175d98d2-db7a-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u0d21d241&name=image-20220613171424927.png&originHeight=623&originWidth=960&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36863&status=done&style=none&taskId=u4ea56912-05f4-438e-b96d-da09bbca726&title=)

<a name="999618e9"></a>
### 六、索引失效

```sql
insert into student values (6, '19',34, '19', '19', '19', '2015-02-12 10:10:00');

show create table student;
#索引优化
#1、不在索引列上做任何操作（计算，函数等等），会导致索引失效
explain select * from student where id = 3;
explain select * from student where id + 1 = 4;

#2、慎用不等于号，会使索引失效
show create table student;
explain select * from student where c1 =  'wuhan';
explain select * from student where c1 <> 'wuhan';#回表
explain select c1 from student where c1 <> 'wuhan';
explain select c1,c2 from student where c1 <> 'wuhan';

explain select * from student where c1 > 'wuhan' or c1 < 'wuhan';
explain select c1 from student where c1 > 'wuhan' or c1 < 'wuhan';
explain select c1 from student where c1 > 'wuhan' UNION 
 select c1 from student where c1 < 'wuhan';

#3、存储引擎不能使用索引中范围条件右边的列
explain  select * from student where c1 = 'wuhan' and c2 > 'c' and c3 = 'wangdao';
explain  select * from student where c1 = 'wuhan' and c2 like 'c%' and c3 = 'wangdao';

#4. 只访问索引的查询：索引列和查询列一致，尽量用覆盖索引，减少select *
explain  select * from student where c2 = 'wuhan';

explain  select c1,c2 from student where c2 ='wuhan'; 

#5. NULL/NOT NULL的可能影响


#6. 字符串类型加引号，不加引号会索引失效
explain  select * from student where c1 = '19';
explain  select * from student where c1 = 19;

#7. UNION的效率比or更好
explain select * from student where c1 = '19';
explain select * from student where c1 = 'wuhan';
explain select * from student where c1 = '19' or c1 = 'wuhan';
explain select * from student where c1 = '19' union select * from student where c1 = 'wuhan';
```



<a name="XBNFn"></a>
### 第三天问题总结

1.  使用数据库有什么优势数据保存在内存<br />优点： 存取速度快<br />缺点： 数据不能永久保存<br />数据保存在文件<br />优点： 数据永久保存<br />缺点：1）速度比内存操作慢，频繁的IO操作。2）查询数据不方便<br />数据保存在数据库<br />1）数据永久保存<br />2）使用SQL语句，查询方便效率高。<br />3）管理数据方便 

2.  设计表时，数据类型如何选择？<br />一般情况下，应该尽量使用可以正确存储数据的最小数据类型，使用时要注意只分配需要的空间，更长的列排序时会消耗更多内存。<br />对于经常变更的数据来说，CHAR比VARCHAR更好，因为CHAR不容易产生碎片。<br />对于非常短的列，CHAR比VARCHAR在存储空间上更有效率。<br />尽量避免使用TEXT/BLOB类型，查询时会使用临时表，导致严重的性能开销。 

3.  MyISAM与InnoDB各自有什么特点？<br />Innodb引擎：Innodb引擎提供了对数据库ACID事务的支持。并且还提供了行级锁和外键的约束。它的设计的目标就是处理大数据容量的数据库系统。数据和索引是集中存储的，`.ibd`文件<br />MyIASM引擎(原本Mysql的默认引擎)：不提供事务的支持，也不支持行级锁和外键，数据和索引是分别存储的，数据`.MYD`，索引`.MYI`文件。 

4.  MyISAM索引与InnoDB索引的区别？<br />InnoDB索引是聚簇索引，MyISAM索引是非聚簇索引。<br />InnoDB的主键索引的叶子节点存储着行数据，因此主键索引非常高效。<br />MyISAM索引的叶子节点存储的是行数据地址，需要再寻址一次才能得到数据。<br />InnoDB非主键索引的叶子节点存储的是主键和其他带索引的列数据，因此查询时做到覆盖索引会非常高效。

5.  创建索引的原则有哪些？<br />1）最左前缀匹配原则，组合索引非常重要的原则，mysql会一直向右匹配直到遇到范围查询(>、<、between、like)就停止匹配，比如a = 1 and b = 2 and c > 3 and d = 4 如果建立(a,b,c,d)顺序的索引，d是用不到索引的，如果建立(a,b,d,c)的索引则都可以用到，a,b,d的顺序可以任意调整。<br />2）较频繁作为查询条件的字段才去创建索引<br />3）更新频繁字段不适合创建索引<br />4）若是不能有效区分数据的列不适合做索引列(如性别，男女未知，最多也就三种，区分度实在太低)<br />5）尽量的扩展索引，不要新建索引。比如表中已经有a的索引，现在要加(a,b)的索引，那么只需要修改原来的索引即可。<br />6）定义有外键的数据列一定要建立索引。<br />7）对于那些查询中很少涉及的列，重复值比较多的列不要建立索引。 

6.  索引使用场景<br />1）利用建立了索引的字段作为查询条件，可以提高查询效率。<br />2）当我们使用`order by`将查询结果按照某个字段排序时，如果该字段没有建立索引，那么执行计划会将查询出的所有数据使用外部排序（将数据从硬盘分批读取到内存使用内部排序，最后合并排序结果），这个操作是很影响性能的，因为需要将查询涉及到的所有数据从磁盘中读到内存（如果单条数据过大或者数据量过多都会降低效率），再排序。<br />但是如果我们对该字段建立了索引，那么由于索引本身是有序的，因此直接按照索引的顺序和映射关系逐条取出数据即可。<br />3）索引覆盖<br />如果要查询的字段都建立过索引，那么引擎会直接在索引表中查询而不会访问原始数据（否则只要有一个字段没有建立索引就会做全表扫描），这叫索引覆盖。因此我们需要尽可能的在`select`后只写必要的查询字段，以增加索引覆盖的几率。 

7.  创建索引时需要注意什么？<br />1）非空字段：应该指定列为NOT NULL，除非你想存储NULL。在mysql中，含有空值的列很难进行查询优化，因为它们使得索引、索引的统计信息以及比较运算更加复杂。你应该用0、一个特殊的值或者一个空串代替空值；<br />2）取值离散大的字段（变量各个取值之间的差异程度）的列放到联合索引的前面，这样能够更加有效的过滤数据。<br />3）索引字段越小越好：数据库的数据存储以页为单位一页存储的数据越多一次IO操作获取的数据越大效率越高。 

8.  使用索引查询一定能提高查询的性能吗？为什么？<br />通常，通过索引查询数据比全表扫描要快。但是我们也必须注意到它的代价。<br />索引需要空间来存储，也需要定期维护， 每当有记录在表中增减或索引列被修改时，索引本身也会被修改。 这意味着每条记录的INSERT，DELETE，UPDATE将为此多付出4，5 次的磁盘I/O。 因为索引需要额外的存储空间和处理，那些不必要的索引反而会使查询反应时间变慢。使用索引查询不一定能提高查询性能，索引范围查询(INDEX RANGE SCAN)适用于两种情况:<br />	基于一个范围的检索，一般查询返回结果集小于表中记录数的30%<br />	基于非唯一性索引的检索 

9.  什么是最左前缀原则？ 
- 顾名思义，就是最左优先，在创建多列索引时，要根据业务需求，where子句中使用最频繁的一列放在最左边。
- 最左前缀匹配原则，非常重要的原则，mysql会一直向右匹配直到遇到范围查询(>、<、between、like)就停止匹配，比如a = 1 and b = 2 and c > 3 and d = 4 如果建立(a,b,c,d)顺序的索引，d是用不到索引的，如果建立(a,b,d,c)的索引则都可以用到，a,b,d的顺序可以任意调整。
- =和in可以乱序，比如a = 1 and b = 2 and c = 3 建立(a,b,c)索引可以任意顺序，mysql的查询优化器会帮你优化成索引可以识别的形式

10.  非聚簇索引一定会回表查询吗？<br />不一定，B+树在满足聚簇索引和覆盖索引的时候不需要回表查询数据，在B+树的索引中，叶子节点可能存储了当前的key值，也可能存储了当前的key值以及整行的数据，这就是聚簇索引和非聚簇索引。 在InnoDB中，只有主键索引是聚簇索引，如果没有主键，则挑选一个唯一键建立聚簇索引。如果没有唯一键，则隐式的生成一个键来建立聚簇索引。<br />当查询使用聚簇索引时，在对应的叶子节点，可以获取到整行数据，因此不用再次进行回表查询。 

11.  MySQL中InnoDB引擎的行锁是怎么实现的？<br />InnoDB是基于索引来完成行锁<br />例: select * from tab_with_index where id = 1 for update;<br />for update 可以根据条件来完成行锁锁定，并且 id 是有索引的列，如果 id 不是索引键那么InnoDB会使用表锁，此时行锁退化为表锁，并发性能降低。 

12.  B树和B+树的区别？<br />1）在B树中，你可以将键和值存放在内部节点和叶子节点；但在B+树中，内部节点都是键，没有值，叶子节点同时存放键和值。<br />2）B+树的叶子节点有一条链相连，而B树的叶子节点各自独立。

 

13.  如何定位及优化SQL语句的性能问题？创建的索引有没有被使用到?或者说怎么才可以知道这条语句运行很慢的原因？<br />对于低性能的SQL语句的定位，最重要也是最有效的方法就是使用执行计划，MySQL提供了explain命令来查看语句的执行计划。 我们知道，不管是哪种数据库，或者是哪种数据库引擎，在对一条SQL语句进行执行的过程中都会做很多相关的优化，对于查询语句，最重要的优化方式就是使用索引。 而执行计划，就是显示数据库引擎对于SQL语句的执行的详细情况，其中包含了是否使用索引，使用什么索引，使用的索引的相关信息等。 

14.  为什么要尽量设定一个主键？<br />主键是数据库确保数据行在整张表唯一性的保障，即使业务上本张表没有主键，也建议添加一个自增长的ID列作为主键。设定了主键之后，在后续的删改查的时候可能更加快速以及确保操作数据范围安全。 

15.  统计过慢查询吗？对慢查询都怎么优化过？<br />慢查询的优化首先要搞明白慢的原因是什么？ 是查询条件没有命中索引？是load了不需要的数据列？还是数据量太大？<br />所以优化也是针对这三个方向来的， 
   - 首先分析语句，看看是否load了额外的数据，可能是查询了多余的行并且抛弃掉了，可能是加载了许多结果中并不需要的列，对语句进行分析以及重写。
   - 分析语句的执行计划，然后获得其使用索引的情况，之后修改语句或者修改索引，使得语句可以尽可能的命中索引。
   - 如果对语句的优化已经无法进行，可以考虑表中的数据量是否太大，如果是的话可以考虑进行分表。



<a name="DBDay04"></a>
## DBDay04
<a name="KAkpm"></a>
### 一、问题回顾
1、三大范式？优缺点？反范式设计？优缺点

2、什么是聚集索引？什么是非聚集索引？聚集索引与主键索引是一回事吗？<br />.ibd<br />.myd .myi

3、什么是索引覆盖（覆盖索引）？什么是回表？<br />辅助索引树

4、执行计划中的几个重要字段，id、type、possible_keys、key、ken_len、extra、select_type？

5、索引失效的几种常见情况？

<a name="854000a1"></a>
### 二、主从复制
<a name="7ac32497"></a>
#### 定义
就是将一台MySQL服务器上的数据复制到一台或者多台服务器上。（主服务器-从服务器）<br />主机：dump线程， binlog日志<br />从机：IO线程、SQL线程、RelayLog日志

<a name="0a7a4bd5"></a>
### 三、Redis数据库
关系型数据库：支持表结构<br />非关系型数据库：不是以表结构存储数据<br />NoSQL，指的是**非关系型的数据库**。NoSQL有时也称作Not Only SQL的缩写

<a name="d0771a42"></a>
#### 分类
基于键值对 key-value类型：**Redis**，memcached<br />列存储数据库 Column-oriented Graph：HBase<br />图形数据库 Graphs based：Neo4j<br />文档型数据库： MongoDB<br />MongoDB是一个基于分布式文件存储的数据库，主要用来处理大量的文档。

<a name="bb5b60b7"></a>
#### Redis的概念
Remote Dictionary Servives .  远程字典服务器。<br />特点：开源的、C语言编写、高性能。可以用作**数据库、缓存、消息中间件**。基于**内存**的数据库、支持**持久化**（可以将数据长期保存）。

中文官网：[https://redis.cn/](https://redis.cn/)<br />官网：[https://redis.io/](https://redis.io/)

<a name="64b59234"></a>
#### Redis三大特性
1、支持持久化<br />2、支持丰富数据类型<br />3、支持数据备份（主从复制）

<a name="f1d7aa80"></a>
#### Redis的优点
1、性能高 读11w/s  写8.1w/s<br />2、具有丰富数据类型（五大数据类型）<br />3、原子的   操作是原子的，但是redis事务是不支持原子。<br />4、丰富的特性  支持发布订阅、支持key过期、

<a name="488f0be2"></a>
#### Redis基本命令
```sql
#默认支持16个数据库
#数据库的切换  
select + 数据库的编号

#查看数据库的大小
 DBSIZE
 
#查看当前数据库key的多少
127.0.0.1:6379> keys *  #  *可以匹配0个到任意个字符  ？可以匹配一个字符
1) "k1"
2) "k2"

127.0.0.1:6379> keys k?
1) "k1"
2) "k2"
127.0.0.1:6379> 


#删除key值
127.0.0.1:6379> DEL k1
(integer) 1    #结果是1或者0
127.0.0.1:6379> keys *
1) "k2"
127.0.0.1:6379>

#情况数据库
127.0.0.1:6379> FLUSHDB  #清空当前数据库
OK
127.0.0.1:6379> 
127.0.0.1:6379> FLUSHALL  #清空所有数据库
OK
127.0.0.1:6379> 

#key值移动到其他数据库
127.0.0.1:6379> move k3 1
(integer) 1
127.0.0.1:6379>

#判断某个key值是不是存在的
127.0.0.1:6379> EXISTS k3
(integer) 0
127.0.0.1:6379> EXISTS k1
(integer) 1
127.0.0.1:6379>

#查看变量的类型
127.0.0.1:6379> type k1
string

#设置过期时间
127.0.0.1:6379> EXPIRE k1 20
(integer) 1

#查看过期时间
127.0.0.1:6379> ttl k1
(integer) 17   #-1表名永不过期  -2表示已经过期了
```

<a name="02a5ba11"></a>
### 四、Redis的五种数据类型与命令
<a name="9226531f"></a>
#### 1、string数据类型
二进制安全的，可以存任何数据
```sql
#设置命令
set  key value
set k1 100

#获取key值
get key


#同时设置与获取多个key
127.0.0.1:6379> mset k11 11 k12 12 k13 helloworld k14 12.3
OK
127.0.0.1:6379> mget k11 k12 k13 k14
1) "11"
2) "12"
3) "helloworld"
4) "12.3"
127.0.0.1:6379> 
127.0.0.1:6379> 

#获取子串
127.0.0.1:6379> GETRANGE k13 0 -1  #-1表示倒数第一个
"helloworld"
127.0.0.1:6379>

#设置子串
127.0.0.1:6379> SETRANGE k13 0 wu
(integer) 10
127.0.0.1:6379> GETRANGE k13 0 -1
"wulloworld"
127.0.0.1:6379>

#同时获取与设置
127.0.0.1:6379> getset k1 hello
"100"
127.0.0.1:6379> get k1
"hello"
127.0.0.1:6379> 

#给某个key设置过期时间，并且赋新值
127.0.0.1:6379> setex k1 20 3000  #ex expire
OK
127.0.0.1:6379>

#累加
incr #每次加1个

incrby key  + 值  #每次可以增加指定的值
```

<a name="32a0dc04"></a>
#### 2、list数据类型
双向链表
```sql
#在链表的左右两边进行数据的插入与删除
lpush/rpush
lpop/rpop

#list的遍历
127.0.0.1:6379> lrange list1 0 -1
 1) "8"
 2) "6"
 3) "5"
 4) "4"
 5) "3"
 6) "2"
 7) "1"
 8) "20"
 9) "21"
10) "22"
127.0.0.1:6379>

#list是支持下标的（与STL中的list不一样,STL中的list不支持下标）
#lset  key  index value
127.0.0.1:6379> lset list1 0 888888  #下标的设置
OK

127.0.0.1:6379> lindex list1 8   #下标查找
"21"
127.0.0.1:6379>


#删除重复元素（与STL中list中unique不一样，unique需要进行sort）
127.0.0.1:6379> LREM list1 5 1
(integer) 5
127.0.0.1:6379> 


#修剪指定范围以外数据
127.0.0.1:6379> LTRIM list1 1 4
OK
127.0.0.1:6379>

#在指定元素的前后插入数据
127.0.0.1:6379> LINSERT list1 after 2 2222
(integer) 7
127.0.0.1:6379> lrange list1 0 -1
1) "5"
2) "4"
3) "100"
4) "3"
5) "200"
6) "2"
7) "2222"
127.0.0.1:6379>
```

<a name="1be814a1"></a>
#### 3、set数据类型
集合，元素是唯一的，但是没有顺序的，底层使用哈希（不同与STL中的set）
```sql
#添加元素使用sadd
127.0.0.1:6379> sadd myset1 1 2 3 1 2 3 4 6 8
(integer) 6
#查看元素的个数
127.0.0.1:6379> scard myset1
(integer) 6
#遍历set
127.0.0.1:6379> smembers myset1
1) "1"
2) "2"
3) "3"
4) "4"
5) "6"
6) "8"
127.0.0.1:6379>
#随机获取number个数据
127.0.0.1:6379> srandmember myset1 3
1) "7"
2) "3"
3) "2"
127.0.0.1:6379> 
#随机选取num个元素并且删除
127.0.0.1:6379> spop myset1 1
1) "4"
127.0.0.1:6379> 
127.0.0.1:6379> 
127.0.0.1:6379> smembers myset1
1) "3"
2) "2"
3) "1"
4) "6"
5) "8"
127.0.0.1:6379>

#取差集、取交集、取并集
SDIFF key1 key2
SINTER key1 key2 
SUNION key1 key2
```

<a name="7b829d3f"></a>
#### 4、sorted set数据类型
将每个元素的前面设置一个double分数（看成是权重）
```sql
127.0.0.1:6379> zadd myset2 10  k1  10 hello 10 world  10 wangdao
(integer) 4
127.0.0.1:6379> ZRANGEBYLEX myset2 - +   #此处-表示负无穷  +正无穷
1) "hello"
2) "k1"
3) "wangdao"
4) "world"
127.0.0.1:6379>
#保证元素的分数值一致的情况下面，使用ZRANGEBYLEX命令
#后面是范围值    [闭区间   (开区间
127.0.0.1:6379> ZRANGEBYLEX myset2 [h [k1
1) "hello"
2) "k1"
127.0.0.1:6379>
```

<a name="eb293d6f"></a>
#### 5、hash数据类型
Key-value模式不变，但value是一个键值对map<key, map<key1, value>>
```sql
#string类型可以看成是key-value类型，但是hash是key1-（key2-value）
#map<key, value>                 map<key1, map<key2, value>>
127.0.0.1:6379> set k1 100
OK
127.0.0.1:6379> hset hash1 str1 100
(integer) 1
127.0.0.1:6379> type k1
string
127.0.0.1:6379> type hash1
hash
127.0.0.1:6379> 

#一次可以获取或者设置多个值
127.0.0.1:6379> hmset people age 10 sex man 
OK
127.0.0.1:6379> hmget people age sex
1) "10"
2) "man"
127.0.0.1:6379> 

127.0.0.1:6379> hkeys people
1) "age"
2) "sex"
127.0.0.1:6379> 
127.0.0.1:6379> 
127.0.0.1:6379> hvals people
1) "10"
2) "man"
127.0.0.1:6379>
```

<a name="66806879"></a>
### 五、Redis的配置文件
路径：/etc/redis下面会有一个6379.conf

<a name="4db37dd7"></a>
#### redis服务器的启动
redis-server /path/to/redis.conf，会以守护进程的形式开启

redis-server 不带配置文件开启redis服务器，带图形界面

<a name="a0381886"></a>
### 六、持久化
<a name="osBSQ"></a>
#### 概念
将redis中的数据从内存保存的磁盘。

<a name="d0771a42-1"></a>
#### 分类
RDB：将**数据**保存到磁盘上面（原理：定期的将redis的数据dump到磁盘上面），默认的持久化方式<br />AOF：将每次执行的**写命令**保存到硬盘（原理是将Reids的操作日志以追加的方式写入文件，类似于MySQL的binlog），主流的持久化方式

<a name="5a8fc0b1"></a>
#### RDB的特点
在指定的**时间间隔**内，执行指定次数的写操作，则会将内存中的数据写入到磁盘中。即在指定目录下生成一个dump.rdb文件。Redis 重启会通过加载dump.rdb文件恢复数据。（/var/lib/redis/6379）

<a name="a586d22a"></a>
##### 触发快照的方式
1、执行shutdown命令，会触发快照<br />2、执行flushall命令，也会触发快照<br />3、手动执行save命令，也会触发快照

```bash
cd /var/lib/redis/6379   // redis dump.rdb 备份文件存储位置
```
![image-20220614160804362.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655210295622-05e34b01-fb22-4331-a647-99b3545237e6.png#clientId=u7bcd6c8b-085f-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uc0446096&name=image-20220614160804362.png&originHeight=307&originWidth=1475&originalType=binary&ratio=1&rotation=0&showTitle=false&size=54481&status=done&style=none&taskId=ud32e18e8-02d3-444d-a355-bb99a253635&title=)

**4、在指定的时间间隔内，执行指定次数的写操作**<br />![image-20220614160907755.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655210327535-f5adbed0-b039-4f93-a54a-ed13a6b12e68.png#clientId=u7bcd6c8b-085f-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ua910009e&name=image-20220614160907755.png&originHeight=108&originWidth=825&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15662&status=done&style=none&taskId=u047b3fd6-a7fa-43e0-94fe-681d61f0032&title=)

```sql
#配置文件的默认写法-优先从下，不满足则往上(需同时满足一行两个条件)
308 save 900 1
309 save 300 10
310 save 60 10000
```
save time times 时间time与次数times要都满足，不然就触发不了快照。<br />测试：save 30 2，要保证在30s以内执行2次写操作；保证时间30s要到达，写次数2次也要满足。可以将时间设置在后面30s，并且先执行一些save，再执行两次写操作。

![image-20220614162210997.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655210505572-c4acbe89-b580-4854-a125-dbcf381ef4d0.png#clientId=u7bcd6c8b-085f-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u9eeda428&name=image-20220614162210997.png&originHeight=350&originWidth=1577&originalType=binary&ratio=1&rotation=0&showTitle=false&size=92403&status=done&style=none&taskId=ub69dde5b-efc9-41b1-a72f-d9347f80584&title=)

优点：<br />1、数据恢复的时间比aof要快<br />2、如果对数据的一致性和完整性要求不高的时候，可以使用RDB持久化的方式。

缺点：<br />1、对数据的完整性与一致性的要求不高。<br />2、备份时占用内存，因为Redis 在备份时会独立创建一个fork子进程，将数据写入到一个临时文件（此时内存中的数据是原来的两倍哦）

<a name="e1f661ef"></a>
#### AOF持久化方式
AOF方式是将执行过的**写指令记录**下来，在数据恢复时按照**从前到后的顺序再将指令都执行一遍**<br />默认情况下，是每秒同步一次。最多会丢失1s的数据<br />![image-20220614163816328.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655210559636-a122ea93-0951-411c-955a-ebfa75584c2f.png#clientId=u7bcd6c8b-085f-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u81d8f80a&name=image-20220614163816328.png&originHeight=162&originWidth=522&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18222&status=done&style=none&taskId=u741e04d9-66a7-4d59-8941-3c61360c6b7&title=)

```sql
set k1 1
incr k1
incr k1
#.... 10000次
incr k1
get k1 #10000

# <=>
set k1 10000
```

![image-20220614164615082.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655210641795-ead7d4fa-4ea3-4fce-b00f-4ddf41b37ef1.png#clientId=u7bcd6c8b-085f-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u556411d5&name=image-20220614164615082.png&originHeight=233&originWidth=818&originalType=binary&ratio=1&rotation=0&showTitle=false&size=48225&status=done&style=none&taskId=u446e1ae3-3189-48d1-b9d4-92de350d301&title=)

<a name="52b8c184"></a>
#### 优点
1、对数据完整性与一致性更高，最多只会丢失1s的数据

<a name="2e769a75"></a>
#### 缺点
对于大量数据恢复的时候，执行的命令的时间比较长

<a name="25f9c7fa"></a>
#### 总结
1、两种持久化的方式一般都是同时开启的，既能保证数据的完整性和一致性，也能保证大量数据恢复的时候，时间比较快。<br />2、如果只开启aof持久化的方式，并且被损坏了，此时不能启动成功的。<br />3、如果aof文件损坏了，是可以进行手动修复的。redis-check-aof

![image-20220614165752090.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655210678693-73f3b5e1-16ec-41ea-a1ea-001d71994305.png#clientId=u7bcd6c8b-085f-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u674d888a&name=image-20220614165752090.png&originHeight=335&originWidth=932&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33376&status=done&style=none&taskId=u986fa8ea-4d1f-4886-b719-20b9a7aa682&title=)

<a name="1ed4e9fd"></a>
### 七、Redis事务
<a name="u7U2L"></a>
#### 概念
一组命令的集合。
<a name="6743b681"></a>
#### 三个阶段
开启事务、命令入队（命令之间不会有加塞）、执行事务

<a name="e198958d"></a>
#### 事务的基本操作
```sql
#开启事务
multi

#执行事务
exec

#监视一个或多个变量
watch

#事务的基本操作
127.0.0.1:6379[2]> MULTI  #开启事务
OK
127.0.0.1:6379[2]> get k1   #执行第一条命令
QUEUED
127.0.0.1:6379[2]> get k2   #执行第二条命令
QUEUED
127.0.0.1:6379[2]> set k3 300   #执行第三条命令
QUEUED
127.0.0.1:6379[2]> exec  #执行事务
1) "100"
2) "hello"
3) OK
127.0.0.1:6379[2]>
```

![image-20220614172650700.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655210714289-ad1347e6-872d-4811-882a-f3ba27b32a22.png#clientId=u7bcd6c8b-085f-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uec0e28ca&name=image-20220614172650700.png&originHeight=522&originWidth=847&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52385&status=done&style=none&taskId=ub3003175-3a05-4f54-bd83-10bcacc013d&title=)

![image-20220614173051253.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655210736449-5911da33-c468-49ed-8b9d-bb3d4fbc1e2c.png#clientId=u7bcd6c8b-085f-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uf16aac30&name=image-20220614173051253.png&originHeight=494&originWidth=917&originalType=binary&ratio=1&rotation=0&showTitle=false&size=45397&status=done&style=none&taskId=u4ed70526-8fb2-4221-bfab-7aad74ee9ec&title=)<br />可以把这两种错误看成是编译起码时候的，编译时出错（set k5，语法不通）以及运行时出错（incr k2）

**总结：redis的每条命令是原子的，但是redis的事务是不保证原子性的。（MySQL事务是具有原子性的）**

**watch可以监视某个变量**<br />![image-20220614173959121.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655210765521-828db669-7422-4289-9b30-1f4d8048f2e6.png#clientId=u7bcd6c8b-085f-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u91ca2d4f&name=image-20220614173959121.png&originHeight=583&originWidth=1474&originalType=binary&ratio=1&rotation=0&showTitle=false&size=80295&status=done&style=none&taskId=u417ef0bb-52ad-41e7-bdd2-b9b241ffa78&title=)<br /> 

<a name="e4469890"></a>
#### 事务的锁机制
悲观锁：每次拿数据的时候，都会对数据进行加锁操作。<br />乐观锁：每次去拿数据的时候都不会上锁（**使用版本号机制或CAS操作实现**）

共享数据不加锁   

- CAS(check and set)  **内存值V、预期值A、新值B** 需要更新时，判断当前内存值V与之前的值A是否相等，若相等，则用新值更新；若失败则重试，一般是自旋操作，即不断重试。 
- 开不同版本号，保证数据相同) 

原子数据类型_int

<a name="a45a5ea4"></a>
#### 事务的特征
1、单独的隔离操作<br />2、没有隔离级别的说法<br />3、事务不保证原子性

<a name="a41ko"></a>
### day04 -  Redis 问题总结
<a name="705520f2"></a>
### 1、 什么是Redis?有哪些有优缺点？
Redis(Remote Dictionary Server) 是一个使用 C 语言编写的，开源的（BSD许可）高性能非关系型（NoSQL）的键值对数据库。<br />与传统数据库不同的是 Redis 的数据是存在内存中的，所以读写速度非常快，因此 redis 被广泛应用于缓存方向，每秒可以处理超过 10万次读写操作，是已知性能最快的Key-Value DB。<br />数据库容量受到物理内存的限制，不能用作海量数据的高性能读写，因此Redis适合的场景主要局限在较小数据量的高性能操作和运算上

<a name="cbeeb3e6"></a>
### 2、为什么要用 Redis /为什么要用缓存
主要从“高性能”和“高并发”这两点来看待这个问题。

**高性能：**<br />假如用户第一次访问数据库中的某些数据。这个过程会比较慢，因为是从硬盘上读取的。将该用户访问的数据存在数缓存中，这样下一次再访问这些数据的时候就可以直接从缓存中获取了。操作缓存就是直接操作内存，所以速度相当快。如果数据库中的对应数据改变的之后，同步改变缓存中相应的数据即可！

**高并发：**<br />直接操作缓存能够承受的请求是远远大于直接访问数据库的，所以我们可以考虑把数据库中的部分数据转移到缓存中去，这样用户的一部分请求会直接到缓存这里而不用经过数据库。

<a name="1a308dfc"></a>
### 3、 Redis为什么这么快
1）完全基于内存，绝大部分请求是纯粹的内存操作，非常快速。数据存在内存中，类似于 HashMap，HashMap 的优势就是查找和操作的时间复杂度都是O(1)；<br />2）数据结构简单，对数据操作也简单，Redis 中的数据结构是专门进行设计的；<br />3）采用单线程，避免了不必要的上下文切换和竞争条件，也不存在多进程或者多线程导致的切换而消耗 CPU，不用去考虑各种锁的问题，不存在加锁释放锁操作，没有因为可能出现死锁而导致的性能消耗；<br />4）使用多路 I/O 复用模型，非阻塞 IO；

<a name="e14ab91a"></a>
### 4、Redis有哪些数据类型
Redis相比其他缓存，有一个非常大的优势，就是支持多种数据类型。Redis主要有5种数据类型，包括String，List，Set，Zset，Hash，虽然Redis不像关系数据库那么复杂的数据结构，但是，也能适合很多场景，比一般的缓存数据结构要多。

<a name="0a51bb7a"></a>
### 5、什么是Redis持久化？
持久化就是把内存的数据写到磁盘中去，防止服务宕机了内存数据丢失。

<a name="e5e15810"></a>
### 6、Redis 的持久化机制是什么？各自的优缺点？
Redis 提供两种持久化机制 RDB（默认） 和 AOF 机制:<br />RDB：是Redis DataBase缩写快照<br />RDB是Redis默认的持久化方式。按照一定的时间将内存的数据以快照的形式保存到硬盘中，对应产生的数据文件为dump.rdb。通过配置文件中的save参数来定义快照的周期。

优点：

- 1、只有一个文件 dump.rdb，方便持久化。
- 2、容灾性好，一个文件可以保存到安全的磁盘。
- 3、性能最大化，fork 子进程来完成写操作，让主进程继续处理命令，所以是 IO 最大化。使用单独子进程来进行持久化，主进程不会进行任何 IO 操作，保证了 redis 的高性能
- 4.相对于数据集大时，比 AOF 的启动效率更高。

缺点：

- 1、数据安全性低。RDB 是间隔一段时间进行持久化，如果持久化之间 redis 发生故障，会发生数据丢失。所以这种方式更适合数据要求不严谨的时候)
- 2、AOF（Append-only file)持久化方式： 是指所有的命令行记录以 redis 命令请 求协议的格式完全持久化存储)保存为 aof 文件。

AOF：持久化<br />AOF持久化(即Append Only File持久化)，则是将Redis执行的每次写命令记录到单独的日志文件中，当重启Redis会重新将持久化的日志中文件恢复数据。<br />当两种方式同时开启时，数据恢复Redis会优先选择AOF恢复。

优点：

- 1、数据安全，aof 持久化可以配置 appendfsync 属性，有 always，每进行一次 命令操作就记录到 aof 文件中一次。
- 2、通过 append 模式写文件，即使中途服务器宕机，可以通过 redis-check-aof 工具解决数据一致性问题。
- 3、AOF 机制的 rewrite 模式。AOF 文件没被 rewrite 之前（文件过大时会对命令 进行合并重写），可以删除其中的某些命令（比如误操作的 flushall）)

缺点：

- 1、AOF 文件比 RDB 文件大，且恢复速度慢。
- 2、数据集大的时候，比 rdb 启动效率低。

两者对比：

- AOF文件比RDB更新频率高，优先使用AOF还原数据。
- AOF比RDB更安全也更大
- RDB性能比AOF好
- 如果两个都配了优先加载AOF

<a name="0fbccbd1"></a>
### 7、 Redis key的过期时间和永久有效分别怎么设置？
EXPIRE和PERSIST命令。

我们知道通过expire来设置key 的过期时间，那么对过期的数据怎么处理呢?<br />除了缓存服务器自带的缓存失效策略之外（Redis默认的有6中策略可供选择），我们还可以根据具体的业务需求进行自定义的缓存淘汰，常见的策略有两种：

1. 定时去清理过期的缓存；
1. 当有用户请求过来时，再判断这个请求所用到的缓存是否过期，过期的话就去底层系统得到新数据并更新缓存。

两者各有优劣，第一种的缺点是维护大量缓存的key是比较麻烦的，第二种的缺点就是每次用户请求过来都要判断缓存失效，逻辑相对比较复杂！具体用哪种方案，大家可以根据自己的应用场景来权衡。

<a name="1af65d5c"></a>
### 8、Redis事务的概念
Redis 事务的本质是通过MULTI、EXEC、WATCH等一组命令的集合。事务支持一次执行多个命令，一个事务中所有命令都会被序列化。在事务执行过程，会按照顺序串行化执行队列中的命令，其他客户端提交的命令请求不会插入到事务执行命令序列中。

总结说：redis事务就是一次性、顺序性、排他性的执行一个队列中的一系列命令。

<a name="76d53acf"></a>
### 9、Redis事务的三个阶段

1. 事务开始 MULTI
1. 命令入队
1. 事务执行 EXEC

<a name="469748b3"></a>
### 10、Redis事务相关命令和事务的特征？
Redis事务功能是通过MULTI、EXEC、DISCARD和WATCH 四个原语实现的<br />Redis会将一个事务中的所有命令序列化，然后按顺序执行。

1. **redis 不支持回滚**，“Redis 在事务失败时不进行回滚，而是继续执行余下的命令”， 所以 Redis 的内部可以保持简单且快速。
1. **如果在一个事务中的命令出现错误，那么所有的命令都不会执行**；
1. **如果在一个事务中出现运行错误，那么正确的命令会被执行**。
- WATCH 命令是一个乐观锁，可以为 Redis 事务提供 check-and-set （CAS）行为。 可以监控一个或多个键，一旦其中有一个键被修改（或删除），之后的事务就不会执行，监控一直持续到EXEC命令。
- MULTI命令用于开启一个事务，它总是返回OK。 MULTI执行之后，客户端可以继续向服务器发送任意多条命令，这些命令不会立即被执行，而是被放到一个队列中，当EXEC命令被调用时，所有队列中的命令才会被执行。
- EXEC：执行所有事务块内的命令。返回事务块内所有命令的返回值，按命令执行的先后顺序排列。 当操作被打断时，返回空值 nil 。
- 通过调用DISCARD，客户端可以清空事务队列，并放弃执行事务， 并且客户端会从事务状态中退出。
- UNWATCH命令可以取消watch对所有key的监控。

<a name="34cba965"></a>
### 11、缓存穿透是什么？如何解决？
**缓存穿透**是指缓存和数据库中都没有的数据，导致所有的请求都落到数据库上，造成数据库短时间内承受大量请求而崩掉。

**解决方案**

1. 接口层增加校验，如用户鉴权校验，id做基础校验，id<=0的直接拦截；
1. 从缓存取不到的数据，在数据库中也没有取到，这时也可以将key-value对写为key-null，缓存有效时间可以设置短点，如30秒（设置太长会导致正常情况也没法使用）。这样可以防止攻击用户反复用同一个id暴力攻击
1. 采用布隆过滤器，将所有可能存在的数据哈希到一个足够大的 bitmap 中，一个一定不存在的数据会被这个 bitmap 拦截掉，从而避免了对底层存储系统的查询压力

<a name="78ba009a"></a>
### 12、缓存击穿是什么？有什么解决方案？
**缓存击穿**是指缓存中没有但数据库中有的数据（一般是缓存时间到期），这时由于并发用户特别多，同时读缓存没读到数据，又同时去数据库去取数据，引起数据库压力瞬间增大，造成过大压力。和缓存雪崩不同的是，缓存击穿指并发查同一条数据，缓存雪崩是不同数据都过期了，很多数据都查不到从而查数据库。

**解决方案**

1. 设置热点数据永远不过期。
1. 利用互斥锁保证同一时刻只有一个客户端可以查询底层数据库的这个数据，一旦查到数据就缓存至Redis内，避免其他大量请求同时穿过Redis访问底层数据库。

<a name="9ba0fdac"></a>
### 13、缓存雪崩的概念？如何应对？
**缓存雪崩**是指缓存同一时间大面积的失效，所以，后面的请求都会落到数据库上，造成数据库短时间内承受大量请求而崩掉。

**解决方案**

1.  缓存数据的过期时间设置随机，防止同一时间大量数据过期现象发生。 
1.  一般并发量不是特别多的时候，使用最多的解决方案是加锁排队。 



<a name="DBDay05"></a>
## DBDay05
<a name="pLssX"></a>
### 一、问题回顾
1、Redis的基本概念？优缺点？特征？Redis的有哪五大数据类型以及对应的命令？

2、Redis的持久化包含那两种，分别具有什么特征？

3、Redis事务的三个阶段？Redis的锁机制？事务的特征？

<a name="45abec73"></a>
### 二、Redis的主从复制
主从复制，是指将一台Redis服务器的数据，复制到其他的Redis服务器。前者称为主节点(master)，后者称为从节点(slave)；数据的复制是**单向**的，只能由主节点到从节点。

**实现负载均衡、故障恢复、读写分离。**

<a name="1fc4c1f5"></a>
#### 配置步骤
1、在/etc/redis下面，拷贝6379.conf到6380.conf与6381.conf，然后修改6380与6381中的数据<br />端口号port：6379  6380 6381<br />pidfile： pidfile "/var/run/redis_6380.pid"<br />日志文件：logfile "/var/log/redis_6380.log"<br />dump.rdb：dbfilename "dump6380.rdb"<br />aof文件名：appendfilename "appendonly6380.aof"

2、分别启动三台redis服务器<br />sudo redis-server   /etc/redis/6379.conf<br />sudo redis-server   /etc/redis/6380.conf<br />sudo redis-server   /etc/redis/6381.conf<br />![image-20220615100006790.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655292772274-c2c7bdac-20e2-4d49-be48-945d0bf3f4f5.png#clientId=uea72094d-8858-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ubd7bc627&name=image-20220615100006790.png&originHeight=171&originWidth=1508&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24073&status=done&style=none&taskId=u9bcaa8ff-4399-4e58-99aa-8b85cfd0f00&title=)

<br />3、登录到对应的服务器的客户端<br />redis-cli -p 6381 <br />redis-cli -p 6380 <br />redis-cli -p 6379


4、在每个客户端下面执行info replication，查看主从复制的信息（默认情况下，每台机器都是主节点）<br />![image-20220615100411097.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655292804307-cd578602-9e26-4d4b-93fb-6e7c0ec30d5e.png#clientId=uea72094d-8858-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ufe90f7fc&name=image-20220615100411097.png&originHeight=495&originWidth=860&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37076&status=done&style=none&taskId=uad42dcd1-3b39-4ee2-a5fc-e2e0e975e01&title=)

5、在设置为从机的客户端上面，执行相应的命令<br />SLAVEOF 127.0.0.1 6379

6、现象

- 在主机上面进行写操作，数据会备份到从机上面来，**从机**是不能进行**写操作**的。
- 当主机挂掉之后，从机会默默等待主机上线，**从机**之间**不会自动竞争为主机身份**。当主机6379重新恢复上线的时候，6380与6381会自动连接到6379上面，还是6379的**从机**。
- 将6381设置为6380的从机，结构上6379是6380的主机，6380是6381的主机，6380此时还是从机的身份。在6379上面写的数据会备份到6380，再从6380备份到6381。同时6380虽然是6381的主机，但是6380是6379的从机，所以6380上面仍然**不能进行写操作**。
- 将从机挂掉之后，在重新上线，从机依然会连接到之前的主机上面。（哨兵模式配置好后，才会主动连接）

<a name="b87a883b"></a>
### 三、哨兵模式
可以使用一个哨兵进行监视主机，当主机挂掉之后，会执行**流言协议**并且执行**投票协议**，让剩下的从机竞争出一个主机。

<a name="01190121"></a>
#### 哨兵的配置
1、配置文件
```sql
sentinel monitor master6379 127.0.0.1 6379 1  #监视的主机6379
```

2、启动哨兵的配置文件<br />sudo redis-server /etc/redis/sentinel.conf

3、将主机6379挂掉（shutdown）

4、哨兵就会进行投票，选出新的主机

可以解决的问题：当主机挂掉之后，从机依然是从机，群龙无首的现象。

<a name="41c734b7"></a>
### 四、Redis常见问题（重点）

<a name="b901facc"></a>
#### 缓存雪崩
**大量数据在同一时间失效**了，多个请求进行查找的时候，不能在缓存中找到，只能在底层的数据库中进行查找，此时数据库的压力就比较大。

解决方案：1、分散失效时间，让数据不再同一时间失效  2、可以不设置过期时间<br />![image-20220615112238662.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655292864058-ccd2d33c-ea03-49a6-a729-a5431eca6e44.png#clientId=uea72094d-8858-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ubf310d8d&name=image-20220615112238662.png&originHeight=496&originWidth=877&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29775&status=done&style=none&taskId=ue98277ef-6ac3-48b8-8af9-7d6daa46934&title=)


<a name="a62f4468"></a>
#### 缓存击穿
**某个热点key值**，从缓存中失效了，如果大量请求都进来的时候，在缓存找不到该key，这些请求都会到底层数据库进行查找，底层数据库的压力就比较大。

解决方案：延长热点数据的过期时间或者让其永不失效。<br />![image-20220615112302103.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655292887029-99452a38-6c0d-4e9f-b604-bb2766426d04.png#clientId=uea72094d-8858-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ua93b30f6&name=image-20220615112302103.png&originHeight=511&originWidth=869&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31442&status=done&style=none&taskId=u43c1459e-c44d-4771-9fe6-29813276c43&title=)

<a name="b8d9ceea"></a>
#### 缓存穿透
查找的**数据在缓存以及底层数据库中，压根就不存在**，每次查找都必须到底层数据库，底层数据库的压力也会非常大。

解决方案：map<key, null><br />1、可以设置一个key以及对应的value值为空，并且存放在缓存中，这样当进行查找的时候，如果value为空，就不会再继续在底层数据库上进行查找<br />![image-20220615112937469.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655292915225-36f16607-058f-4751-9fa3-ddf84dc1f3af.png#clientId=uea72094d-8858-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ue1e2fa26&name=image-20220615112937469.png&originHeight=539&originWidth=925&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37557&status=done&style=none&taskId=ub96a6c18-4ae8-4929-b725-6e4f7af2913&title=)

<a name="5ee20bcc"></a>
### 五、Hiredis的安装与使用
安装hiredis，对应的安装步骤
```bash
tar -xzvf hiredis.tar.gz
cd hiredis
make
sudo make install

//更新缓存
sudo ldconfig

//相应的头文件
/usr/local/include
```

<a name="ecff77a8"></a>
#### 使用
在代码中包含头文件即可
```c
#include <hiredis/hiredis.h>
```

<a name="984612f0"></a>
#### 编译
```bash
g++ *.cc -lhiredis
```

<a name="c7d0afc0"></a>
#### 四个API
```c
//进行数据库的连接
redisContext* redisConnect(const char *ip, int port);

//对应命令的执行
void *redisCommand(redisContext *c, const char *format...);

//两个释放的命令
void freeReplyObject(void *reply);

void redisFree(redisContext *c);
```
