## 标准模板库

STL包含六大基本组件：

1.  容器：用来存放数据，也称为数据结构
   -  序列式容器（顺序容器）：vector、list
   -  关联式容器：set 、 map
   -  无序关联式容器：unordered_set 、unordered_map
2.  迭代器 类似于指针，称为广义指针，遍历或者访问容器
2.  适配器 类似于转接口，将不完全匹配的进行匹配
2.  算法
2.  函数对象（仿函数）
2.  空间配置器 `Allocator`    对容器进行空间的申请与释放

`push_back()`可以插入左值或右值

```cpp
push_back ( & );
push_back ( && );
```

#### 源码：

```cpp
//重定义的方式
using line_no = vector<string>::size_type;//C++11的写法
typedef vector<string>::size_type line_no;//C语言的实现方式
```

```cpp
typedef typename _Alloc_traits<_Tp, _Allocator>::allocator_type
allocator_type;
//为了严格说明_Alloc_traits<_Tp, _Allocator>::allocator_type 是一种类型，所以加上
typename
```

#### 自定义打印模板（方便调用）

```cpp
template <typename Container>
void display(const Container &con) {
    for(auto &elem : con) {
        cout << elem << "  ";
    }
    cout << endl;
}
```

# 1、容器

## 1. 序列式容器

序列式容器的初始化和遍历

```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <list>

using std::cout;
using std::endl;
using std::vector;
using std::deque;
using std::list;

void test() {
    // 初始化
    /* vector<int> number(10, 4);//1、传count个value */
    /* int arr[10] = {1, 3, 7, 9, 6, 5, 3, 2, 6, 1}; */
    /* vector<int> number(arr, arr + 10);//2、迭代器范围的[arr, arr + 10) */
    vector<int> number = {1, 3, 5, 7, 9, 8, 6, 4, 2, 1};//3、大括号形式

    //遍历
    for(size_t idx = 0; idx != number.size(); ++idx) {
        cout << number[idx] << "  ";
    }
    cout << endl;

    vector<int>::iterator it;
    for(it = number.begin(); it != number.end(); ++it) {
        cout << *it << "  ";
    }
    cout << endl;

    vector<int>::iterator it2 = number.begin();
    for(; it2 != number.end(); ++it2) {
        cout << *it2 << "  ";
    }
    cout << endl;

    for(auto &elem : number) {
        cout << elem << "  ";
    }
    cout << endl;
}

void test2() {
    //初始化
    /* deque<int> number(10, 4);//1、传count个value */
    /* int arr[10] = {1, 3, 7, 9, 6, 5, 3, 2, 6, 1}; */
    /* deque<int> number(arr, arr + 10);//2、迭代器范围的[arr, arr + 10) */
    deque<int> number = {1, 3, 5, 7, 9, 8, 6, 4, 2, 1};//3、大括号形式

    //遍历
    for(size_t idx = 0; idx != number.size(); ++idx) {
        cout << number[idx] << "  ";
    }
    cout << endl;

    deque<int>::iterator it;
    for(it = number.begin(); it != number.end(); ++it) {
        cout << *it << "  ";
    }
    cout << endl;

    deque<int>::iterator it2 = number.begin();
    for(; it2 != number.end(); ++it2) {
        cout << *it2 << "  ";
    }
    cout << endl;

    for(auto &elem : number) {
        cout << elem << "  ";
    }
    cout << endl;
}

void test3() {
    //初始化
    /* list<int> number(10, 4);//1、传count个value */
    /* int arr[10] = {1, 3, 7, 9, 6, 5, 3, 2, 6, 1}; */
    /* list<int> number(arr, arr + 10);//2、迭代器范围的[arr, arr + 10) */
    list<int> number = {1, 3, 5, 7, 9, 8, 6, 4, 2, 1};//3、大括号形式

    //遍历
    //使用下标进行初始化的方式，error
    /* for(size_t idx = 0; idx != number.size(); ++idx) */
    /* { */
    /*     cout << number[idx] << "  "; */
    /* } */
    /* cout << endl; */

    list<int>::iterator it;
    for(it = number.begin(); it != number.end(); ++it) {
        cout << *it << "  ";
    }
    cout << endl;

    list<int>::iterator it2 = number.begin();
    for(; it2 != number.end(); ++it2) {
        cout << *it2 << "  ";
    }
    cout << endl;

    for(auto &elem : number) {
        cout << elem << "  ";
    }
    cout << endl;
}
int main(int argc, char **argv) {
    test();

    cout << endl << "测试deque" << endl;
    test2();

    cout << endl << "测试list" << endl;
    test3();
    return 0;
}
```

序列式容器的插入等常用操作

```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <list>

using std::cout;
using std::endl;
using std::vector;
using std::deque;
using std::list;

template <typename Container>
void display(const Container &con){
    for(auto &elem : con)    {
        cout << elem << "  ";
    }
    cout << endl;
}

class Point{
public:
    Point(int ix = 0, int iy = 0)
    : _ix(ix)
    , _iy(iy)    {
        cout << "Point(int = 0, int = 0)" << endl;
    }

    void print() const    {
        cout << "(" << _ix
             << ", " << _iy
             << ")" << endl;
    }

    ~Point()    {
        cout << "~Point()" << endl;
    }

private:
    int _ix;
    int _iy;
};

void test00() {
    vector<Point> vec;
    /* vec.push_back(Point(1, 2)); */
    vec.emplace_back(1, 3);
}
void test() {
    cout << "sizeof(vector<int>) = " << sizeof(vector<int>) << endl;
    cout << "sizeof(vector<char>) = " << sizeof(vector<char>) << endl << endl;

    vector<int> number = {1, 3, 5, 7, 9, 4, 8, 6};
    display(number);
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;

    cout << endl << "在vector的尾部进行插入与删除" << endl;
    number.push_back(100);
    number.push_back(200);
    display(number);
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;
    number.pop_back();
    display(number);
    number.shrink_to_fit();
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;

    //为什么vector不支持在头部与尾部进行插入与删除？
    //插入与删除第一个元素的时候，都会将后面元素进行挪动，时间
    //复杂度O(N)
    &number;//得不到第一个元素的地址
    &number[0];
    &*number.begin();//_M_start

    /* vector<int>::iterator it3 = number.begin(); */
    /* *it3 = 100; */
    /* vector<int>::const_iterator cit = number.begin(); */
    /* *cit = 100;//error */

    cout << endl << "在vector的中间进行插入" << endl;
    auto cit = number.begin();
    ++cit;
    ++cit;
    cout << "*cit = " << *cit << endl;
    auto it = number.insert(cit, 300);
    display(number);
    cout << "*it = " << *it << endl;
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;

    cout << endl;
    //迭代器已经失效了（在进行insert操作的时候，底层已经发生了扩容）
    //解决方案：每次进行insert之后，将迭代器重新置位
    it = number.insert(it, 30, 200);
    display(number);
    /* cout << "*it = " << *it << endl; */
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;

    cout << endl;
    vector<int> vec = {100, 500, 600, 1000};
    /* it = number.begin();//迭代器重新置位的一种方式 */
    number.insert(it, vec.begin(), vec.end());
    display(number);
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;

    cout << endl << "vector中元素的清空" << endl;
    number.clear();//清空元素
    number.shrink_to_fit();
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;

    vector<int> vec1{1, 3, 5, 7};
    vector<int> vec2{3, 4, 5, 6};
    if(vec1 == vec2) {

    }
}

void test2() {
    deque<int> number = {1, 3, 5, 7, 9, 4, 8, 6};
    display(number);

    cout << endl << "在deque的尾部进行插入与删除" << endl;
    number.push_back(100);
    number.push_back(200);
    display(number);
    number.pop_back();
    display(number);

    cout << endl << "在deque的头部进行插入与删除" << endl;
    number.push_front(1111);
    number.push_front(2222);
    display(number);
    number.pop_front();
    display(number);

    cout << endl << "在deque的中间进行插入" << endl;
    auto cit = number.begin();
    ++cit;
    ++cit;
    cout << "*cit = " << *cit << endl;
    auto it = number.insert(cit, 300);
    display(number);
    cout << "*it = " << *it << endl;

    cout << endl;
    it = number.insert(it, 3, 200);
    display(number);
    cout << "*it = " << *it << endl;

    cout << endl;
    vector<int> vec = {100, 500, 600, 1000};
    number.insert(it, vec.begin(), vec.end());
    display(number);

    cout << endl << "deque中元素的清空" << endl;
    number.clear();//清空元素
    number.shrink_to_fit();
    cout << "number.size() = " << number.size() << endl;
}

void test3() {
    list<int> number = {1, 3, 5, 7, 9, 4, 8, 6};
    display(number);

    cout << endl << "在list的尾部进行插入与删除" << endl;
    number.push_back(100);
    number.push_back(200);
    display(number);
    number.pop_back();
    display(number);

    cout << endl << "在list的头部进行插入与删除" << endl;
    number.push_front(1111);
    number.push_front(2222);
    display(number);
    number.pop_front();
    display(number);

    cout << endl << "在list的中间进行插入" << endl;
    auto cit = number.begin();
    ++cit;
    ++cit;
    cout << "*cit = " << *cit << endl;
    auto it = number.insert(cit, 300);
    display(number);
    cout << "*it = " << *it << endl;

    cout << endl;
    number.insert(it, 30, 200);
    display(number);
    /* cout << "*it = " << *it << endl; */

    cout << endl;
    vector<int> vec = {100, 500, 600, 1000};
    number.insert(it, vec.begin(), vec.end());
    display(number);

    cout << endl << "list中元素的清空" << endl;
    number.clear();//清空元素
    cout << "number.size() = " << number.size() << endl;
}
int main(int argc, char **argv) {
    test00();

    cout << endl << "测试vector" << endl;
    test();

    cout << endl << "测试deque" << endl;
    test2();

    cout << endl << "测试list" << endl;
    test3();
    return 0;
}
```

### `vector`

![image-20220605232452303.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654702622512-7606cabf-7afe-4d52-b18f-c98982639e25.png)

```cpp
typedef _Tp value_type;
typedef value_type* pointer;
typedef const value_type* const_pointer;
typedef value_type* iterator;
typedef const value_type* const_iterator;
typedef value_type& reference;
typedef const value_type& const_reference;
typedef size_t size_type;
typedef ptrdiff_t difference_type;
//直接获取容器的size_type
Container<T>::iterator
//类型萃取
```

```cpp
#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

template <typename Container>
void display(const Container &con) {
    for(auto &elem : con) {
        cout << elem << "  ";
    }
    cout << endl;
}

void test() {
    vector<int> number = {1, 3, 5, 7, 9, 4, 8, 6};
    display(number);
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;

    cout << endl << "在vector的尾部进行插入" << endl;
    number.push_back(100);
    number.push_back(200);
    display(number);
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;

    cout << endl << "在vector的中间进行插入" << endl;
    auto cit = number.begin();
    ++cit;
    ++cit;
    cout << "*cit = " << *cit << endl;
    auto it = number.insert(cit, 300);
    display(number);
    cout << "*it = " << *it << endl;
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;

    //因为push_back每次插入的元素的个数是一个，所以按照两倍的
    //扩容方式是没有问题的，但是因为insert每次插入元素的个数是
    //不确定的，所以扩容方式也是不固定的，insert扩容就麻烦一些
    //size() = t, capacity() = n, 插入的元素个数m
    //1、m <= n - t,此时不需要进行扩容
    //2、n -t < m < t, 此时是2 * t进行扩容操作
    //3、n - t < m, t < m < n 此时是t + m进行扩容操作
    //4、n - t < m, m > n 此时是t + m进行扩容操作
    cout << endl;
    it = number.insert(it, 50, 200);
    display(number);
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;

    cout << endl;
    vector<int> vec = {100, 500, 600, 1000};
    number.insert(it, vec.begin(), vec.end());
    display(number);
    cout << "number.size() = " << number.size() << endl;
    cout << "number.capacity() = " << number.capacity() << endl;
}

int main(int argc, char **argv) {
    test();

    return 0;
}
```

```cpp
#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

template <typename Container>
void display(const Container &con){
    for(auto &elem : con) {
        cout << elem << "  ";
    }
    cout << endl;
}

void test() {
    vector<int> number = {1, 5, 6, 6, 6, 7, 9};
    display(number);

    cout << endl;
    //删除所有的重复的6
    for(auto it = number.begin(); it != number.end();  ++it; ) {
        if(6 == *it) {
            number.erase(it);
        }
       // 与预期不同，删除后，容器自动前移，但是程序员仍然自增，后移了一位
    }
    display(number);
}

void test2() {
    vector<int> number = {1, 5, 6, 6, 6, 7, 9};
    display(number);

    cout << endl;
    //删除所有的重复的6
    for(auto it = number.begin(); it != number.end(); ) {
        if(6 == *it) {
            it = number.erase(it);
        }
        else {
            ++it;
        }
    }
    display(number);
}

int main(int argc, char **argv) {
    test2();
    return 0;
}
```

迭代器失效的情况：

- 底层扩容，可能指向原来的位置，发生错误
- 删除单个元素导致剩余元素自动前移，但是程序员自加，跳过了某些元素

### `deque`

![image-20220605232534904.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1654702612745-d85d9e82-8d81-4f5d-830d-df1c3e3fcf85.png)

同`vector`

### `list`

```cpp
#include <iostream>
#include <list>

using std::cout;
using std::endl;
using std::list;

template <typename Container>
void display(const Container &con) {
    for(auto &elem : con) {
        cout << elem << "  ";
    }
    cout << endl;
}

template <typename T>
struct Com {
    bool operator()(const T &lhs, const T &rhs) const {
        return lhs < rhs;
    }
};

void test() {
    list<int> number = {1, 3, 7, 9, 7, 9, 3, 1, 4, 2, 8};
    display(number);

    cout << endl << "list的unique测试" << endl;
    number.unique();
    display(number);

    cout << endl << "list的逆置" << endl;
    number.reverse();
    display(number);

    cout << endl << "链表的排序" << endl;
    /* number.sort(); */
    /* number.sort(std::less<int>()); */
    /* number.sort(std::greater<int>()); */
    number.sort(Com<int>());
    display(number);

    cout << endl << "list的unique测试" << endl;
    number.unique();
    display(number);

    cout << endl << "链表的merge操作" << endl;
    list<int> lst1 = {1, 3, 7, 9, 4};
    list<int> lst2 = {8, 30, 70, 90, 40};
    lst1.sort();
    lst2.sort();
    display(lst1);
    display(lst2);
    lst1.merge(lst2);
    display(lst1);
    display(lst2);

    cout << endl << "链表的splice使用" << endl;
    list<int>  lst3 = {1, 4, 7, 9, 3};
    list<int>  lst4 = {5, 8, 10, 20, 2};
    auto cit = lst3.begin();
    ++cit;
    cout << "*cit = " << *cit << endl;
    auto it = lst4.end();
    --it;
    cout << "*it = " << *it << endl;
    lst3.splice(cit, lst4, it);
    display(lst3);
    display(lst4);

    cout << endl;
    list<int> lst5 = {1, 3, 7, 9, 20, 90, 30, 70};
    display(lst5);
    auto it2 = lst5.begin();
    ++it2;
    ++it2;
    cout << "*it2 = " << *it2 << endl;
    auto it3 = lst5.end();
    --it3;
    cout << "*it3 = " << *it3 << endl;
    lst5.splice(it2, lst5, it3);
    display(lst5);
}

int main(int argc, char **argv) {
    test();
    return 0;
}
```

## 2. 关联式容器(红黑树)

### `set`  Key值唯一（ 不支持下标访问 、不支持修改）

```cpp
#include <math.h>

#include <iostream>
#include <set>
#include <vector>

using std::cout;
using std::endl;
using std::set;
using std::vector;

template <typename Container>
void display(const Container &con) {
    for (auto &elem : con) {
        cout << elem << "  ";
    }
    cout << endl;
}
void test() {
    // set的特征
    // 1、key值是唯一的，不能重复
    // 2、默认情况下，会按照key值进行升序排列
    // 3、底层使用红黑树
    set<int> number = {1, 3, 5, 2, 3, 5, 7, 9, 4, 5};
    /* set<int, std::greater<int>> number = {1, 3, 5, 2, 3, 5, 7, 9, 4, 5}; */
    display(number);

    cout << endl
         << "set的查找操作" << endl;
    size_t cnt1 = number.count(3);
    size_t cnt2 = number.count(10);
    cout << "cnt1 = " << cnt1 << endl
         << "cnt2 = " << cnt2 << endl;

    auto it = number.find(5);
    if (it != number.end()) {
        cout << "*it = " << *it << endl;
    } else {
        cout << "查找失败，该元素不存在" << endl;
    }

    cout << endl
         << "set的插入操作" << endl;
    /* auto it2 = number.insert(8); */
    std::pair<set<int>::iterator, bool> ret = number.insert(8);
    if (ret.second) {
        cout << "该元素插入成功" << *ret.first << endl;
    } else {
        cout << "插入失败,该元素存在set中" << endl;
    }

    cout << endl;
    vector<int> vec = {10, 3, 6, 20, 50};
    number.insert(vec.begin(), vec.end());  //迭代器范围进行插入
    display(number);

    cout << endl;
    number.insert({1, 0, 100, 300});
    display(number);

    cout << endl
         << "set的删除操作" << endl;
    number.erase(10);
    display(number);
    it = number.begin();
    ++it;
    number.erase(it);
    display(number);

    cout << endl
         << "set的下标访问" << endl;
    /* cout << "number[0] = " << number[0] << endl; //error,不支持下标*/

    cout << endl
         << "set的修改操作" << endl;
    auto it3 = number.begin();
    cout << "*it3 = " << *it3 << endl;
    /* *it3 = 200;//set是不支持修改的 */
}

class Point {
public:
    Point(int ix = 0, int iy = 0)
        : _ix(ix), _iy(iy) {
        /* cout << "Point(int = 0, int = 0)" << endl; */
    }

    double getDistance() const {
        return hypot(_ix, _iy);
    }

    ~Point() {
        /* cout << "~Point()" << endl; */
    }

    friend bool operator<(const Point &lhs, const Point &rhs);
    friend bool operator>(const Point &lhs, const Point &rhs);

    friend std::ostream &operator<<(std::ostream &os, const Point &rhs);

    friend struct Comparetion;  //声明为Point的友元

private:
    int _ix;
    int _iy;
};

std::ostream &operator<<(std::ostream &os, const Point &rhs) {
    os << "(" << rhs._ix
       << ", " << rhs._iy
       << ")";

    return os;
}

//点到原点的距离作为大小的比较
bool operator<(const Point &lhs, const Point &rhs) {
    if (lhs.getDistance() < rhs.getDistance()) {
        return true;
    } else if (lhs.getDistance() == rhs.getDistance()) {
        if (lhs._ix < rhs._ix) {
            return true;
        } else if (lhs._ix == rhs._ix) {
            if (lhs._iy < rhs._iy) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
}

bool operator>(const Point &lhs, const Point &rhs) {
    cout << "bool operator>(const Point &, const Point &)" << endl;
    if (lhs.getDistance() > rhs.getDistance()) {
        return true;
    } else if (lhs.getDistance() == rhs.getDistance()) {
        if (lhs._ix > rhs._ix) {
            return true;
        } else if (lhs._ix == rhs._ix) {
            if (lhs._iy > rhs._iy) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
}

struct Comparetion {
    bool operator()(const Point &lhs, const Point &rhs) const {
        cout << "bool operator()(const Point &, const Point &) const" << endl;
        if (lhs.getDistance() < rhs.getDistance()) {
            return true;
        } else if (lhs.getDistance() == rhs.getDistance()) {
            if (lhs._ix < rhs._ix) {
                return true;
            } else if (lhs._ix == rhs._ix) {
                if (lhs._iy < rhs._iy) {
                    return true;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
};
void test2() {
    /* set<Point, Comparetion> number = { */
    set<Point, std::greater<Point>> number = {
        Point(1, 2),
        Point(1, -2),
        Point(-1, -2),
        Point(-1, 3),
        Point(0, 0),
        Point(3, 2),
        Point(4, 5),
        Point(1, 2),
    };
    display(number);
}

int main(int argc, char **argv) {
    test2();
    return 0;
}
```

`set`对于自定义类型 必须重载 自定义类型的 `<` ( `std::less`调用 )  和  `>`  ( `std::greater`调用 )     或者    自己写一个 `**struct Compare( bool operator()(const T &lhs, const T &rhs))**` 。

### `multiset` Key值不唯一，可以重复（ 不支持下标访问 、不支持修改）

```cpp
#include <math.h>

#include <iostream>
#include <set>
#include <vector>

using std::cout;
using std::endl;
using std::multiset;
using std::vector;

template <typename Container>
void display(const Container &con) {
    for (auto &elem : con) {
        cout << elem << "  ";
    }
    cout << endl;
}
void test() {
    // multiset的特征
    // 1、key值是不唯一的，可以重复
    // 2、默认情况下，会按照key值进行升序排列
    // 3、底层使用红黑树
    multiset<int> number = {1, 3, 5, 2, 3, 5, 7, 9, 4, 5};
    /* multiset<int, std::greater<int>> number = {1, 3, 5, 2, 3, 5, 7, 9, 4, 5}; */
    display(number);

    cout << endl
         << "multiset的查找操作" << endl;
    size_t cnt1 = number.count(3);
    size_t cnt2 = number.count(10);
    cout << "cnt1 = " << cnt1 << endl
         << "cnt2 = " << cnt2 << endl;

    auto it = number.find(5);
    if (it != number.end()) {
        cout << "*it = " << *it << endl;
    } else {
        cout << "查找失败，该元素不存在" << endl;
    }

    cout << endl
         << "测试multiset的xxx_bound" << endl;
    auto itt1 = number.lower_bound(5);
    cout << "*itt1 = " << *itt1 << endl;
    auto itt2 = number.upper_bound(5);
    cout << "*itt2 = " << *itt2 << endl;
    while (itt1 != itt2) {
        cout << *itt1 << "  ";
        ++itt1;
    }
    cout << endl;

    /* auto ret2 = number.equal_range(5); */
    std::pair<multiset<int>::iterator, multiset<int>::iterator>
        ret2 = number.equal_range(5);
    while (ret2.first != ret2.second) {
        cout << *ret2.first << "  ";
        ++ret2.first;
    }
    cout << endl;

    cout << endl
         << "multiset的插入操作" << endl;
    /* auto it2 = number.insert(8); */
    number.insert(8);
    display(number);

    cout << endl;
    vector<int> vec = {10, 3, 6, 6, 20, 50};
    number.insert(vec.begin(), vec.end());  //迭代器范围进行插入
    display(number);

    cout << endl;
    number.insert({1, 0, 100, 300, 100});
    display(number);

    cout << endl
         << "multiset的删除操作" << endl;
    number.erase(10);
    display(number);
    it = number.begin();
    ++it;
    number.erase(it);
    display(number);

    cout << endl
         << "multiset的下标访问" << endl;
    /* cout << "number[0] = " << number[0] << endl; //error,不支持下标 */

    cout << endl
         << "multiset的修改操作" << endl;
    auto it3 = number.begin();
    cout << "*it3 = " << *it3 << endl;
    /* *it3 = 200;//multiset是不支持修改的 */
}

class Point {
public:
    Point(int ix = 0, int iy = 0)
        : _ix(ix), _iy(iy) {
        /* cout << "Point(int = 0, int = 0)" << endl; */
    }

    double getDistance() const {
        return hypot(_ix, _iy);
    }

    ~Point() {
        /* cout << "~Point()" << endl; */
    }

    friend bool operator<(const Point &lhs, const Point &rhs);
    friend bool operator>(const Point &lhs, const Point &rhs);

    friend std::ostream &operator<<(std::ostream &os, const Point &rhs);

    friend struct Comparetion;  //声明为Point的友元

private:
    int _ix;
    int _iy;
};

std::ostream &operator<<(std::ostream &os, const Point &rhs) {
    os << "(" << rhs._ix
       << ", " << rhs._iy
       << ")";

    return os;
}

//点到原点的距离作为大小的比较
bool operator<(const Point &lhs, const Point &rhs) {
    if (lhs.getDistance() < rhs.getDistance()) {
        return true;
    } else if (lhs.getDistance() == rhs.getDistance()) {
        if (lhs._ix < rhs._ix) {
            return true;
        } else if (lhs._ix == rhs._ix) {
            if (lhs._iy < rhs._iy) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
}

bool operator>(const Point &lhs, const Point &rhs) {
    cout << "bool operator>(const Point &, const Point &)" << endl;
    if (lhs.getDistance() > rhs.getDistance()) {
        return true;
    } else if (lhs.getDistance() == rhs.getDistance()) {
        if (lhs._ix > rhs._ix) {
            return true;
        } else if (lhs._ix == rhs._ix) {
            if (lhs._iy > rhs._iy) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
}

struct Comparetion {
    bool operator()(const Point &lhs, const Point &rhs) const {
        cout << "bool operator()(const Point &, const Point &) const" << endl;
        if (lhs.getDistance() < rhs.getDistance()) {
            return true;
        } else if (lhs.getDistance() == rhs.getDistance()) {
            if (lhs._ix < rhs._ix) {
                return true;
            } else if (lhs._ix == rhs._ix) {
                if (lhs._iy < rhs._iy) {
                    return true;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
};
void test2() {
    /* multiset<Point> number = { */
    multiset<Point, Comparetion> number = {
        /* multiset<Point, std::greater<Point>> number = { */
        Point(1, 2),
        Point(1, -2),
        Point(-1, -2),
        Point(-1, 3),
        Point(0, 0),
        Point(3, 2),
        Point(4, 5),
        Point(1, -2),
        Point(1, 2),
    };
    display(number);
}

int main(int argc, char **argv) {
    test2();
    return 0;
}
```

`set`与`multiset`的初始化、遍历、查找、删除的使用都一样，都不支持下标访问、都不支持修改。对于 insert插入而言，`multiset`肯定可以插入成功，所以二者返回类型不一样，至于插入迭代器返回与大括号类型都是一样的。

`lower_bound`  第一个小于等于给定Key值的迭代器

`upper_bound`   第一个大于等于给定Key值的迭代器

`equal_range`   返回一个`pair`   ： `first`指向第一个小于等于给定Key值的迭代器，`second`指向第一个大于等于给定Key值的迭代器

### `map`  Key值唯一，默认升序

```cpp
#include <math.h>

#include <iostream>
#include <map>
#include <string>
#include <utility>

using std::cout;
using std::endl;
using std::make_pair;
using std::map;
using std::pair;
using std::string;

template <typename Container>
void display(const Container &con) {
    for (auto &elem : con) {
        cout << elem.first << "  " << elem.second << endl;
    }
}

void test() {
    // map的特征
    // 1、存放的元素是一个pair类型，key与value值，key是唯一的，不能重复
    ///但是value值重复与否是没有关系的
    // 2、默认情况下，会按照key值进行升序排列
    // 3、底层实现是红黑树
    map<int, string> number = {
        {3, "武汉"},
        {5, "上海"},
        {3, "武汉"},
        pair<int, string>(4, "北京"),
        pair<int, string>(5, "天津"),
        pair<int, string>(4, "北京"),
        make_pair(2, "南京"),
        make_pair(6, "南京")};
    display(number);

    cout << endl
         << "map的下标访问" << endl;
    cout << "number[2] = " << number[2] << endl;
    cout << "number[1] = " << number[1] << endl;
    display(number);
    cout << endl
         << endl;
    number[1] = "东京";
    number[6] = "东京";
    display(number);
}

class Point {
public:
    Point(int ix = 0, int iy = 0)
        : _ix(ix), _iy(iy) {
        /* cout << "Point(int = 0, int = 0)" << endl; */
    }

    double getDistance() const {
        return hypot(_ix, _iy);
    }

    ~Point() {
        /* cout << "~Point()" << endl; */
    }

    friend std::ostream &operator<<(std::ostream &os, const Point &rhs);

private:
    int _ix;
    int _iy;
};

std::ostream &operator<<(std::ostream &os, const Point &rhs) {
    os << "(" << rhs._ix
       << ", " << rhs._iy
       << ")";

    return os;
}

void test2() {
    map<string, Point> number = {
        {"wuhan", Point(1, 2)},
        {"hubei", Point(1, -2)},
        pair<string, Point>("nanjing", Point(1, 2)),
        pair<string, Point>("wuhan", Point(10, 2)),
        make_pair("dongjing", Point(3, 4)),
        make_pair("tianjin", Point(2, 3)),
    };
    display(number);

    cout << endl
         << "map的查找操作" << endl;
    size_t cnt1 = number.count("wuhan");
    size_t cnt2 = number.count("wuhan2");
    cout << "cnt1 = " << cnt1 << endl;
    cout << "cnt2 = " << cnt2 << endl;

    auto it = number.find("tianjin");
    if (it != number.end()) {
        cout << "查找成功 " << it->first
             << "  " << it->second << endl;
    } else {
        cout << "查找失败，该元素存在map中" << endl;
    }

    cout << endl
         << "map的插入操作" << endl;
    /* pair<map<string,Point>::iterator, bool> ret = */
    /*     number.insert(pair<string, Point>("hubei2", Point(2, 3))); */
    /* auto ret = number.insert(make_pair("hubei2", Point(2, 3))); */
    auto ret = number.insert({"hubei2", Point(2, 3)});

    if (ret.second) {
        cout << "插入成功 " << ret.first->first << "   "
             << ret.first->second << endl;
    } else {
        cout << "插入失败,该元素存在map中" << endl;
    }
    display(number);

    cout << endl
         << "map的下标访问" << endl;
    cout << "number[\"dongjing\"] = " << number["dongjing"] << endl;
    cout << "number[\"1\"] = " << number["1"] << endl;

    number["1"] = Point(2, 4);
    display(number);
}

int main(int argc, char **argv) {
    test2();
    return 0;
}
```

### `multimap` Key值不唯一，可以重复（ 不支持下标访问 ）

```cpp
#include <math.h>

#include <iostream>
#include <map>
#include <string>
#include <utility>

using std::cout;
using std::endl;
using std::make_pair;
using std::multimap;
using std::pair;
using std::string;

template <typename Container>
void display(const Container &con) {
    for (auto &elem : con) {
        cout << elem.first << "  " << elem.second << endl;
    }
}

void test() {
    // multimap的特征
    // 1、存放的元素是一个pair类型，key与value值，key是不唯一的，可以重复
    ///但是value值重复与否是没有关系的
    // 2、默认情况下，会按照key值进行升序排列
    // 3、底层实现是红黑树
    multimap<int, string> number = {
        /* multimap<int, string, std::greater<int>> number = { */
        {3, "武汉"},
        {5, "上海"},
        {3, "武汉"},
        pair<int, string>(4, "北京"),
        pair<int, string>(5, "天津"),
        pair<int, string>(4, "北京"),
        make_pair(2, "南京"),
        make_pair(6, "南京")};
    display(number);
#if 0
    cout << endl << "multimap的下标访问" << endl;
    cout << "number[2] = " << number[2] << endl;
    cout << "number[1] = " << number[1] << endl;
    display(number);
    cout << endl << endl;
    number[1] = "东京";
    number[6] = "东京";
    display(number);
#endif
}

class Point {
public:
    Point(int ix = 0, int iy = 0)
        : _ix(ix), _iy(iy) {
        /* cout << "Point(int = 0, int = 0)" << endl; */
    }

    double getDistance() const {
        return hypot(_ix, _iy);
    }

    ~Point() {
        /* cout << "~Point()" << endl; */
    }

    friend std::ostream &operator<<(std::ostream &os, const Point &rhs);

private:
    int _ix;
    int _iy;
};

std::ostream &operator<<(std::ostream &os, const Point &rhs) {
    os << "(" << rhs._ix
       << ", " << rhs._iy
       << ")";

    return os;
}

void test2() {
    multimap<string, Point> number = {
        {"wuhan", Point(1, 2)},
        {"hubei", Point(1, -2)},
        pair<string, Point>("nanjing", Point(1, 2)),
        pair<string, Point>("wuhan", Point(10, 2)),
        make_pair("dongjing", Point(3, 4)),
        make_pair("tianjin", Point(2, 3)),
    };
    display(number);

    cout << endl
         << "multimap的查找操作" << endl;
    size_t cnt1 = number.count("wuhan");
    size_t cnt2 = number.count("wuhan2");
    cout << "cnt1 = " << cnt1 << endl;
    cout << "cnt2 = " << cnt2 << endl;

    auto it = number.find("tianjin");
    if (it != number.end()) {
        cout << "查找成功 " << it->first
             << "  " << it->second << endl;
    } else {
        cout << "查找失败，该元素存在multimap中" << endl;
    }

    cout << endl
         << "multimap的插入操作" << endl;
#if 1
    number.insert(pair<string, Point>("hubei2", Point(2, 3)));
    /* number.insert(make_pair("hubei2", Point(2, 3))); */
    /* number.insert({"hubei2", Point(2, 3)}); */
    display(number);

    cout << endl
         << "multimap是不支持下标访问" << endl;
    /* cout << "number[\"dongjing\"] = " << number["dongjing"] << endl; */
    /* cout << "number[\"1\"] = " << number["1"] << endl; */

    /* number["1"] = Point(2, 4); */
    /* display(number); */
#endif
}

int main(int argc, char **argv) {
    test2();
    return 0;
}
```

## 3. 无序关联式容器（哈希表）

底层实现是哈希表

#### `unodered_set`   不支持下标访问  不支持修改

```cpp
template<
    class Key,
    class Hash = std::hash<Key>,
    class KeyEqual = std::equal_to<Key>,
    class Allocator = std::allocator<Key>
> class unordered_set;
```

委托构造函数

```cpp
//委托构造函数
unordered_set()
: unordered_set( size_type(/*implementation-defined*/) ) {
    //初始化列表
}
```

```cpp
#include <iostream>
#include <unordered_set>

using std::cout;
using std::endl;
using std::unordered_set;

template <typename Container>
void display(const Container &con) {
    for (auto &elem : con) {
        cout << elem << "  ";
    }
    cout << endl;
}

void test() {
    // unordered_set的特征
    // 1、key值是唯一，不能重复
    // 2、key值是没有顺序的
    // 3、底层使用的是哈希
    unordered_set<int> number = {1, 3, 5, 7, 9, 6, 4, 2, 3, 1, 3};
    display(number);

    /* auto it = number.begin(); */
    /* *it = 100; */
}

class Point {
public:
    Point(int ix = 0, int iy = 0)
        : _ix(ix), _iy(iy) {
        /* cout << "Point(int = 0, int = 0)" << endl; */
    }

    int getX() const {
        return _ix;
    }

    int getY() const {
        return _iy;
    }

    /* double getDistance() const */
    /* { */
    /*     return hypot(_ix, _iy); */
    /* } */

    ~Point() {
        /* cout << "~Point()" << endl; */
    }

    friend std::ostream &operator<<(std::ostream &os, const Point &rhs);

private:
    int _ix;
    int _iy;
};

std::ostream &operator<<(std::ostream &os, const Point &rhs) {
    os << "(" << rhs._ix
       << ", " << rhs._iy
       << ")";

    return os;
}

//函数对象
struct HashPoint {
    size_t operator()(const Point &rhs) const {
        cout << "size_t operator()(const Point &) const" << endl;
        //哈希函数的设计
        return (rhs.getX() << 1) ^ (rhs.getY() << 2);
    }
};

//标准命名空间std中的类模板hash的全特化版本
namespace std {

//模板的特化（全特化）
template <>
struct hash<Point> {
    size_t operator()(const Point &rhs) const {
        cout << "size_t std::hash::operator()(const Point &) const " << endl;
        return (rhs.getX() << 1) ^ (rhs.getY() << 2);
    }
};

}  // end of namespace std

#if 1
// std::equal_to
bool operator==(const Point &lhs, const Point &rhs) {
    cout << "bool operator==(const Point &, const Point &)" << endl;
    return ((lhs.getX() == rhs.getX()) && (lhs.getY() == rhs.getY()));
}
#endif

namespace std {

// equal_to的特化
template <>
struct equal_to<Point> {
    bool operator()(const Point &lhs, const Point &rhs) const {
        cout << "bool std::equal_to " << endl;
        return ((lhs.getX() == rhs.getX()) && (lhs.getY() == rhs.getY()));
    }
};

};  // namespace std

void test2() {
    /* unordered_set<Point, HashPoint> number = { */
    unordered_set<Point> number = {
        Point(1, 2),
        Point(1, 2),
        Point(1, -2),
        Point(3, 2),
        Point(-1, 4),
        Point(-10, -2),
    };
    display(number);

    cout << endl
         << "unordered_set的下标访问" << endl;
    /* cout << "number[] = " << number[Point(1, 2)] << endl; */

    cout << endl
         << endl;
    auto it = number.begin();
    /* *it = Point(1, 2); */
}
int main(int argc, char **argv) {
    test2();
    return 0;
}
```

#### `unodered_map`   不支持下标访问  不支持修改

```cpp
template<
    class Key,
    class Hash = std::hash<Key>,
    class KeyEqual = std::equal_to<Key>,
    class Allocator = std::allocator<Key>
> class unordered_set;
```

```cpp
#include <math.h>

#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>

using std::cout;
using std::endl;
using std::make_pair;
using std::pair;
using std::string;
using std::unordered_map;

template <typename Container>
void display(const Container &con) {
    for (auto &elem : con) {
        cout << elem.first << "  " << elem.second << endl;
    }
}

void test() {
    // unordered_map的特征
    // 1、存放的元素是一个pair类型，key与value值，key是唯一的，不能重复
    ///但是value值重复与否是没有关系的
    // 2、不会按照key值进行排序
    // 3、底层实现是哈希表
    unordered_map<int, string> number = {
        {3, "武汉"},
        {5, "上海"},
        {3, "武汉"},
        pair<int, string>(4, "北京"),
        pair<int, string>(5, "天津"),
        pair<int, string>(4, "北京"),
        make_pair(2, "南京"),
        make_pair(6, "南京")};
    display(number);

    cout << endl
         << "unordered_map的下标访问" << endl;
    cout << "number[2] = " << number[2] << endl;
    cout << "number[1] = " << number[1] << endl;
    display(number);
    cout << endl
         << endl;
    number[1] = "东京";
    number[6] = "东京";
    display(number);
}

class Point {
public:
    Point(int ix = 0, int iy = 0)
        : _ix(ix), _iy(iy) {
        /* cout << "Point(int = 0, int = 0)" << endl; */
    }

    double getDistance() const {
        return hypot(_ix, _iy);
    }

    ~Point() {
        /* cout << "~Point()" << endl; */
    }

    friend std::ostream &operator<<(std::ostream &os, const Point &rhs);

private:
    int _ix;
    int _iy;
};

std::ostream &operator<<(std::ostream &os, const Point &rhs) {
    os << "(" << rhs._ix
       << ", " << rhs._iy
       << ")";

    return os;
}

void test2() {
    unordered_map<string, Point> number = {
        {"wuhan", Point(1, 2)},
        {"hubei", Point(1, -2)},
        pair<string, Point>("nanjing", Point(1, 2)),
        pair<string, Point>("wuhan", Point(10, 2)),
        make_pair("dongjing", Point(3, 4)),
        make_pair("tianjin", Point(2, 3)),
    };
    display(number);

    cout << endl
         << "unordered_map的查找操作" << endl;
    size_t cnt1 = number.count("wuhan");
    size_t cnt2 = number.count("wuhan2");
    cout << "cnt1 = " << cnt1 << endl;
    cout << "cnt2 = " << cnt2 << endl;

    auto it = number.find("tianjin");
    if (it != number.end()) {
        cout << "查找成功 " << it->first
             << "  " << it->second << endl;
    } else {
        cout << "查找失败，该元素存在unordered_map中" << endl;
    }

    cout << endl
         << "unordered_map的插入操作" << endl;
    /* pair<unordered_map<string,Point>::iterator, bool> ret = */
    /*     number.insert(pair<string, Point>("hubei2", Point(2, 3))); */
    /* auto ret = number.insert(make_pair("hubei2", Point(2, 3))); */
    auto ret = number.insert({"hubei2", Point(2, 3)});

    if (ret.second) {
        cout << "插入成功 " << ret.first->first << "   "
             << ret.first->second << endl;
    } else {
        cout << "插入失败,该元素存在unordered_map中" << endl;
    }
    display(number);

    cout << endl
         << "unordered_map的下标访问" << endl;
    cout << "number[\"dongjing\"] = " << number["dongjing"] << endl;
    cout << "number[\"1\"] = " << number["1"] << endl;

    number["1"] = Point(2, 4);
    display(number);
}

int main(int argc, char **argv) {
    test();
    return 0;
}
```

### 方式一：

自实现 `Hash` ( `std::hash` )

```cpp
struct S {
    std::string first_name;
    std::string last_name;
};

// 自定义哈希能是独立函数对象：
struct MyHash
{
    std::size_t operator()(S const& s) const
    {
        std::size_t h1 = std::hash<std::string>{}(s.first_name);
        std::size_t h2 = std::hash<std::string>{}(s.last_name);
        return h1 ^ (h2 << 1); // 或使用 boost::hash_combine （见讨论）
    }
};
```

自实现 `KeyEqual`  ( `equal_to`  )

```cpp
bool operator==(const S& lhs, const S& rhs) {
    return lhs.first_name == rhs.first_name && lhs.last_name == rhs.last_name;
}
```

### 方式二：标准命名空间中 类模板的 指定特化版本

自定义类特化 `std::hash` 模板。

```cpp
namespace std {
template <>
class hash<Employee> {
 public:
  size_t operator()(const Employee &employee) const
  {
    // 用 Fowler-Noll-Vo hash 哈希函数的变体计算 employee 的哈希
    size_t result = 2166136261;

    for (size_t i = 0, ie = employee.name.size(); i != ie; ++i) {
      result = (result * 16777619) ^ employee.name[i];
    }

    return result ^ (employee.ID << 1);
  }
};
}// end of namespaace std
```

#### `unorderred_multiset` Key值不唯一

```cpp
#include <iostream>
#include <unordered_set>

using std::cout;
using std::endl;
using std::unordered_multiset;

template <typename Container>
void display(const Container &con) {
    for (auto &elem : con) {
        cout << elem << "  ";
    }
    cout << endl;
}

void test() {
    // unordered_multiset的特征
    // 1、key值是不唯一，可以重复
    // 2、key值是没有顺序的
    // 3、底层使用的是哈希
    unordered_multiset<int> number = {1, 3, 5, 7, 9, 6, 4, 2, 3, 1, 3};
    display(number);

    /* auto it = number.begin(); */
    /* *it = 100; */
}

class Point {
public:
    Point(int ix = 0, int iy = 0)
        : _ix(ix), _iy(iy) {
        /* cout << "Point(int = 0, int = 0)" << endl; */
    }

    int getX() const {
        return _ix;
    }

    int getY() const {
        return _iy;
    }

    /* double getDistance() const */
    /* { */
    /*     return hypot(_ix, _iy); */
    /* } */

    ~Point() {
        /* cout << "~Point()" << endl; */
    }

    friend std::ostream &operator<<(std::ostream &os, const Point &rhs);

private:
    int _ix;
    int _iy;
};

std::ostream &operator<<(std::ostream &os, const Point &rhs) {
    os << "(" << rhs._ix
       << ", " << rhs._iy
       << ")";

    return os;
}

//函数对象
struct HashPoint {
    size_t operator()(const Point &rhs) const {
        cout << "size_t operator()(const Point &) const" << endl;
        //哈希函数的设计
        return (rhs.getX() << 1) ^ (rhs.getY() << 2);
    }
};

//标准命名空间std中的类模板hash的全特化版本
namespace std {

//模板的特化（全特化）
template <>
struct hash<Point> {
    size_t operator()(const Point &rhs) const {
        cout << "size_t std::hash::operator()(const Point &) const " << endl;
        return (rhs.getX() << 1) ^ (rhs.getY() << 2);
    }
};

}  // end of namespace std

#if 1
// std::equal_to
bool operator==(const Point &lhs, const Point &rhs) {
    cout << "bool operator==(const Point &, const Point &)" << endl;
    return ((lhs.getX() == rhs.getX()) && (lhs.getY() == rhs.getY()));
}
#endif

namespace std {

// equal_to的特化
template <>
struct equal_to<Point> {
    bool operator()(const Point &lhs, const Point &rhs) const {
        cout << "bool std::equal_to " << endl;
        return ((lhs.getX() == rhs.getX()) && (lhs.getY() == rhs.getY()));
    }
};

};  // namespace std

void test2() {
    unordered_multiset<Point, HashPoint> number = {
        /* unordered_multiset<Point> number = { */
        Point(1, 2),
        Point(1, 2),
        Point(1, -2),
        Point(1, -2),
        Point(3, 2),
        Point(-1, 4),
        Point(-10, -2),
        Point(-1, 4),
    };
    display(number);

    cout << endl
         << "unordered_multiset的下标访问" << endl;
    /* cout << "number[] = " << number[Point(1, 2)] << endl; */
}
int main(int argc, char **argv) {
    test2();
    return 0;
}
```

string 类中重载了 `hash` ( 先检查`std::hash`  ，再查看对应类型如`string` 下有无写好)

#### `unordered_multimap`

```cpp
#include <math.h>

#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>

using std::cout;
using std::endl;
using std::make_pair;
using std::pair;
using std::string;
using std::unordered_multimap;

template <typename Container>
void display(const Container &con) {
    for (auto &elem : con) {
        cout << elem.first << "  " << elem.second << endl;
    }
}

void test() {
    // unordered_multimap的特征
    // 1、存放的元素是一个pair类型，key与value值，key是不唯一的，可以重复
    ///但是value值重复与否是没有关系的
    // 2、key值是没有顺序的
    // 3、底层实现是哈希
    unordered_multimap<int, string> number = {
        /* unordered_multimap<int, string, std::greater<int>> number = { */
        {3, "武汉"},
        {5, "上海"},
        {3, "武汉"},
        pair<int, string>(4, "北京"),
        pair<int, string>(5, "天津"),
        pair<int, string>(4, "北京"),
        make_pair(2, "南京"),
        make_pair(6, "南京")};
    display(number);
#if 0
    cout << endl << "unordered_multimap的下标访问" << endl;
    cout << "number[2] = " << number[2] << endl;
    cout << "number[1] = " << number[1] << endl;
    display(number);
    cout << endl << endl;
    number[1] = "东京";
    number[6] = "东京";
    display(number);
#endif
}

class Point {
public:
    Point(int ix = 0, int iy = 0)
        : _ix(ix), _iy(iy) {
        /* cout << "Point(int = 0, int = 0)" << endl; */
    }

    double getDistance() const {
        return hypot(_ix, _iy);
    }

    ~Point() {
        /* cout << "~Point()" << endl; */
    }

    friend std::ostream &operator<<(std::ostream &os, const Point &rhs);

private:
    int _ix;
    int _iy;
};

std::ostream &operator<<(std::ostream &os, const Point &rhs) {
    os << "(" << rhs._ix
       << ", " << rhs._iy
       << ")";

    return os;
}

void test2() {
    unordered_multimap<string, Point> number = {
        {"wuhan", Point(1, 2)},
        {"hubei", Point(1, -2)},
        pair<string, Point>("nanjing", Point(1, 2)),
        pair<string, Point>("wuhan", Point(10, 2)),
        make_pair("dongjing", Point(3, 4)),
        make_pair("tianjin", Point(2, 3)),
    };
    display(number);

    cout << endl
         << "unordered_multimap的查找操作" << endl;
    size_t cnt1 = number.count("wuhan");
    size_t cnt2 = number.count("wuhan2");
    cout << "cnt1 = " << cnt1 << endl;
    cout << "cnt2 = " << cnt2 << endl;

    auto it = number.find("tianjin");
    if (it != number.end()) {
        cout << "查找成功 " << it->first
             << "  " << it->second << endl;
    } else {
        cout << "查找失败，该元素存在unordered_multimap中" << endl;
    }

    cout << endl
         << "unordered_multimap的插入操作" << endl;
#if 1
    number.insert(pair<string, Point>("hubei2", Point(2, 3)));
    /* number.insert(make_pair("hubei2", Point(2, 3))); */
    /* number.insert({"hubei2", Point(2, 3)}); */
    display(number);

    cout << endl
         << "unordered_multimap是不支持下标访问" << endl;
    /* cout << "number[\"dongjing\"] = " << number["dongjing"] << endl; */
    /* cout << "number[\"1\"] = " << number["1"] << endl; */

    /* number["1"] = Point(2, 4); */
    /* display(number); */
#endif
}

int main(int argc, char **argv) {
    test2();
    return 0;
}
```

## 总结 ： 注意 比较：

比较：需要的是比较函数（ `bool cmp(lhs, rhs) { return lhs < rhs; }` 重要的是 `**<**` )

1. std::less  ( 里面写好了内置类型的 `<` )
1. operator <

-
```cpp
// 自己实现的 Compare , 并显式调用
struct Compare {
    bool operator(){
        return lhs < rhs; // 只此一句话，< 对自定义类型无效，则需重载 operator< 。否则这里可以实现完整的 < , 则不需要再重载 operator<
    }
}

// 重载 <
bool operator<(const Point& lhs, const Point &rhs){
    // ...
}
```

```cpp
template<
    class Key,
    class Compare = std::less<Key>,
    class Allocator = std::allocator<Key>
> class set;
set<int, std::less<int>, std::allocator<int>> number = {1, 2, 3, 5, 9, 7};

// 默认参数 std::less;

namespace std
{
    //......
    template <typename T>
    struct less {
        bool operator()(const T &lhs, const T &rhs) const {
            return lhs < rhs;
        }
    }
    //......
}

// 1. 内置类型的特化
namespace std
{
    //......
    template <>
    struct less<int> {
        bool operator()(const int &lhs, const int &rhs) const {
            return lhs < rhs;
        }
    }
}

// 2. operator<
set<Point, std::less<Point>, std::allocator<Point>> number = {1, 2, 3, 5,
9, 7};
namespace std
{
    //......
    template <>
    struct less<Point> {
        bool operator()(const Point &lhs, const Point &rhs) const {
             //也可以在这里直接写 < 的逻辑，则不需要再重载 operator<
            return lhs < rhs;
        }
    }
}

//肯定是一个普通函数的形式(作友元访问类)
bool operator<(const Point &lhs, const Point &rhs) {
    //逻辑
}

// 3. struct Compare
set<Point, Comparation, std::allocator<Point>> number = {Point(1, 2),
Point(3, 4)};
template <typename T>
    struct Comparation   {
        bool operator()(const T &lhs, const T &rhs) const {
            //也可以在这里直接写 < 的逻辑，则不需要再重载 operator<
            return lhs < rhs;
        }
    }
#if 0
    bool operator<(const Point &lhs, const Point &rhs) {
        //如果在括号里写好了 < 的逻辑, 则不需要在这里写
    }
#endif
```

## 如何选择合适的容器

#### 1、如果元素是连续存储的？

肯定不是关联式容器，也不是无序关联式容器，肯定就只能在序列式容器中进行选取。list元素之间也不 是连续的，是链表；deque是逻辑上是连续的，但是物理上是不一定连续的；只能是vector。

#### 2、查找数据的时候，时间复杂度？

查找的时间复杂度是O(1)，可以首选底层使用哈希表的容器，就是四个无序关联式容器。需要注意 vector是可以支持下标访问，时间复杂度也能是O(1)。 时间复杂度是O(logN)，树的结构查找数据的时候，满足这个条件。关联式容器底层使用红黑树，所以可 以首选四种关联式容器。

#### 3、可以使用下标？

vector、deque、map、unordered_map

#### 4、下标具有插入操作的

map或者unordered_map

#### 5、容器可以使用迭代器

不能使用容器适配器，不能使用stack、queue、priority_queue

## 优先级队列  ( `heap`  (大根堆) )

##### 类型萃取

```cpp
template<
    class T,
    class Container = std::vector<T>, //必须是一个序列式容器
    class Compare = std::less<typename Container::value_type> //类型萃取
> class priority_queue;
```

`priority_queue` 不支持一个大括号直接初始化

```cpp
#include <math.h>

#include <iostream>
#include <queue>
#include <vector>

using std::cout;
using std::endl;
using std::priority_queue;
using std::vector;

void test() {
    //原理：优先级队列底层使用的是大根堆（大顶堆）。
    //当将元素存到优先级队列后，会按照std::less的标准进行排序，当
    //只有一个元素的时候，优先级最高的就是该元素，该元素会放在堆
    //顶，当有新的元素插入进来之后，此时会与堆顶进行比较，如果堆顶
    //小于插入进来的元素，此时就满足std::less,就会将新的元素与
    //堆顶进行置换，新的元素成为新的堆顶,如果新插入的元素与堆顶
    //进行比较，如果堆顶大于等于新插入的元素，此时不满足std::less
    //老的堆顶依旧是新的堆顶，不会发生置换。

    //可以使用迭代器范围的方式进行初始化
    vector<int> vec = {1, 5, 8, 9, 5, 6, 3};
    /* priority_queue<int> number(vec.begin(), vec.end());//ok */
    /* priority_queue<int> pque;//创建空对象 */
    priority_queue<int, std::vector<int>, std::greater<int>> pque;  //创建空对象
    for (size_t idx = 0; idx != vec.size(); ++idx) {
        pque.push(vec[idx]);
        cout << "优先级最高的元素 " << pque.top() << endl;
    }

    while (!pque.empty()) {
        cout << pque.top() << "  ";
        pque.pop();
    }
    cout << endl;
}

class Point {
public:
    Point(int ix = 0, int iy = 0)
        : _ix(ix), _iy(iy) {
        /* cout << "Point(int = 0, int = 0)" << endl; */
    }

    double getDistance() const {
        return hypot(_ix, _iy);
    }

    ~Point() {
        /* cout << "~Point()" << endl; */
    }

    friend bool operator<(const Point &lhs, const Point &rhs);
    friend bool operator>(const Point &lhs, const Point &rhs);

    friend std::ostream &operator<<(std::ostream &os, const Point &rhs);

    friend struct Comparetion;  //声明为Point的友元

private:
    int _ix;
    int _iy;
};

std::ostream &operator<<(std::ostream &os, const Point &rhs) {
    os << "(" << rhs._ix
       << ", " << rhs._iy
       << ")";

    return os;
}

//点到原点的距离作为大小的比较
bool operator<(const Point &lhs, const Point &rhs) {
    if (lhs.getDistance() < rhs.getDistance()) {
        return true;
    } else if (lhs.getDistance() == rhs.getDistance()) {
        if (lhs._ix < rhs._ix) {
            return true;
        } else if (lhs._ix == rhs._ix) {
            if (lhs._iy < rhs._iy) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
}

bool operator>(const Point &lhs, const Point &rhs) {
    /* cout << "bool operator>(const Point &, const Point &)" << endl; */
    if (lhs.getDistance() > rhs.getDistance()) {
        return true;
    } else if (lhs.getDistance() == rhs.getDistance()) {
        if (lhs._ix > rhs._ix) {
            return true;
        } else if (lhs._ix == rhs._ix) {
            if (lhs._iy > rhs._iy) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
}

struct Comparetion {
    bool operator()(const Point &lhs, const Point &rhs) const {
        /* cout << "bool operator()(const Point &, const Point &) const" << endl; */
        if (lhs.getDistance() < rhs.getDistance()) {
            return true;
        } else if (lhs.getDistance() == rhs.getDistance()) {
            if (lhs._ix < rhs._ix) {
                return true;
            } else if (lhs._ix == rhs._ix) {
                if (lhs._iy < rhs._iy) {
                    return true;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
};
void test2() {
    vector<Point> vec = {
        Point(1, 2),
        Point(3, 4),
        Point(0, 4),
        Point(-3, 4),
        Point(3, 4),
        Point(10, 0),
        Point(1, 2),
    };

    /* priority_queue<Point> pque; */
    /* priority_queue<Point, vector<Point>, std::less<Point>> pque; */
    /* priority_queue<Point, vector<Point>, std::greater<Point>> pque; */
    /* priority_queue<Point, vector<Point>, Comparetion> pque; */
    priority_queue<Point, std::deque<Point>, Comparetion> pque;

    for (size_t idx = 0; idx != vec.size(); ++idx) {
        pque.push(vec[idx]);
        cout << "优先级最高的元素 " << pque.top() << endl;
    }

    while (!pque.empty()) {
        cout << pque.top() << "  ";
        pque.pop();
    }
    cout << endl;
}
int main(int argc, char **argv) {
    test2();
    return 0;
}
```

## 二、流迭代器

list单独的sort

全局的sort，算法库中的sort。

低耦合，将容器与算法之间的关系变得更加微弱。

```cpp
class A {
    private:
    int _ix;
    int _iy;
    int _iz;
};

class B
: public A {

};

class B {
private:
    A *_pa;
}
```

迭代器类似于指针，可以操作容器中的数据，使得算法与容器之间就关联起来。

输入输出流数据都会进缓冲区，缓冲区是可以存数据的，而容器就是用来存数据的，所以输入输出流可 以看成是容器。

#### 输出流迭代器

```cpp
#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>

using std::cout;
using std::endl;
using std::ostream_iterator;
using std::vector;
using std::copy;

//输出流运算符在哪里
void test() {
    vector<int> vec = {1, 4, 7, 9, 3, 2};
    ostream_iterator<int> osi(cout, "\n");
    copy(vec.begin(), vec.end(), osi);

    /* cout << 1 << endl; */
    /* cout << 4 << endl; */
    /* cout << 7 << endl; */
}

int main(int argc, char **argv) {
    test();
    return 0;
}
```

```cpp
ostream_iterator(ostream_type& stream, const CharT* delim)

ostream_iterator(ostream_type& stream)

template< class InputIt, class OutputIt >
OutputIt copy( InputIt first, InputIt last, OutputIt d_first );
```

```cpp
//ostream_iterator<int> osi(cout, "\n");
// __s = cout
//__c = "\n"
//_M_stream = &cout;
//_M_string = "\n";
class ostream_iterator {
public:
    ostream_iterator(ostream_type& __s, const _CharT* __c)
    : _M_stream(&__s), _M_string(__c) {}
        ostream_iterator<_Tp>& operator*() { return *this; }
        ostream_iterator<_Tp>& operator++() { return *this; }
        ostream_iterator<_Tp>& operator++(int) { return *this; }
        ostream_iterator<_Tp>& operator=(const _Tp& __value) {
        *_M_stream << __value;
        if (_M_string) *_M_stream << _M_string;
        return *this;
    }
private:
    ostream_type* _M_stream;
    const _CharT* _M_string;
}
```

```cpp
template <class _InputIter, class _OutputIter>
inline _OutputIter copy(_InputIter __first, _InputIter __last,
                        _OutputIter __result) {
    __STL_REQUIRES(_InputIter, _InputIterator);
    __STL_REQUIRES(_OutputIter, _OutputIterator);
    return __copy_aux(__first, __last, __result, __VALUE_TYPE(__first));
}
template <class _InputIter, class _OutputIter, class _Tp>
inline _OutputIter __copy_aux(_InputIter __first, _InputIter __last,
                              _OutputIter __result, _Tp*) {
    typedef typename __type_traits<_Tp>::has_trivial_assignment_operator
        _Trivial;
    return __copy_aux2(__first, __last, __result, _Trivial());
}
// _Trivial:平凡的。如果对应的是类的话，类没有显示的写构造函数、析构函数、拷贝构造函数、赋值
// 运算符函数等。int/bool/char 内置类型

// noTrival:非平凡的。如果对应的是类的话，类有显示的写构造函数、析构函数、拷贝构造函数、赋值
// 运算符函数等。
template <class _InputIter, class _OutputIter>
inline _OutputIter __copy_aux2(_InputIter __first, _InputIter __last,
                               _OutputIter __result, __false_type) {
    return __copy(__first, __last, __result,
                  __ITERATOR_CATEGORY(__first),
                  __DISTANCE_TYPE(__first));
}
// copy(vec.begin(), vec.end(), osi);
__first = vec.begin();
__last = vec.end();
osi = __result template <class _InputIter, class _OutputIter, class _Distance>
inline _OutputIter __copy(_InputIter __first, _InputIter __last,
                          _OutputIter __result,
                          input_iterator_tag, _Distance*) {
    for (; __first != __last; ++__result, ++__first)
        *__result = *__first;
    return __result;
}
__last 1, 4, 7, 9, 3, 2 f
                          //对象 = int
                          osi = 4;
ostream_iterator& operator=(const int& __value) {
    cout << 4;
    if (_M_string) *_M_stream << _M_string;  // cout << "\n"
    return *this;
}
// ostream_iterator<int> osi(cout, "\n");
//  __s = cout
//__c = "\n"
//_M_stream = &cout;
//_M_string = "\n";
```

#### 输入流迭代器

```cpp
#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>

using std::cout;
using std::endl;
using std::istream_iterator;
using std::ostream_iterator;
using std::vector;
using std::copy;

void test() {
    vector<int> number;
    //创建的输入流迭代器isi，使用std::cin进行输入
    istream_iterator<int> isi(std::cin);

    //将数据输入到vector中
    //vector插入元素的时候，需要使用push_back
    /* copy(isi, istream_iterator<int>(), number.begin()); */
    copy(isi, istream_iterator<int>(),
         std::back_insert_iterator<vector<int>>(number));

    //将vector中的数据做了输出
    copy(number.begin(), number.end(),
         ostream_iterator<int>(cout, " "));
    cout << endl;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
```

```cpp
//_M_stream = &cin;
class istream_iterator {
public:
    istream_iterator(istream_type& __s)
        : _M_stream(&__s) {
        _M_read();
    }
    reference operator*() const { return _M_value; }
    istream_iterator& operator++() {
        _M_read();
        return *this;
    }

private:
    istream_type* _M_stream;  //可以与cin之间产生联系
    _Tp _M_value;             //记录cin输入的值
    bool _M_ok;               //可以记录流的状态
    //真正进行数据输入的函数
    void _M_read() {
        _M_ok = (_M_stream && *_M_stream) ? true : false;
        if (_M_ok) {
            *_M_stream >> _M_value;  // cin >> _M_value = 4
            _M_ok = *_M_stream ? true : false;
        }
    }
};
template <class _Container>
class back_insert_iterator {
protected:
    _Container* container;
    explicit back_insert_iterator(_Container& __x)
        : container(&__x) {}
    back_insert_iterator<_Container>&
    operator=(const typename _Container::value_type& __value) {
        container->push_back(__value);
        return *this;
    }
    back_insert_iterator<_Container>& operator*() { return *this; }
    back_insert_iterator<_Container>& operator++() { return *this; }
    back_insert_iterator<_Container>& operator++(int) { return *this; }
};

//__first = isi
//__last = istream_iterator<int>()
//__result = std::back_insert_iterator<vector<int>>(number)
copy(isi, istream_iterator<int>(), std::back_insert_iterator<vector<int>>(number));
_OutputIter __copy(_InputIter __first, _InputIter __last,
                   _OutputIter __result,
                   input_iterator_tag, _Distance*) {
    for (; __first != __last; ++__result, ++__first)  //_M_read() cin >>
        _M_value* __result = *__first;
    return __result;
}

// __result = 4
back_insert_iterator & operator=(const int& __value) {
    container->push_back(__value);
    return *this;
}
```

#### 插入迭代器

三个迭代器适配器的类模板与函数模板

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <iterator>
#include <algorithm>

using std::cout;
using std::endl;
using std::vector;
using std::list;
using std::set;
using std::ostream_iterator;
using std::copy;
using std::back_insert_iterator;
using std::back_inserter;
using std::front_insert_iterator;
using std::front_inserter;
using std::insert_iterator;
using std::inserter;

void test() {
    vector<int> vecNumber = {1, 9, 7, 5};
    list<int> lstNumber = {2, 6, 8, 10};

    //底层会调用push_back将数据插入到vector中
    /* copy(lstNumber.begin(), lstNumber.end(), back_inserter(vecNumber)); */
    copy(lstNumber.begin(), lstNumber.end(), back_insert_iterator<vector<int>>(vecNumber));
    //将vector中的数据进行遍历,做了打印操作
    copy(vecNumber.begin(), vecNumber.end(), ostream_iterator<int>(cout, " "));
    cout << endl << endl;

    //将vector中的数据插入到list的头部
    //底层会调用push_front
    /* copy(vecNumber.begin(), vecNumber.end(), front_inserter(lstNumber)); */
    copy(vecNumber.begin(), vecNumber.end(), front_insert_iterator<list<int>>(lstNumber));
    copy(lstNumber.begin(), lstNumber.end(), ostream_iterator<int>(cout, "  "));
    cout << endl << endl;

    set<int> setNumber = {1, 6, 12, 90, 23};
    auto it = setNumber.begin();
    //底层会调用set的insert方法在中间进行插入
    // insert 需要 迭代器位置it
    /* copy(vecNumber.begin(), vecNumber.end(), insert_iterator<set<int>>(setNumber, it)); */
    copy(vecNumber.begin(), vecNumber.end(), inserter(setNumber, it));
    copy(setNumber.begin(), setNumber.end(), ostream_iterator<int>(cout, "  "));
    cout << endl << endl;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
```

#### 反向迭代器

```cpp
#include <iostream>
#include <iterator>
#include <vector>

using std::cout;
using std::endl;
using std::reverse_iterator;
using std::vector;

void test() {
    vector<int> number = {1, 4, 7, 9, 12, 34, 78, 14};
    vector<int>::iterator it;
    for(it = number.begin(); it != number.end(); ++it) {
        cout << *it << "  ";
    }
    cout << endl << endl;

    vector<int>::reverse_iterator rit;
    for(rit = number.rbegin(); rit != number.rend(); ++rit) {
        cout << *rit << "  ";
    }
    cout << endl << endl;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
```

## 函数对象

可以与小括号进行结合，表示函数的含义

1、重载了函数调用运算符的类对象的对象

2、函数名字

3、函数指针

## 算法

类型

1、非修改式的算法 count、find、find_xxx、for_each

2、修改式的算法 copy、remove、remove_if、unique、fill

3、排序算法 sort以及sort相关、lower_bound、upper_bound、binary_search

4、集合操作 set_intersection

5、heap的操作 make_heap、push_heap、pop_heap

6、最大值与最小值 min、max

7、比较函数 equal

8、当空间的申请与对象的构建分开的时候，可以uninitialized_copy未初始化拷贝操作， uninitialized_xxx

函数类型

一元函数（UnaryFunction）：函数的参数只有一个。

一元断言/一元谓词（UnaryPredicate）：函数的参数只有一个，并且函数的返回类型是bool。

二元函数：函数的参数有两个。

n元函数：函数的参数有n个。

#### `for_each`

```cpp
void print(int value) {
    cout << value << " ";
}

vector<int> number = {1, 6, 8, 4, 2, 7, 9};
for_each(number.begin(), number.end(), print);

template <class _InputIter, class _Function>
_Function for_each(_InputIter __first, _InputIter __last, _Function __f) {
    for ( ; __first != __last; ++__first)
    	__f(*__first);//print(*__first)
    return __f;
}
// 				     __last
// 1, 6, 8, 4, 2, 7, 9
// __f
```

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>

using std::cout;
using std::endl;
using std::for_each;
using std::vector;
using std::ostream_iterator;
using std::copy;

void print(int &value) {
    ++value;
    cout << value << "  ";
}

void test() {
    //想去将vector进行遍历
    vector<int> number = {1, 6, 8, 4, 2, 7, 9};
    /* copy(number.begin(), number.end(), ostream_iterator<int>(cout, "  ")); */
    /* cout << endl; */

    for_each(number.begin(), number.end(), print);
    cout << endl;

    //lambda表达式 ==  匿名函数
    for_each(number.begin(), number.end(), [](int &value) {
             ++value;
             cout << value << " ";
             });
    cout << endl;
    copy(number.begin(), number.end(), ostream_iterator<int>(cout, "  "));
    cout << endl;

}

int main(int argc, char **argv) {
    test();
    return 0;
}
```

#### `remove_if`

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>

using std::cout;
using std::endl;
using std::copy;
using std::remove_if;
using std::vector;
using std::ostream_iterator;

bool func(int value) {
    return value > 4;
}
void test() {
    vector<int> number = {1, 4, 7, 9, 5, 6, 4, 3, 2, 7};
    copy(number.begin(), number.end(), ostream_iterator<int>(cout, "  "));
    cout << endl;

    auto it = remove_if(number.begin(), number.end(),
                        bind2nd(std::greater<int>(), 4));

    /* auto it = remove_if(number.begin(), number.end(), */
    /*                     bind1st(std::less<int>(), 4)); */

    //[]捕获列表,lambda表达式
    /* auto it = remove_if(number.begin(), number.end(), [](int value){ */
    /*                     return value > 4; */
    /*                     }); */

    //remove_if不会将满足条件的数据删除，但是会返回待删除元素的
    //首地址（首迭代器），然后在配合erase使用
    /* auto it = remove_if(number.begin(), number.end(), func); */
    number.erase(it, number.end());
    copy(number.begin(), number.end(), ostream_iterator<int>(cout, "  "));
    cout << endl;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
```

remove_if不会将满足条件的数据删除，但是会返回待删除元素的首地址（首迭代器），然后在配合erase使用

#### `remove_if`源码

```cpp
bool func(int value) {
    return value > 4;
}

remove_if(number.begin(), number.end(), func);
first = number.begin();
last = number.end();
p = func;

template<class InputIt, class UnaryPredicate>
InputIt find_if(InputIt first, InputIt last, UnaryPredicate p) {
    for (; first != last; ++first) {
        if (p(*first)) {
        	return first;
    	}
    }
    return last;
}

1 4 7 9 5 6 4 3 2 7
f

bool func(int value) {
    return value > 4;
}
template<class ForwardIt, class UnaryPredicate>
ForwardIt remove_if(ForwardIt first, ForwardIt last, UnaryPredicate p) {
	first = std::find_if(first, last, p);
    if (first != last) {
        for(ForwardIt i = first; ++i != last; ) {
            if (!p(*i))  {
                //*first++ = std::move(*i);
                *first = *i;
                first++;
            }
        }
    }
    return first;
}
		 f        last
1 4 4 3 2 6 4 3 2 7
				  i

		1, 4, 7, 9, 5, 6, 4, 3, 2, 7
vector   1 4 9, 6, 4, 3, 2
list     1 4 4 3 2
```

STL算法库中的算法属于通用算法，不是针对于某一种具体容器去设计，所有的容器都可以直接使用，这就是通用编程或者泛型编程的思想。

#### 解决迭代器失效的通用方法：迭代器重新置位。

```cpp
vector<int> number;
number.push_back(1);

bool flag = true;
for (auto it = number.begin(); it != number.end(); ++it) {
    cout << *it << "  ";
    if (flag) {
        number.push_back(2);  //底层已经发生了扩容，迭代器失效了
        it = number.begin();  //每次在使用迭代器之前，将迭代器
                              //重新置位
        flag = false;
    }
}
cout << endl;
```

```cpp
remove_if(number.begin(), number.end(), 一元断言/谓词);
bool func(int value) {
    return value > 4;
}

remove_if(number.begin(), number.end(), 二元断言/谓词);
bool func(int num1, int num2){
    return value > 4;
}

remove_if(number.begin(), number.end(), 一元断言/谓词);
bool func2(int num1, int num2 = 4){
    return num1 > num2;
}

func2(10);

struct greater{
    bool operator()(const int &num1, const int &num2 = 4){
        return num1 > 4;
    }
}
```

```cpp
//可以绑定二元函数f的第一个参数，使得二元函数变成一元函数，并固定第一个参数
template< class F, class T >
std::binder1st<F> bind1st( const F& f, const T& x );

bind1st(f, 4);
f(4, y)

remove_if(number.begin(), number.end(), 一元断言/谓词);
bool func(int value){
    return value > 4;
}

remove_if(number.begin(), number.end(), bind1st(std::less<int>(), 4))
struct less{
    bool operator()(const int &num1 = 4, const int &num2)  {
        return 4 < num2;
    }
}

////可以绑定二元函数f的第二个参数，使得二元函数变成一元函数，并固定第二个参数
//template< class F, class T >
//std::binder2nd<F> bind2nd( const F& f, const T& x )
```

#### `bind` 可以改变函数的形态 （ 改变函数类型： 返回类型 、参数列表 ）

```cpp
Defined in header <functional>
template< class F, class... Args >
/*unspecified*/ bind( F&& f, Args&&... args );

template< class R, class F, class... Args >
/*unspecified*/ bind( F&& f, Args&&... args );
```

bind可以绑定到n元函数，该函数可以是自由函数、全局函数（非成员函数），也可以绑定到成员函数，甚至可以绑定的数据成员上。

```cpp
#include <functional>
#include <iostream>

using std::bind;
using std::cout;
using std::endl;
using std::function;

int a = 10;
int add(int x, int y, int z) {
    cout << "int add(int, int, int)" << endl;
    return x + y + z;
}

class Example {
public:
    int add(int x, int y) {
        cout << "int Example::add(int, int)" << endl;
        return x + y;
    }

    int data = 200;  // C++11中可以允许的
};

void test00() {
    // bind是可以改变函数的形态的（改变函数的类型）,函数的类型包括
    //函数的返回类型，以及函数的参数列表（参数的个数，参数的顺序
    //，参数类型）
    // function可以去接收函数的类型，function是函数的容器
    // std::bind + std::function，可以实现多态
    //

    // add函数类型int (int, int, int )
    // f的函数类型int ()
    // function可以用来存函数类型，所以function是函数的容器
    function<int()> f = bind(&add, 1, 2, 3);
    cout << "f() = " << f() << endl;

    // add函数类型  int (this, int, int)
    // int ()
    Example ex;
    function<int()> f2 = bind(&Example::add, &ex, 20, 30);
    cout << "f2() = " << f2() << endl;

    // add int(int, int, int)
    // f3 int(int, int)
    // 占位符
    // int(int, int)
    function<int(int, int)> f3 = bind(&add, 100, std::placeholders::_1,
                                      std::placeholders::_2);
    cout << "f3(20, 30) = " << f3(20, 30) << endl;

    // int(int)
    function<int(int)> f4 = bind(&add, 20, std::placeholders::_1, 30);
    cout << "f4(300) = " << f4(300) << endl;

    cout << endl
         << "bind绑定到数据成员上面" << endl;
    f = bind(&Example::data, &ex);
    cout << "f() = " << f() << endl;
}
void test() {
    // add函数类型int (int, int, int )
    // f的函数类型int ()
    auto f = bind(&add, 1, 2, 3);
    cout << "f() = " << f() << endl;

    // add函数类型  int (this, int, int)
    // int ()
    Example ex;
    auto f2 = bind(&Example::add, &ex, 20, 30);
    cout << "f2() = " << f2() << endl;

    // add int(int, int, int)
    // f3 int(int, int)
    //占位符
    // int(int, int)
    auto f3 = bind(&add, 100, std::placeholders::_1,
                   std::placeholders::_2);
    cout << "f3(20, 30) = " << f3(20, 30) << endl;

    // int(int)
    auto f4 = bind(&add, 20, std::placeholders::_1, 30);
    cout << "f4(300) = " << f4(300) << endl;
}

int func1(int x) {
    cout << "int func1(int)" << endl;
    return x;
}

int func2(int y) {
    cout << "int func2(int)" << endl;
    return y;
}

void test2() {
    add(1, 2, 3);
    // pFunc是一个函数指针  指针函数int*  pf(int)
    //回调函数可以延迟函数的调用
    typedef int (*pFunc)(int);  // pFunc是一个函数类型，int(int)
    pFunc f = &func1;           //注册回调函数
    //....
    //...
    //...
    cout << "f(10) = " << f(10) << endl;  //回调函数的调用

    f = &func2;
    cout << "f(200) = " << f(200) << endl;

    /* f = &add;//pFunc类型被固定了,error */
    /* double da = 10; */
    /* int *pInt = &da; */
}

void func3(int x1, int x2, int x3, const int &x4, int &x5) {
    cout << "x1 = " << x1 << endl
         << "x2 = " << x2 << endl
         << "x3 = " << x3 << endl
         << "x4 = " << x4 << endl
         << "x5 = " << x5 << endl;
}

void test3() {
    //占位符本身代表的是形参的位置
    //占位符中的数字代表的是实参的位置
    //使用的是值传递
    // cref,引用的包装器 const reference
    // ref, 引用的包装器,reference
    int number = 100;
    auto f = bind(&func3, 1, std::placeholders::_1,
                  std::placeholders::_6,
                  std::cref(number), std::ref(number));
    number = 700;
    f(20, 40, 300, 200, 600, 800);
}
int main(int argc, char **argv) {
    test00();
    return 0;
}
```

#### 占位符 `std::placeholders::_29`

```cpp
// bind.cc test3()

void test3()
	//占位符本身代表的是形参的位置
    //占位符中的数字代表的是实参的位置
    //使用的是值传递
    //cref,引用的包装器 const reference
    //ref, 引用的包装器,reference
    int number = 100;
    auto f = bind(&func3, 1, std::placeholders::_1,
                  std::placeholders::_6,
                  std::cref(number), std::ref(number));
    number = 700;
    f(20, 40, 300, 200, 600, 800);
}

void test4(){
    //bind是可以改变函数的形态的（改变函数的类型）,函数的类型包括
    //函数的返回类型，以及函数的参数列表（参数的个数，参数的顺序
    //，参数类型）
    //function可以去接收函数的类型，function是函数的容器
    //std::bind + std::function，可以实现多态
    //

    //add函数类型int (int, int, int )
    //f的函数类型int ()
    //function可以用来存函数类型，所以function是函数的容器
    function<int()> f = bind(&add, 1, 2, 3);
    cout << "f() = " << f() << endl;

    //add函数类型  int (this, int, int)
    //int ()
    Example ex;
    function<int()> f2 = bind(&Example::add, &ex, 20, 30);
    cout << "f2() = " << f2() << endl;

    //add int(int, int, int)
    //f3 int(int, int)
    //占位符
    //int(int, int)
    function<int(int, int)> f3 = bind(&add, 100, std::placeholders::_1,
                   std::placeholders::_2);
    cout << "f3(20, 30) = " << f3(20, 30) << endl;

    //int(int)
    function<int(int)> f4 = bind(&add, 20, std::placeholders::_1, 30);
    cout << "f4(300) = " << f4(300) << endl;

    cout << endl << "bind绑定到数据成员上面" << endl;
    f = bind(&Example::data, &ex); // data 是Example类public数据成员
    cout << "f() = " << f() << endl;
}
```

占位符代表的是形参的位置，占位符中的数字代表的是实参的位置。

使用的是值传递， `cref(const reference )` , 常引用的包装器

`ref( reference )` , 引用的包装器

#### `std::function` 可以用来存函数类型（ 函数容器 ）

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using std::cout;
using std::endl;
using std::vector;
using std::for_each;

class Number{
public:
    Number(size_t data = 0)
    : _data(data)    {

    }

    void print() const    {
        cout << _data << "  ";
    }

    //判断是不是偶数
    bool isEven() const    {
        return (0 == _data%2);
    }

    bool isPrimer() const    {
        if(1 == _data)        {
            return false;
        }

        for(size_t idx = 2; idx != _data/2; ++idx)        {
            if(0 == _data%2)
            {
                return false;
            }
        }

        return true;
    }
private:
    size_t _data;
};
void test(){
    vector<Number> vec;
    for(size_t idx = 0; idx != 30; ++idx)    {
        vec.push_back(Number(idx));
    }

    //成员函数是一个受限制的函数
    for_each(vec.begin(), vec.end(), std::mem_fn(&Number::print));
    cout << endl;
}

int main(int argc, char **argv){
    test();
    return 0;
}
```

function可以去接收函数的类型，function是函数的容器。

#### 思路打开

```cpp
class {

    // C++11 允许
    int data = 100; // int data() { 100; }
}
```

`bind` 可以绑定到n元函数，也可以绑定到**数据成员**。

bind是可以改变函数的形态的（改变函数的类型）,函数的类型包括
函数的返回类型，以及函数的参数列表（参数的个数，参数的顺序，参数类型）

#### `std::bind` + `std::function` 结合使用 ， 可以实现多态( 基于对象的方法（没有继承)

```cpp
#include <math.h>
#include <iostream>
#include <functional>

using std::cout;
using std::endl;
using std::function;
using std::bind;

//抽象类作为接口使用的例子可以实现多态
//
//面向对象的设计原则：开闭原则对扩展开放，对修改关闭
//
//使用std::bind + std::function实现多态,基于对象的方法(没有使用继承)
//
class Figure{
public:
    //重定义
    using DisplayCallback = function<void()>;
    using AreaCallback = function<double()>;

    DisplayCallback _displayCallback;
    AreaCallback _areaCallback;

    /* virtual void display() = 0; */
    /* virtual double area() = 0; */

    //注册回调函数
    /* void setDisplayCallback(function<void()> &&cb) */
    void setDisplayCallback(DisplayCallback &&cb)    {
        _displayCallback = std::move(cb);
    }

    void setAreaCallback(AreaCallback &&cb)    {
        _areaCallback = std::move(cb);
    }

    //执行回调函数
    void handleDisplayCallback() const    {
        if(_displayCallback)        {
            _displayCallback();
        }
    }

    double handleAreaCallback() const    {
        if(_areaCallback)  {
           return  _areaCallback();
        }
        else  {
            return 0;
        }
    }
};

class Rectangle {
public:
    Rectangle(double length = 0, double width = 0)
    : _length(length)
    , _width(width)    {

    }

    void display() {
        cout << "Rectangle";
    }

    double area() {
        return _length * _width;
    }
private:
    double _length;
    double _width;
};

class Circle {
public:
    Circle(double radius = 0)
    : _radius(radius) {

    }

    void show() {
        cout << "Circle";
    }

    double showArea()     {
        return 3.14 * _radius *_radius;;
    }
private:
    double _radius;
};

class Triangle{
public:
    Triangle(double a = 0, double b = 0, double c = 0)
    : _a(a)
    , _b(b)
    , _c(c) {

    }

    void print(int x)  {
        cout << "Triangle";
    }

    double printArea() {
        double tmp = (_a + _b + _c)/2;

        return sqrt(tmp * (tmp - _a) * (tmp - _b) * (tmp - _c));
    }
private:
    double _a;
    double _b;
    double _c;
};

void func(const Figure &pfig){
    //执行回调函数
    pfig.handleDisplayCallback();
    cout << "的面积 : " << pfig.handleAreaCallback() << endl;
}

int main(int argc, char **argv) {
    Rectangle rectangle(10, 20);
    Circle circle(10);
    Triangle triangle(3, 4, 5);

    Figure fig;
    //回调函数的注册
    fig.setDisplayCallback(bind(&Rectangle::display, &rectangle));
    fig.setAreaCallback(bind(&Rectangle::area, &rectangle));
    func(fig);

    fig.setDisplayCallback(bind(&Circle::show, &circle));
    fig.setAreaCallback(bind(&Circle::showArea, &circle));
    func(fig);

    fig.setDisplayCallback(bind(&Triangle::print, &triangle, 3));
    fig.setAreaCallback(bind(&Triangle::printArea, &triangle));
    func(fig);

    return 0;
}
```

#### 成员函数绑定器 `std::men_fn()`

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using std::cout;
using std::endl;
using std::vector;
using std::for_each;

class Number{
public:
    Number(size_t data = 0)
    : _data(data) {

    }

    void print() const {
        cout << _data << "  ";
    }

    //判断是不是偶数
    bool isEven() const {
        return (0 == _data%2);
    }

    bool isPrimer() const {
        if(1 == _data) {
            return false;
        }

        for(size_t idx = 2; idx != _data/2; ++idx) {
            if(0 == _data%2) {
                return false;
            }
        }

        return true;
    }
private:
    size_t _data;
};
void test(){
    vector<Number> vec;
    for(size_t idx = 0; idx != 30; ++idx) {
        vec.push_back(Number(idx));
    }

    //成员函数是一个受限制的函数
    for_each(vec.begin(), vec.end(), std::mem_fn(&Number::print));
    cout << endl;
}

int main(int argc, char **argv){
    test();
    return 0;
}
```

#### 函数指针 与 成员函数指针

```cpp
int (*pFunc)(int, int);

//普通函数
int add(int x, int y) {}

class Test{
    public:
    int add(int x, int y) {

    }
}


// 非静态的成员函数，都会在第一个参数的位置隐藏一个this
// 成员函数指针
int (Test::*pFunc)(int, int);//解决this指针的问题
pFunc = &Test::add;

template< class M, class T >
/*unspecified*/ mem_fn(M T::* pm);

// 成员函数是一个受限制的函数
```

#### 函数名 与 函数入口地址

在C语言中，函数名字是函数的入口地址，C语言是不支持函数重载的 add; //在C++中因为存在函数重载，要找到函数，可以使用函数进行取地址&add;

C是兼容C语言,所以普通 函数的函数名就是函数的入口地址，但是C中成员函数的函数名字就不是函数的入口地址。

_men_fn  65 Number num(1) 去掉还可以绑定吗？   可以_

## 空间适配器

#### 先自己实现了`Vector`

```cpp
#include <iostream>
#include <string>
#include <vector>

using std::allocator;
using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

template <typename T>
class Vector {
public:
    Vector() /* : _start(NULL), _finish(NULL), _end_of_storage(NULL) */
        : _start(nullptr), _finish(nullptr), _end_of_storage(nullptr) {
        cout << "Vector()" << endl;
    }
    ~Vector() {
        cout << "~Vector()" << endl;
        if (_start) {
            while (_start != _finish) {
                _alloc.destroy(--_finish);  // destructor
                // _alloc.destroy(_start++);  // destructor
            }
            _alloc.deallocate(_start, capacity());  // 解分配存储
        }
    }

    void push_back(const T &value) {
        if (size() == capacity()) {
            reallocate();  // 调用下面的函数 重新分配内存
        }
        _alloc.construct(_finish++, value);  // 在分配的内存空间上构造对象
    }
    void pop_back() {
        if (size() > 0) {
            _alloc.destroy(--_finish);  // destructor
        }
    }
    int size() const {
        return _finish - _start;
    }
    int capacity() const {
        return _end_of_storage - _start;
    }

    T &operator[](int idx) {
        // if (idx < 0 || idx > size()) {
        //     return T(NULL);
        // }
        return *(_start + idx);
    }

    void printSize() {
        cout << "the size :" << size() << "\t"
             << "the capacity :" << capacity() << endl;
    }

    // iterator
    typedef T* iterator;
    iterator begin(){
        return _start;
    }
    iterator end(){
        return _finish;
    }
    // for(auto &elem : number) {
    //     cout << elem << "  ";
    // }
    // cout << endl;
}
private:
    void reallocate() {  //重新分配内存空间,动态扩容要用
        int oldCap = capacity();
        int newCap = (oldCap == 0) ? 1 : 2 * oldCap;

        T *newMem = _alloc.allocate(newCap);  // 申请未初始化的内存空间
        if (_start) {

            //copy 到 新空间
            std::uninitialized_copy(_start, _finish, newMem);

            // destructor 老空间的对象
            while ( _finish != _start ) {
                // 注意考虑 _start == _finish 的边界条件
                _alloc.destroy(--_finish);  // destructor
                // _alloc.destroy(_start++);  // destructor
            }

            // 回收 旧内存空间
            _alloc.deallocate(_start, oldCap);
        }

        // 指向新空间
        _start = newMem;
        _finish = _start + oldCap;
        _end_of_storage = _start + newCap;
    }

private:
    static std::allocator<T> _alloc;

    T *_start;           //指向数组中的第一个元素
    T *_finish;          //指向最后一个实际元素之后的那个元素
    T *_end_of_storage;  //指向数组本身之后的位置
};

// 静态 类外初始化
template <typename T>
std::allocator<T> Vector<T>::_alloc;

void print(Vector<int> &v) {
    for (int i = 0; i != v.size(); ++i) {
        cout << v[i] << " ";
    }
    cout << endl;
}

template <typename Container>
void printCapacity(const Container &con) {
    cout << "con.size() = " << con.size() << endl;
    cout << "con.capacity() = " << con.capacity() << endl;
}

int main(int argc, char **argv) {
    Vector<int> vec;
    vec.printSize();

    vec.push_back(1);
    vec.printSize();
    print(vec);

    vec.push_back(2);
    vec.printSize();
    print(vec);
    vec.push_back(3);
    vec.printSize();
    print(vec);
    vec.push_back(4);
    vec.printSize();
    print(vec);
    vec.push_back(5);
    vec.printSize();
    print(vec);
    vec.push_back(6);
    vec.printSize();
    print(vec);
    vec.push_back(7);
    vec.printSize();
    print(vec);

    return 0;
}
/*
Vector()
the size :0     the capacity :0
the size :1     the capacity :1
1
the size :2     the capacity :2
1 2
the size :3     the capacity :4
1 2 3
the size :4     the capacity :4
1 2 3 4
the size :5     the capacity :8
1 2 3 4 5
the size :6     the capacity :8
1 2 3 4 5 6
the size :7     the capacity :8
1 2 3 4 5 6 7
~Vector()
*/
```

#### `allocator` 重要接口

```cpp
// 配置空间，足以存储n个T对象
pointer allocator::allocate(size_type n, const void* = 0)
// 释放空间
void allocator::deallocate(pointer p, size_type n)
// 调用对象的构造函数，等同于 new((void*)p) T(x)
// new((void*)p) T(x) 为placement new，即在指定内存空间下构造函数
void allocator::construct(pointer p, const T& x)
// 调用对象的析构函数，等同于 p->~T()
void allocator::destroy(pointer p)
```

1、为什么需要将空间的申请和对象的构建分开？

new :  申请未初始化的内存空间 、 在内存上构建对象、 返回指向对象的指针。

STL中存放的是大量的元素，如果每次都创建一个对象，这样的话，效率很低，所以就可以一次申请大片空间，然后在申请的空间上构建对象。

```cpp
template <class _Tp>
class allocator
{

public:
    //空间的申请函数，该函数会走两个分支，对应一级空间配置器与二级空间配置器（默认的）
    _Tp* allocate(size_type __n, const void* = 0)
	{
		return __n != 0 ? static_cast<_Tp*>(_Alloc::allocate(__n * sizeof(_Tp))) : 0;
	}

	//空间的释放函数
	// __p is not permitted to be a null pointer.
	void deallocate(pointer __p, size_type __n)
    {
		_Alloc::deallocate(__p, __n * sizeof(_Tp));
	}

	size_type max_size() const __STL_NOTHROW
    {
	    return size_t(-1) / sizeof(_Tp);
	}

	//对象的构建
	void construct(pointer __p, const _Tp& __val)
	{
		new(__p) _Tp(__val); //定位new表达式，在指定位置上构建对象
	}

	//对象的销毁
	void destroy(pointer __p)
	{
		__p->~_Tp();
	}

private:
     typedef alloc _Alloc;

};

//对于alloc的探究，也就是探究两级空间配置器
typedef alloc _Alloc;

# ifdef __USE_MALLOC
//一级空间配置器底层使用了malloc
typedef malloc_alloc alloc;

typedef __malloc_alloc_template<0> malloc_alloc;

template <int __inst>
class __malloc_alloc_template
{
public:
static void* allocate(size_t __n)
  {
      void* __result = malloc(__n);
      if (nullptr == __result)
        __result = _S_oom_malloc(__n);//out of memory

      return __result;
  }
};

else
//二级空间配置器
typedef __default_alloc_template<__NODE_ALLOCATOR_THREADS, 0> alloc;

template <bool threads, int inst>
class __default_alloc_template
{
private:
    enum {_ALIGN = 8};//对齐
	//最大字节数128，认为128就是大字节（类似之前facebook的folly库，255字节是大字节）
    enum {_MAX_BYTES = 128};
	//自由链表，也就是数组的维度
    enum {_NFREELISTS = 16};

#if defined(__SUNPRO_CC) || defined(__GNUC__) || defined(__HP_aCC)
    static _Obj* __STL_VOLATILE _S_free_list[];
#else
    static _Obj* __STL_VOLATILE _S_free_list[_NFREELISTS];
#endif

     union _Obj
	 {
        union _Obj* _M_free_list_link;
        char _M_client_data[1];    /* The client sees this.        */
	};

  // Chunk allocation state.
  //这个就是与内存池相关的两个指针（分别指向内存池的头与内存池的尾），以及记录申请的堆空间的大小
  static char* _S_start_free;
  static char* _S_end_free;
  static size_t _S_heap_size;

public:
    void* allocate(size_t __n)
	{
		if(__n > 128)
		{
			malloc(__n);
		}
		else
		{
			//16个自由链表 + 内存池
		}
	}


	 static void deallocate(void* __p, size_t __n)//__n = 32
  {
    if (__n > (size_t) _MAX_BYTES)
      malloc_alloc::deallocate(__p, __n);
    else
	{
		//用完的内存空间直接重新挂回到对应下标的自由链表下面
      _Obj* *  __my_free_list = _S_free_list + _S_freelist_index(__n);//_S_free_list[3]
      _Obj* __q = (_Obj*)__p;

      __q -> _M_free_list_link = *__my_free_list;
      *__my_free_list = __q;

    }
};

//_S_start_free与_S_end_free指向内存池的首位
char* __default_alloc_template::_S_start_free = nullptr;

char* __default_alloc_template::_S_end_free = nullptr;

size_t __default_alloc_template::_S_heap_size = 0;

//返回对应的下标值
 static  size_t _S_freelist_index(size_t __bytes) //__bytes = 32
 {
	 return (((__bytes) + (size_t)_ALIGN-1)/(size_t)_ALIGN - 1);
	   (32  + 8 - 1)/8 - 1 = 4 - 1 = 3
  }

//__bytes  [25,32],向上取整，得到8的整数倍
static size_t  _S_round_up(size_t __bytes) //__bytes = 32
{
     return (((__bytes) + (size_t) _ALIGN-1) & ~((size_t) _ALIGN - 1));

	 (32 + 8 - 1)&~(8 - 1)  = 39 & ~ 7
	 0000 0111
	 1111 1000

	 39 = 32 + 4 + 2 + 1 = 0010  0111
	 39 & 1111 1000
	 0010  0111


	 0010  0111
   & 1111  1000
     0010  0000


	 38 & ~ 7
}
//1、当申请的n的大小是32字节的时候(一次性申请了40个32字节，1280)
//__size = 32
//__nobjs = 20

//该函数会进行真正空间的申请
char* __default_alloc_template::_S_chunk_alloc(size_t __size, int& __nobjs)
{
    char* __result;
    size_t __total_bytes = __size * __nobjs = 32 * 20 = 640;
    size_t __bytes_left = _S_end_free - _S_start_free = 0;

	else {
        size_t __bytes_to_get = 2 * __total_bytes + _S_round_up(_S_heap_size >> 4)
		                         = 2 * 640 = 1280 ;
		_S_start_free = (char*)malloc(__bytes_to_get) = malloc(1280);

		 _S_heap_size += __bytes_to_get = 1280;
        _S_end_free = _S_start_free + __bytes_to_get;
        return(_S_chunk_alloc(__size, __nobjs));
	}
	//递归调用
	 char* __result;
    size_t __total_bytes = __size * __nobjs = 32 * 20 = 640;
    size_t __bytes_left = _S_end_free - _S_start_free = 1280;

	 if (__bytes_left >= __total_bytes)
	 {
        __result = _S_start_free;
        _S_start_free += __total_bytes;
        return(__result);
    }
}

//将申请好的空间挂接在对应的自由链表下面，每次以__n的大小为一个等分
void*  __default_alloc_template::_S_refill(size_t __n)//__n = 32
{
    int __nobjs = 20;
    char* __chunk = _S_chunk_alloc(__n, __nobjs);
    _Obj* __STL_VOLATILE* __my_free_list;
    _Obj* __result;
    _Obj* __current_obj;
    _Obj* __next_obj;
    int __i;

	__my_free_list = _S_free_list + _S_freelist_index(__n);//_S_free_list[3]

	__result = (_Obj*)__chunk;
      *__my_free_list = __next_obj = (_Obj*)(__chunk + __n);
      for (__i = 1; ; __i++)
	  {
        __current_obj = __next_obj;
        __next_obj = (_Obj*)((char*)__next_obj + __n);
        if (__nobjs - 1 == __i)
		{
            __current_obj -> _M_free_list_link = 0;
            break;
        } else {
            __current_obj -> _M_free_list_link = __next_obj;
        }
      }
}

void* allocate(size_t __n)//__n = 32
{
		else
		{
			_Obj* * __my_free_list = _S_free_list + _S_freelist_index(__n);

			 _Obj*  __result = *__my_free_list;
           if (__result == nullptr)
               __ret = _S_refill(_S_round_up(__n));
           else {
             *__my_free_list = __result -> _M_free_list_link;
              __ret = __result;//下次再取__n大小的时候，就直接在自由链表进行获取，无需malloc
         }
		}
}
//2、当申请的n的大小是64字节的时候
//__size = 64
//__nobjs = 20
char* __default_alloc_template::_S_chunk_alloc(size_t __size, int& __nobjs)
{
    char* __result;
    size_t __total_bytes = __size * __nobjs = 64 * 20 = 1280;
    size_t __bytes_left = _S_end_free - _S_start_free = 640;

	else if (__bytes_left >= __size)
	{
        __nobjs = (int)(__bytes_left/__size) = 10;
        __total_bytes = __size * __nobjs = 640;
        __result = _S_start_free;
        _S_start_free += __total_bytes;//内存池已经是空的
        return(__result);
    }

}

void*  __default_alloc_template::_S_refill(size_t __n)//__n = 64
{
    int __nobjs = 20;
    char* __chunk = _S_chunk_alloc(__n, __nobjs);
    _Obj* __STL_VOLATILE* __my_free_list;
    _Obj* __result;
    _Obj* __current_obj;
    _Obj* __next_obj;
    int __i;


	__my_free_list = _S_free_list + _S_freelist_index(__n);//_S_free_list[7]
     __result = (_Obj*)__chunk;
      *__my_free_list = __next_obj = (_Obj*)(__chunk + __n);
      for (__i = 1; ; __i++) {
        __current_obj = __next_obj;
        __next_obj = (_Obj*)((char*)__next_obj + __n);
        if (__nobjs - 1 == __i) {
            __current_obj -> _M_free_list_link = nullptr;
            break;
        } else {
            __current_obj -> _M_free_list_link = __next_obj;
        }
      }
}

 static void* allocate(size_t __n)//__n = 64
  {
    void* __ret = 0;


    else {
      _Obj* * __my_free_list = _S_free_list + _S_freelist_index(__n);//_S_free_list[7]

	  _Obj* __RESTRICT __result = *__my_free_list;
      if (__result == nullptr)
        __ret = _S_refill(_S_round_up(__n));
      else {
        *__my_free_list = __result -> _M_free_list_link;
        __ret = __result;
      }
	}

//3、当申请的n的大小是96字节的时候
//__size = 96
//__nobjs = 20
char* __default_alloc_template::_S_chunk_alloc(size_t __size, int& __nobjs)
{
    char* __result;
    size_t __total_bytes = __size * __nobjs = 96 * 20 = 1920;
    size_t __bytes_left = _S_end_free - _S_start_free = 0;

	else {
        size_t __bytes_to_get = 2 * __total_bytes + _S_round_up(_S_heap_size >> 4)
		                         = 2 * 1920 + _S_round_up(1280 >> 4)
								  = 3840 + 80 = 3920;
	    _S_start_free = (char*)malloc(__bytes_to_get) = malloc(3920);

		 _S_heap_size += __bytes_to_get = 1280 + 3920 = 5200;
        _S_end_free = _S_start_free + __bytes_to_get;
        return(_S_chunk_alloc(__size, __nobjs));
	}
	//递归调用
	char* __result;
    size_t __total_bytes = __size * __nobjs = 96 * 20 = 1920;
    size_t __bytes_left = _S_end_free - _S_start_free = 3920;

    if (__bytes_left >= __total_bytes) {
        __result = _S_start_free;
        _S_start_free += __total_bytes;
        return(__result);//返回1920字节交个_S_refill,剩余2000字节存放在内存中
    }

}

void* __default_alloc_template::_S_refill(size_t __n)//__n = 96
{
    int __nobjs = 20;
    char* __chunk = _S_chunk_alloc(__n, __nobjs);//1920字节96  20等分
    _Obj* __STL_VOLATILE* __my_free_list;
    _Obj* __result;
    _Obj* __current_obj;
    _Obj* __next_obj;
    int __i;

	__my_free_list = _S_free_list + _S_freelist_index(__n);//_S_free_list[11]

    /* Build free list in chunk */
      __result = (_Obj*)__chunk;
      *__my_free_list = __next_obj = (_Obj*)(__chunk + __n);
      for (__i = 1; ; __i++) {
        __current_obj = __next_obj;
        __next_obj = (_Obj*)((char*)__next_obj + __n);
        if (__nobjs - 1 == __i) {
            __current_obj -> _M_free_list_link = 0;
            break;
        } else {
            __current_obj -> _M_free_list_link = __next_obj;
        }
      }
}
static void* allocate(size_t __n)//__n = 96
  {
    void* __ret = 0;
    else {
      _Obj* * __my_free_list = _S_free_list + _S_freelist_index(__n);//_S_free_list[11]

      _Obj* __RESTRICT __result = *__my_free_list;
      if (__result == nullptr)
        __ret = _S_refill(_S_round_up(__n));
      else {
        *__my_free_list = __result -> _M_free_list_link;
        __ret = __result;
      }
    }

    return __ret;
  };

//4、当申请的n的大小是72字节的时候,认为内存池空的，堆空间没有足够72字节
//__size = 72
//__nobjs = 20
char* __default_alloc_template::_S_chunk_alloc(size_t __size, int& __nobjs)
{
    char* __result;
    size_t __total_bytes = __size * __nobjs = 72 * 20 = 1440;
    size_t __bytes_left = _S_end_free - _S_start_free = 0;

	else {
        size_t __bytes_to_get = 2 * __total_bytes + _S_round_up(_S_heap_size >> 4)
		                         > 2 * 1440 = 2880 ;
		  _S_start_free = (char*)malloc(__bytes_to_get) = malloc(2880);

		   if (0 == _S_start_free)
		   {
			   size_t __i;
			   _Obj* __STL_VOLATILE* __my_free_list;
			   _Obj* __p;

			   //__size = 72
			   //_MAX_BYTES = 128
			   //_ALIGN = 8
			   //__i = 72 80 88 96 向上“借内存”
			   for (__i = __size; __i <= (size_t) _MAX_BYTES; __i += (size_t) _ALIGN)
			  {
				  ////_S_free_list[8]  _S_free_list[9] _S_free_list[10] _S_free_list[11]
				  __my_free_list = _S_free_list + _S_freelist_index(__i);
                  __p = *__my_free_list;
                if (nullptr != __p)
				{
                    *__my_free_list = __p -> _M_free_list_link;
                    _S_start_free = (char*)__p;
                    _S_end_free = _S_start_free + __i;//__i = 96
                    return(_S_chunk_alloc(__size, __nobjs));
                    // Any leftover piece will eventually make it to the
                    // right free list.
                }
            }
		   }

	//继续调用调用
	char* __result;
    size_t __total_bytes = __size * __nobjs = 72 * 20 = 1440;
    size_t __bytes_left = _S_end_free - _S_start_free = 96;

	else if (__bytes_left >= __size)
	{
        __nobjs = (int)(__bytes_left/__size) = 96/72 = 1;
        __total_bytes = __size * __nobjs = 72 * 1 = 72;
        __result = _S_start_free;
        _S_start_free += __total_bytes;
        return(__result);
    }

}
void* __default_alloc_template::_S_refill(size_t __n)//__n = 72
{
    int __nobjs = 20;
	//__nobjs传入的时候是20， 传出的时候是1
    char* __chunk = _S_chunk_alloc(__n, __nobjs);
    _Obj* __STL_VOLATILE* __my_free_list;
    _Obj* __result;
    _Obj* __current_obj;
    _Obj* __next_obj;
    int __i;

	 if (1 == __nobjs) return(__chunk);

}

 static void* allocate(size_t __n)//__n = 72
  {
    void* __ret = 0;

    else {
      _Obj* __STL_VOLATILE* __my_free_list //_S_free_list[8]
	  = _S_free_list + _S_freelist_index(__n);

	   _Obj* __RESTRICT __result = *__my_free_list;
      if (__result == nullptr)
        __ret = _S_refill(_S_round_up(__n));
      else {
        *__my_free_list = __result -> _M_free_list_link;
        __ret = __result;
      }
	}

```

### CPP基础总复习
静态数据成员  只能在实现文件。

优先写成const成员函数  因为参数多是const 数据成员

派生类的析构函数执行完成后会 自动调用基类的析构函数

类型适应  派生类对象之间适应

虚函数被访问的五种情况

抽象类 的构造函数用protected修饰 15：24

虚析构函数 因为析构函数是唯一的

重载 重定义  隐藏（就近）数据成员也可以隐藏

16：07  有可能

16：18  new/delete

默认参数 从右边到左边连续赋值 声明写即可

inline 不能写成头文件和实现文件 （ 函数模板 也是 ）

17:00  delete   工作步骤
