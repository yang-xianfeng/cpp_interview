
最高效率的 脚本语言（输入一行，执行一行   —— 系统语言）。<br />游戏 、 网络 <br />nginx 的插件<br />redis的原子锁   自带的lua脚本<br />中国 ：2002  云风  《大话西游》<br />国外 ：2004年 《魔兽世界》《dota2》<br />游戏引擎 ： unity   unreal<br />腾讯上海： X-Lua   基于Unreal 提供Lua脚本<br />自己实现 游戏批量操作脚本 

Lua 是由 clean-C （ C和C++的公共部分 ）


<a name="U1c0O"></a>
#### lua解释器
解释器： 把高级语言 --> 汇编语言 以一行为单位，执行代码<br />Lua  --> Lua VM --机器指令--> OS<br />语法特点：<br />1、动态类型<br />2、不需要声明   （ typescript   在 国外公司，基本都是写前端 ）<br />3、解释型语言  跨平台<br />4、垃圾回收 （ 双摄标记垃圾回收算法   回收时必须单线程 ）“ stop the world ”

<a name="iTdXr"></a>
#### Lua代码脚本的运行
1、通过命令行<br />2、lua解释行以lua文件执行<br />3、lua脚本 （ 第一行 /usr/loacl/include/lua  称作share bar ）


![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658214386398-ef1e73f9-df72-4f5a-a9b2-04dedb1d1c24.png#clientId=u60838175-1a7b-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=103&id=ubccd3544&margin=%5Bobject%20Object%5D&name=image.png&originHeight=142&originWidth=650&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13457&status=done&style=none&taskId=ub9402a48-d391-47f1-87e4-227b58458f3&title=&width=472.72727272727275)<br />chunk 单次编译的的单位<br />字节码 和 汇编代码 非常相像<br />编译（词法分析、语法分析、构建文件树） 耗时长  （ 预编译 提升运行速度    例如：Android）<br />JIT （ just in time ）  openresty     lua5.1

<a name="w2b44"></a>
#### args_lua
```lua
print(-1,arg[-1])
print(0,arg[0])
-- 从此处可以看出，列表从1开始，键并不限制为正整数
for i = 1,#arg do -- #是求列表长度运算符
    print(i,arg[i])
end
print(-2,arg[-2])

```
lua数组    下标从1开始      arg[#arg]  最后一个元素<br />pascal语言  do - {        end - }


<a name="YlWmk"></a>
#### 其他的语法规范
标识符 和 C一样<br />大小写敏感  （ sql不敏感 ）<br />变量是对值的引用<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658215244470-62186702-55e3-442f-b3ac-c26efc70c5ff.png#clientId=u60838175-1a7b-4&crop=0&crop=0.0041&crop=0.9441&crop=1&from=paste&height=229&id=u1af38775&margin=%5Bobject%20Object%5D&name=image.png&originHeight=333&originWidth=320&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43612&status=done&style=none&taskId=u4f608456-1939-4aa9-82f9-c29f41ba65d&title=&width=220)<br />作用域 ： 1、全局 （ 默认 ）   2、局部   end    加上local<br />；空语句  C语言编译时按照；划分语句


<a name="YIP4N"></a>
#### lua当中 变量和值的关系
内存分配 数据类型由值决定， 变量只是对值的引用<br />lua中的函数都是函数对象 可以赋值<br /> Lua的值有8种数据类型，分别为nil、布尔、数字、字符串、表、函数、线程和用户数据。其中 nil、布尔、数值、字符串为基础数据类型。  <br />nil  number  string  boolean  table表  function  thread userdate


<a name="dhnGG"></a>
#### 逻辑操作
nil为假 其他为正<br />not > and > or

and      lhs and rhs <br />lhs为真，返回lhs<br />lhs为假，返回rhs

or     lhs or rhs <br />lhs为真，返回rhs<br />lhs为假，返回lhs

not   not hs<br />hs为真，返回false<br />hs为假，返回true

可以实现三目运算符：
```lua
a and b or c  已知b为真
a为真  (a and b)->b  (b or c) -> b
a为假  (a and b)->a  (a or c) -> c
```

<a name="kOuuH"></a>
#### 数值：
数学一致<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658218566742-a80a43af-7cf7-4bec-a6d0-65d49bdfb422.png#clientId=u60838175-1a7b-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=338&id=ub44f6648&margin=%5Bobject%20Object%5D&name=image.png&originHeight=465&originWidth=1058&originalType=binary&ratio=1&rotation=0&showTitle=false&size=191590&status=done&style=none&taskId=ucdf376d9-12a0-449d-9eeb-5a6dc7c4fe0&title=&width=769.4545454545455)

```lua
str = "hello"
print(str)
str = 'hello'
print(str)
--[[ 这里的换行是不在字符串里面的
str = [[ 
"It's 8 o'clock!" She said]]
print(str)
str = [=[
arr[p[i]] = 1 ]=]
print(str)
str = [====n个 ...... ====n个]
```
边界使用 ' （ " ）后，字符串内的' （ " )则需要转义\

<a name="DFf1l"></a>
#### 字符串支持的运算操作
#获取长度<br />.. 运算符 连接字符串，.. 运算符 左右需要加 空格<br />自带隐式转换
```lua
print("1" + 2)
print(1 .. 2)
--print(1..3) --无法识别小数点和..
str = "3.14e1"
print(str)
print(tonumber(str)) --打印出适合阅读的数字

line = oi.read()
n = tonumber(line)
if n then --第一个条件的分割符
  print(2*n)
else
  print(line .. " is not a vaild nummber")
  --error(line .. " is not a vaild nummber") --会打印错误信息和栈信息
end

--tostring --数字转字符串
```


![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1658219985815-c968dc07-bd8a-4f10-b92b-be045770d9d8.png#clientId=u60838175-1a7b-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=217&id=ue87bfc62&margin=%5Bobject%20Object%5D&name=image.png&originHeight=299&originWidth=747&originalType=binary&ratio=1&rotation=0&showTitle=false&size=217659&status=done&style=none&taskId=u658660a3-10ac-4d7c-80d8-36bb21f3818&title=&width=543.2727272727273)
```lua
str = "helloworld"
print(string.byte(str,1,#str))
print(string.byte(str,1,-1))  -- -1代表倒数第一
print(string.char(104,101,108,108,111,119,111,114,108,100)
print(string.len(str))
print(string.upper(str))
print(string.rep(str,3))
print(string.reverse(str))
print(string.sub(str,2,-2))

  10.lua

string.format()
  
  
--%q   \0
--%s   类似C，以\0分割
  
```
自带模式匹配 （简化版本的正则表达式）


lua当中字符串的存储<br />存储在常量区<br />1、字符串值不可被修改
```lua
str =  "hello"
str = str .. "world"

"hello"  "world"  "helloworld"  --所有中间结果也会存储
```
2、多个变量可以引用同一位置的字符串且没有任何风险<br />3、任何修改/中间结果都申请新的内存 <br /> 底层原理是一个字符串散列（hash)桶    ——  字符串常量池

<a name="uWctd"></a>
#### 使用过多的字符串的问题
intermediate.lua
```lua
local begTime = os.clock()
local str = ''
for i = 1, 300000 do
  str = str .. "a"
end
local endTime = os.clock()
print(endTime - begTime)
--12.186306
```
每次的中间结果都会放入hash表中（字符串常量池）


优化
```lua
local begTime = os.clock()
local t = {}
for i = 1, 300000 do
  t[#t+1] = "a"
end
str = table.concat(t,"")
local endTime = os.clock()
print(endTime - begTime)
--0.050907
```
 ‘a'    '30000个a'    放入hash表中（字符串常量池）
