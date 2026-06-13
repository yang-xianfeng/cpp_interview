<a name="01d27bf6"></a>
## C++提升部分

对于一个工程、项目<br />面向对象的分析（OOA）：需求、做什么<br />面向对象的设计（OOD）：怎么样做<br />面向对象的编程（OOP）：

软件需求是一直都在变化的，想以最小的代价去满足需求的变化。

UML：统一建模语言，一个是类图、一个是序列图

<a name="95dc911f"></a>
### 类与类之间的关系

<a name="ae45318d"></a>
#### 1、继承（泛化）
可以使用空心三角箭头从派生类指向基类。<br />![image-20220616100904166.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655372502993-3f999aac-d0bc-45fe-9b16-1ec5c9acec2c.png#clientId=u6a86f877-173c-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=306&id=ua37aef6c&margin=%5Bobject%20Object%5D&name=image-20220616100904166.png&originHeight=461&originWidth=756&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31483&status=done&style=none&taskId=ueaec7deb-ed79-42b8-8cd0-793d18b50e9&title=&width=501.81817626953125)

<a name="b8b1826c"></a>
#### 2、关联关系
代码上：数据成员使用的是指针或引用。彼此时间不会负责对方生命周期的销毁

双向的关联关系（客户与订单之间的关系）（直接使用直线连接两个类）<br />![image-20220616101509244.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655361329006-8a85bef7-0c09-46f8-b934-7edaa4895dad.png#clientId=u6a86f877-173c-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u40a630ac&margin=%5Bobject%20Object%5D&name=image-20220616101509244.png&originHeight=187&originWidth=720&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7889&status=done&style=none&taskId=u74f12d39-f0cc-492d-9071-5fa99eb6180&title=)


单向的关联关系（条件变量知道互斥锁的存在，互斥锁不知道条件变量的存在，可以使用从条件变量到互斥所以的箭头）<br />![image-20220616101818628.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655361353715-ca41568f-ae22-4d09-8a37-fc210612f958.png#clientId=u6a86f877-173c-4&crop=0.0756&crop=0&crop=0.9298&crop=0.9416&from=drop&height=156&id=u96129cb0&margin=%5Bobject%20Object%5D&name=image-20220616101818628.png&originHeight=183&originWidth=742&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8022&status=done&style=none&taskId=u2bd111de-4aa3-46d6-a953-130b7fc39d1&title=&width=634)

<a name="b687644b"></a>
#### 3、聚合
从部分指向整体的一个空心菱形箭头，类与类之前表现问整体与部分的关系，整体部分并不负责局部部分的销毁，在代码上面可以使用指针或者引用。<br />![image-20220616102537451.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655361375192-e2c8d19b-56b0-4b79-ae87-d31821a05757.png#clientId=u6a86f877-173c-4&crop=0.0216&crop=0.0188&crop=0.8973&crop=0.9624&from=drop&height=382&id=u65d6e843&margin=%5Bobject%20Object%5D&name=image-20220616102537451.png&originHeight=436&originWidth=651&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20861&status=done&style=none&taskId=u014005f2-47ad-4d9e-b215-b4b2b023537&title=&width=570)

<a name="02413ab6"></a>
#### 4、组合
从部分指向整体的实心菱形箭头，整体部分会负责局部对象的销毁，可以将局部类创建的对象作为整体的数据成员。<br />![image-20220616103114664.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655361397106-d84404b0-4f32-4a70-a214-b53e0cbbc7cc.png#clientId=u6a86f877-173c-4&crop=0&crop=0.0631&crop=0.928&crop=1&from=drop&height=425&id=u2f20dc0a&margin=%5Bobject%20Object%5D&name=image-20220616103114664.png&originHeight=458&originWidth=729&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21157&status=done&style=none&taskId=u27bfed0b-14fe-47af-a8f8-36f34d3bca0&title=&width=676)

<a name="df02791f"></a>
#### 5、依赖
从A指向B的虚线箭头。在代码上面表现为：B作为A的成员函数参数；B作为A的成员函数的局部变量（B作为A的成员函数返回值）；A的成员函数调用B的静态方法<br />![image-20220616105717809.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655361497448-074ba091-0425-408b-973b-b9c90a50847a.png#clientId=u6a86f877-173c-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u75bf03de&margin=%5Bobject%20Object%5D&name=image-20220616105717809.png&originHeight=228&originWidth=661&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8676&status=done&style=none&taskId=u99250701-cb9f-44da-bc96-aef45f95f39&title=)

<a name="25f9c7fa"></a>
#### 总结
耦合：两个模块或者两个部分之间的连接关系。低耦合（让两个模块或者两个类之间的关系变得微弱一些）

1、继承表现的是类与类之间的纵向关系（垂直关系），其它四种表现的是类与类之间的横向关系<br />2、从耦合程度看的话：依赖 <  关联关系  <   聚合  <    组合     <  继承（泛化）<br />3、语义上：继承（A is  B）、关联、聚合、组合（A has B）、依赖（A use  B）<br />4、 组合+依赖（基于对象） vs  继承 + 虚函数（面向对象）

| 五大关系 | UML语义 | UML图例 |
| --- | --- | --- |
| 继承（泛化） | A is B   | 派生类指向基类的空心三角箭头 |
| 关联 | A has B  | 双向：直线 （一般是指针或者引用）<br />单向：知道 ——> 不知道 |
| 聚合 | A has B  |  空心菱形箭头，部分指向整体。   |
| 组合 | A has B  |  实心菱形箭头，部分指向整体   |
| 依赖 | A use B  |  虚线的箭头 ， 使用方 ----> 被调用方 |


<a name="0d365f63"></a>
### 面向对象的设计原则
总纲：**低耦合**（模块与模块之间，类与类之间的关系），**高内聚**（模块内部或者类内部的关系）

<a name="351f7e08"></a>
#### 1、单一职责原则
核心：一个类或者一个模块尽量只做一件事情，只有一个引起类或者模块变化的外因。<br />![image-20220616113503876.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655361538399-6b0eacb3-17b1-49b0-b827-32f5d631cece.png#clientId=u6a86f877-173c-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u39551d00&margin=%5Bobject%20Object%5D&name=image-20220616113503876.png&originHeight=625&originWidth=1034&originalType=binary&ratio=1&rotation=0&showTitle=false&size=77020&status=done&style=none&taskId=u7e9ea577-8a93-43d8-8920-725f0b432b4&title=)

<a name="ddb2bd54"></a>
#### 2、开闭原则
核心：对扩展开放，对修改关闭<br />![image-20220616113550808.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655361558304-01554bbc-60b7-43c0-b252-006881f3b475.png#clientId=u6a86f877-173c-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u19295e6d&margin=%5Bobject%20Object%5D&name=image-20220616113550808.png&originHeight=347&originWidth=1199&originalType=binary&ratio=1&rotation=0&showTitle=false&size=90977&status=done&style=none&taskId=u4ad9645b-ff28-4d46-ab45-cd5ffbb7865&title=)

<a name="684b11e9"></a>
#### 3、里氏替换原则
核心：派生类必须能够替代基类。<br />派生类不能隐藏（同名函数 会发生隐藏）基类的接口，增加的功能添加 1、 2、 3后缀。<br />![image-20220616143849859.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655372538234-03ad7fe8-ad75-475a-a555-035bdfcfc295.png#clientId=u6a86f877-173c-4&crop=0.0378&crop=0&crop=0.9604&crop=1&from=paste&height=411&id=u11c9d498&margin=%5Bobject%20Object%5D&name=image-20220616143849859.png&originHeight=612&originWidth=1116&originalType=binary&ratio=1&rotation=0&showTitle=false&size=150043&status=done&style=none&taskId=u4067e7e1-1977-48df-88e8-46acea0680f&title=&width=749)

```cpp
#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

class User {
public:
    User(const string &name)
    : _name(name)
    , _score(0) {

    }

    void consume(float delta) {
        cout << "void User::consume(float)" << endl;
        _score += delta;

        cout << ">>" << _name << "消费" << delta << endl;
    }
protected:
    string _name;
    float _score;
};

class VipUser
: public User {
public:
    VipUser(const string &name)
    : User(name)
    , _discount(1) {

    }

    void consume2(float delta)    {
        cout << "void VipUser::consume(float)" << endl;
        float tmp = delta * _discount;
        _score += tmp;

        /* if(_score > 1000 && _score < 5000) */
        if(_score > 1000)        {
            _discount = 0.9;
        }

        cout << ">>" << _name << "消费" << tmp << endl;
    }
private:
    float _discount;
};

void test(){
    User user("刘德华");
    user.consume(2000);
    user.consume(2000);

    cout <<endl;
    VipUser vip("张学友");
    vip.consume(2000);//隐藏
    vip.consume(2000);//隐藏
    vip.consume2(2000);//隐藏
    vip.consume2(2000);//隐藏
}

int main(int argc, char **argv){
    test();
    return 0;
}
```

<a name="91f76de4"></a>
#### 4、接口分离原则
核心：使用多个小的专门的接口，而不要使用一个大的总接口<br />![image-20220616144442460.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655372562849-701a7684-caa6-4d76-af81-b310f095f296.png#clientId=u6a86f877-173c-4&crop=0.0486&crop=0&crop=0.9568&crop=0.9351&from=paste&height=513&id=ucfd92fa9&margin=%5Bobject%20Object%5D&name=image-20220616144442460.png&originHeight=777&originWidth=1167&originalType=binary&ratio=1&rotation=0&showTitle=false&size=100219&status=done&style=none&taskId=u2fa354de-c4ff-40a8-855b-27354337d26&title=&width=771)

<a name="92d056ee"></a>
#### 5、依赖倒置原则
核心：面向接口编程，依赖于抽象(抽象是稳定的，具体的是在变化的)

在此处面向接口编程，说的就是纯虚函数，包含纯虚函数的类，称为抽象类，抽象类是稳定不变的。<br />![image-20220616145823521.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655372703462-19add4c3-d29b-47c3-9c95-bd29eec13bbe.png#clientId=u6a86f877-173c-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u43951664&margin=%5Bobject%20Object%5D&name=image-20220616145823521.png&originHeight=494&originWidth=1025&originalType=binary&ratio=1&rotation=0&showTitle=false&size=96949&status=done&style=none&taskId=u6c1cf32f-ac01-4988-89ae-0a1d2773e93&title=)<br />在大多数情况下，**开闭原则、里氏代换原则和依赖倒置原则**会**同时出现，开闭原则**是**目标，里氏代换原则**是**基础，依赖倒置原则**是**手段。**

<a name="432dab86"></a>
#### 6、最少知识原则
核心：尽量减少类与类之间的耦合程度，或者模块与模块的的关系

<a name="37acbf13"></a>
#### 7、组合复用原则
核心：尽量采用组合、聚合的方式而不是继承的方式来达到软件复用的目标<br />![image-20220616151738919.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655372725868-cd3fbeea-3d4a-4ff2-8c35-ec2193bf4ea6.png#clientId=u6a86f877-173c-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u5280b01c&margin=%5Bobject%20Object%5D&name=image-20220616151738919.png&originHeight=411&originWidth=1155&originalType=binary&ratio=1&rotation=0&showTitle=false&size=80195&status=done&style=none&taskId=ud01ac5a7-8fb3-4ccd-a625-27af0adf455&title=)



<a name="5e96b3de"></a>
### 文本查询扩展作业
```c
get_file实现的功能
1、创建一个文件输入流去进行读取文件，将每行数据存储到vector中   //shared_ptr<vector<string>>
2、将所有的字符串进行处理，全部都转换为小写//tolower
3、将每个合格的单词存入到map之中，将相应的行号也存在set中//map<string, shared_ptr<set<line_no>>>
```



<a name="6f342a94"></a>
## C++Day28

<a name="9e17ecdb"></a>
### 一、问题回顾
1、类与类之间的关系？

2、面向对象的七大设计原则？

<a name="d015413f"></a>
### 二、设计模式
《大话设计模式》<br />GOF的《设计模式：可复用面向对象软件的基础》

<a name="up9ej"></a>
#### 1、简单工厂模式
概述 <br />简单工厂模式又叫静态工厂方法模式。提供一个工厂类，在工厂类中做判断，根据传入的类型创造相应 的产品。当增加新的产品时，就需要修改工厂类。简单工厂模式提供了专门的工厂类用于创建对象，将 对象的创建和对象的使用分离开，它作为一种最简单的工厂模式在软件开发中得到了较为广泛的应用。 

类图  <br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655447237431-d64bf9a5-4ea3-479e-8256-aa13206a3bf4.png#clientId=uf2f4a045-cbc5-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=243&id=u32e8e598&margin=%5Bobject%20Object%5D&name=image.png&originHeight=334&originWidth=770&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53044&status=done&style=none&taskId=ue8b28979-7d30-4e3d-b226-d69d988273b&title=&width=560)

```cpp
// simpleFactory
#include <math.h>

#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

//满足面向对象设计原则
// 1、满足开放闭合原则
// 2、满足依赖倒置原则
class Figure {
public:
    virtual void display() = 0;
    virtual double area() = 0;
};

class Rectangle
    : public Figure {
public:
    Rectangle(double length = 0, double width = 0)
        : _length(length), _width(width) {
    }

    void display() override {
        cout << "Rectangle";
    }

    double area() override {
        return _length * _width;
    }

private:
    double _length;
    double _width;
};

class Circle
    : public Figure {
public:
    Circle(double radius = 0)
        : _radius(radius) {
    }

    void display() override {
        cout << "Circle";
    }

    double area() override {
        return 3.14 * _radius * _radius;
        ;
    }

private:
    double _radius;
};

class Triangle
    : public Figure {
public:
    Triangle(double a = 0, double b = 0, double c = 0)
        : _a(a), _b(b), _c(c) {
    }

    void display() override {
        cout << "Triangle";
    }

    double area() override {
        double tmp = (_a + _b + _c) / 2;

        return sqrt(tmp * (tmp - _a) * (tmp - _b) * (tmp - _c));
    }

private:
    double _a;
    double _b;
    double _c;
};

void func(Figure *pfig) {
    pfig->display();
    cout << "的面积 : " << pfig->area() << endl;
}

// 1、不符合开放闭合原则
// 2、不满足单一职责原则
//
//简单工厂（静态工厂）
class Factory {
public:
    static Figure *create(const string &name) {
        if (name == "rectangle") {
            //读取配置文件
            return new Rectangle(10, 20);
        } else if (name == "circle") {
            //读取配置文件
            return new Circle(10);
        } else if (name == "triangle") {
            //读取配置文件
            return new Triangle(3, 4, 5);
        }

        return nullptr;
    }
#if 0
    static Figure *createRectangle()
    {
        //读取配置文件
        //获取相应的长与宽
        return new Rectangle(10, 20);
    }

    static Figure *createCircle()
    {
        //读取配置文件
        //获取相应的长与宽
        return new Circle(10);
    }

    static Figure *createTriangle()
    {
        //读取配置文件
        //获取相应的长与宽
        return new Triangle(3, 4, 5);
    }
#endif
};
int main(int argc, char **argv) {
    //配置文件
    //...
    //...
    /* Rectangle rectangle(10, 20); */
    /* Circle circle(10); */
    /* Triangle triangle(3, 4, 5); */

    /* Figure *reac = Factory::createRectangle(); */
    /* Figure *circle = Factory::createCircle(); */
    /* Figure *triangle = Factory::createTriangle(); */

    Figure *reac = Factory::create("rectangle");
    Figure *circle = Factory::create("circle");
    Figure *triangle = Factory::create("triangle");

    func(reac);
    func(circle);
    func(triangle);
    return 0;
}
```


<a name="rFndt"></a>
#### 2、工厂方法
 概述 <br />在软件开发及运行过程中，经常需要创建对象，但常出现由于需求的变更，需要创建的对象的具体类型 也要经常变化。工厂方法通过采取虚函数的方法，实现了使用者和具体类型之间的解耦，可以用来解决 这个问题。工厂方法模式对简单工厂模式中的工厂类进一步抽象。核心工厂类不再负责产品的创建，而 是演变为一个抽象工厂角色，仅负责定义具体工厂子类必须实现的接口。同时，针对不同的产品提供不 同的工厂。即每个产品都有一个与之对应的工厂。这样，系统在增加新产品时就不会修改工厂类逻辑而 是添加新的工厂子类，从而弥补简单工厂模式对修改开放的缺陷。定义一个创建对象的接口，让子类决 定实例化哪个类。该模式使类对象的创建延迟到子类。 

类图  <br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655447293980-207bc4c0-d877-4bf6-90b3-d9bbc042faf1.png#clientId=uf2f4a045-cbc5-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=207&id=u78e8eb6a&margin=%5Bobject%20Object%5D&name=image.png&originHeight=285&originWidth=788&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49857&status=done&style=none&taskId=u5f643988-fa43-43cc-a646-1911d006c6e&title=&width=573.0909090909091)

```cpp
#include <math.h>

#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

//满足面向对象设计原则
// 1、满足开放闭合原则
// 2、满足依赖倒置原则
class Figure {
public:
    virtual void display() = 0;
    virtual double area() = 0;

    string _name;
};

class Rectangle
    : public Figure {
public:
    Rectangle(double length = 0, double width = 0)
        : _length(length), _width(width) {
    }

    void display() override {
        cout << "Rectangle";
    }

    double area() override {
        return _length * _width;
    }

private:
    double _length;
    double _width;
};

class Circle
    : public Figure {
public:
    Circle(double radius = 0)
        : _radius(radius) {
    }

    void display() override {
        cout << "Circle";
    }

    double area() override {
        return 3.14 * _radius * _radius;
        ;
    }

private:
    double _radius;
};

class Triangle
    : public Figure {
public:
    Triangle(double a = 0, double b = 0, double c = 0)
        : _a(a), _b(b), _c(c) {
    }

    void display() override {
        cout << "Triangle";
    }

    double area() override {
        double tmp = (_a + _b + _c) / 2;

        return sqrt(tmp * (tmp - _a) * (tmp - _b) * (tmp - _c));
    }

private:
    double _a;
    double _b;
    double _c;
};

void func(Figure *pfig) {
    pfig->display();
    cout << "的面积 : " << pfig->area() << endl;
}

//工厂方法
// 1、可以满足单一职责原则
// 2、满足开放闭合原则
// 3、依赖倒置原则
class Factory {
public:
    virtual Figure *create() = 0;
    virtual ~Factory() {}
};

class RectangleFactory
    : public Factory {
public:
    Figure *create() override {
        //读取配置文件
        return new Rectangle(10, 20);
    }
};

class CircleFactory
    : public Factory {
public:
    Figure *create() override {
        //读取配置文件
        return new Circle(10);
    }
};

class TriangleFactory
    : public Factory {
public:
    Figure *create() override {
        //读取配置文件
        return new Triangle(3, 4, 5);
    }
};
int main(int argc, char **argv) {
    //配置文件
    //...
    //...
    /* Rectangle rectangle(10, 20); */
    /* Circle circle(10); */
    /* Triangle triangle(3, 4, 5); */

    /* Figure *reac = Factory::createRectangle(); */
    /* Figure *circle = Factory::createCircle(); */
    /* Figure *triangle = Factory::createTriangle(); */

    Figure *reac = Factory::create("rectangle");
    Figure *circle = Factory::create("circle");
    Figure *triangle = Factory::create("triangle");

    func(reac);
    func(circle);
    func(triangle);
    return 0;
}

```

<a name="pPXg2"></a>
#### 3、抽象工厂
 在软件开发及运行过程中，经常面临着“一系列相互依赖的对象”的创建工作；而由于需求的变化，常常 存在更多系列对象的创建问题。 定义：提供一个接口，该接口负责创建一系列“相关或者相互依赖的对象”，无需指定它们具体的类。 

类图  <br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655447335689-d67cf3d2-5ff3-4a13-a78d-7a9d14a35a89.png#clientId=uf2f4a045-cbc5-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=339&id=u31a8a208&margin=%5Bobject%20Object%5D&name=image.png&originHeight=466&originWidth=803&originalType=binary&ratio=1&rotation=0&showTitle=false&size=98127&status=done&style=none&taskId=ucc3ece1d-e2f3-47d8-ace5-640c610b367&title=&width=584)

<a name="tY7Y6"></a>
#### 4、观察者模式
 在GOF的《设计模式：可复用面向对象软件的基础》一书中对观察者模式是这样定义的：定义对象的一 种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。 当一个对象发生了变化，关注它的对象就会得到通知；这种交互也成为发布-订阅（publish- subscribe）。  

![image.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655447358604-879c9248-71d7-4b4e-8311-088a121a1891.png#clientId=uf2f4a045-cbc5-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=302&id=udacd67fa&margin=%5Bobject%20Object%5D&name=image.png&originHeight=415&originWidth=744&originalType=binary&ratio=1&rotation=0&showTitle=false&size=82843&status=done&style=none&taskId=uf1a39dd9-cb9b-42f7-98fa-3faddc21be1&title=&width=541.0909090909091)

```cpp
#include <algorithm>
#include <iostream>
#include <list>
#include <memory>
#include <string>

using std::cout;
using std::endl;
using std::find;
using std::list;
using std::string;
using std::unique_ptr;

class Observer;

class Subject {
public:
    virtual void attach(Observer *pObserver) = 0;
    virtual void detach(Observer *pObserver) = 0;
    virtual void notify() = 0;

    virtual ~Subject() {}
};

class ConcreteSubject
    : public Subject {
public:
    void attach(Observer *pObserver) override;
    void detach(Observer *pObserver) override;
    void notify() override;

    void setStatus(int status) {
        _status = status;
    }

    int getStatus() const {
        return _status;
    }

private:
    list<Observer *> _obList;
    int _status;
};

class Observer {
public:
    virtual void update(int) = 0;
    virtual ~Observer() {}
};

class ConcreteObserverA
    : public Observer {
public:
    ConcreteObserverA(const string &name)
        : _name(name) {
    }
    void update(int value) {
        cout << "ConcreteObserverA " << _name << ", value = " << value << endl;
    }

private:
    string _name;
};

class ConcreteObserverB
    : public Observer {
public:
    ConcreteObserverB(const string &name)
        : _name(name) {
    }
    void update(int value) {
        cout << "ConcreteObserverB " << _name << ", value = " << value << endl;
    }

private:
    string _name;
};

void ConcreteSubject::attach(Observer *pObserver) {
    if (pObserver) {
        _obList.push_back(pObserver);
    }
}

void ConcreteSubject::detach(Observer *pObserver) {
    for (auto it = _obList.begin(); it != _obList.end(); ++it) {
        if (*it == pObserver) {
            _obList.remove(pObserver);
            break;
        }
    }
}

void ConcreteSubject::notify() {
    for (auto &ob : _obList) {
        ob->update(_status);
    }
}

int main(int argc, char **argv) {
    unique_ptr<ConcreteSubject> pSubject(new ConcreteSubject());
    unique_ptr<Observer> pObserverA(new ConcreteObserverA("lili"));
    unique_ptr<Observer> pObserverB(new ConcreteObserverB("lucy"));

    pSubject->setStatus(2);

    pSubject->attach(pObserverA.get());
    pSubject->attach(pObserverB.get());

    pSubject->notify();

    cout << endl;
    pSubject->detach(pObserverB.get());
    pSubject->setStatus(3);
    pSubject->notify();

    return 0;
}
```



<a name="a82b995d"></a>
### 三、线程的封装
![image-20220617143819669.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655468718559-a88d9973-614b-4f33-9aec-8f2b9df3163e.png#clientId=uf2f4a045-cbc5-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=135&id=u3836698e&margin=%5Bobject%20Object%5D&name=image-20220617143819669.png&originHeight=185&originWidth=666&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21662&status=done&style=none&taskId=ue49eeff1-1cc0-4dff-97a4-af6f7b09ae2&title=&width=484.3636363636364)<br />搜索C++，然后进行安装，就会出现C++

![image-20220617143854172.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655468735572-92b3b0b9-9020-4a91-ae85-30bf6e97905c.png#clientId=uf2f4a045-cbc5-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=228&id=u81f30693&margin=%5Bobject%20Object%5D&name=image-20220617143854172.png&originHeight=314&originWidth=614&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19232&status=done&style=none&taskId=u152f1832-4205-4824-a4ff-0d380950427&title=&width=446.54545454545456)

vim 多标签问题：<br />：bn切换到下一个<br />：bp切换到上一个<br />：bd可以关闭当前标签

vim 多列操作：<br />**ctrl + v 可视化，方向键 j，shift + i，输入相应的文字，最后按ESC**

<a name="xNRqo"></a>
#### 面向对象的线程封装

![image-20220617151503860.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655468784606-eb2879f9-7bbd-4f6b-bef7-a6d028d1ebda.png#clientId=uf2f4a045-cbc5-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u6c87ee46&margin=%5Bobject%20Object%5D&name=image-20220617151503860.png&originHeight=479&originWidth=421&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19937&status=done&style=none&taskId=uede0d5ea-e208-41f7-8e23-9fdb213ea89&title=)<br />1、threadFunc要设置为静态成员函数，消除this指针的影响<br />2、run方法如何在threadFunc中进行调用？可以在pthread_create方法中，将第四个参数使用this传进来，将this使用arg传进来，就可以在threadFunc中调用run方法，并且该run方法是可以体现多态，调用派生类run方法

<a name="6a756f9d"></a>
#### 基于对象的线程封装
![image-20220617153930141.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655468810140-a2cabe4c-0d18-415d-b40b-198146717b99.png#clientId=uf2f4a045-cbc5-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u2ddc0f40&margin=%5Bobject%20Object%5D&name=image-20220617153930141.png&originHeight=358&originWidth=926&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32757&status=done&style=none&taskId=ue1c7bc53-f7cf-42e2-ae3c-8b3af18e699&title=)<br />将run方法看做一个任务，使用bind与function的方法进行实现。

```cpp
int pthread_create(pthread_t *thread, const pthread_attr_t *attr,
                          void *(*start_routine) (void *), void *arg);
```


<a name="300b38cc"></a>
#### 生产者消费者
<a name="79ff8f90"></a>
##### 原理图
![image-20220617181300672.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655468868071-1b8c2e37-8785-4413-b82e-ead19f5dd9c1.png#clientId=uf2f4a045-cbc5-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ub608e0e1&margin=%5Bobject%20Object%5D&name=image-20220617181300672.png&originHeight=600&originWidth=880&originalType=binary&ratio=1&rotation=0&showTitle=false&size=41918&status=done&style=none&taskId=u1b2070aa-e120-4e94-9438-7d17ae7da48&title=)

<a name="VOCsA"></a>
##### 类图
![image-20220617181233214.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655468886750-e5151bcb-47d9-41ed-a29a-1df2096fa665.png#clientId=uf2f4a045-cbc5-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u9ed2285c&margin=%5Bobject%20Object%5D&name=image-20220617181233214.png&originHeight=869&originWidth=1169&originalType=binary&ratio=1&rotation=0&showTitle=false&size=91052&status=done&style=none&taskId=u4fbdd324-d28f-4c7b-b349-f2493f15c5d&title=)

mutex & condition
```cpp
// condition.h
#ifndef __CONDITION_H__
#define __CONDITION_H__

#include <pthread.h>

class MutexLock {
public:
    MutexLock();
    ~MutexLock();
    //...
    void lock();
    void unlock();
    pthread_mutex_t* getMutexLockPtr();

private:
    //...
    pthread_mutex_t _mutex;
};

class Condition {
public:
    Condition(MutexLock&);
    ~Condition();
    //...
    void wait();
    void notify();
    void notifyAll();

private:
    //...
    // pthread_mutex_t _mutex;
    MutexLock& _mutex;
    pthread_cond_t _cond;
};

#endif
```

```cpp
// condition.cc
#include "condition.h"

#include <stdio.h>

#include <iostream>

using std::cout;
using std::endl;

// class MutexLock

MutexLock::MutexLock() {
    int ret = pthread_mutex_init(&_mutex, nullptr);
    if (ret) {
        perror("pthread_mutex_init");
    }
}

MutexLock::~MutexLock() {
    int ret = pthread_mutex_destroy(&_mutex);
    if (ret) {
        perror("pthread_mutex_destroy");
    }
}

void MutexLock::lock() {
    int ret = pthread_mutex_lock(&_mutex);
    if (ret) {
        perror("pthread_mutex_lock");
    }
}

void MutexLock::unlock() {
    int ret = pthread_mutex_unlock(&_mutex);
    if (ret) {
        perror("pthread_mutex_unlock");
    }
}

pthread_mutex_t* MutexLock::getMutexLockPtr() {
    return &_mutex;
}

// class Condition

Condition::Condition(MutexLock& mutex)
    : _mutex(mutex) {
    pthread_cond_init(&_cond, nullptr);
}

Condition::~Condition() {
    pthread_cond_destroy(&_cond);
}

void Condition::wait() {
    pthread_cond_wait(&_cond, _mutex.getMutexLockPtr());  //_mutex
}

void Condition::notify() {
    pthread_cond_signal(&_cond);
}

void Condition::notifyAll() {
    pthread_cond_broadcast(&_cond);
}
```

TaskQueue
```cpp
// TaskQueue.h
#ifndef __TASKQUEUE_H__
#define __TASKQUEUE_H__

#include <iostream>
#include <queue>

#include "condition.h"

using std::cout;
using std::endl;
using std::queue;

class TaskQueue {
public:
    TaskQueue(size_t n);
    ~TaskQueue();

    bool empty() const;
    bool full() const;
    void push(const int &val);
    int pop();

private:
    size_t _queSize;
    queue<int> _que;
    MutexLock _mutex;
    Condition _notEmpty;
    Condition _notFull;
};

#endif
```

```cpp
// TaskQueue.cc
#include "TaskQueue.h"

TaskQueue ::TaskQueue(size_t n)
    : _queSize(n)
    , _que()
    , _mutex()
    ,_notEmpty(_mutex)
    , _notFull(_mutex) {
    cout << "constructor TaskQueue" << endl;
}
TaskQueue ::~TaskQueue() {
    cout << "destructor TaskQueue" << endl;
}

bool TaskQueue ::empty() const {
    return _que.size() == 0;
}
bool TaskQueue ::full() const {
    return _que.size() == _queSize;
}
void TaskQueue ::push(const int& val) {
    _mutex.lock();

    /* if (full()) // 可能虚假唤醒 */
    while (full()) {
        _notFull.wait();
    }
    _que.push(val);
    // 此时队列中有数据
    _notEmpty.notify();

    _mutex.unlock();
}
int TaskQueue ::pop() {
    _mutex.lock();

    /* if (empty()) // 可能虚假唤醒 */
    while (empty()) {
        _notEmpty.wait();
    }

    int tmp = _que.front();
    _que.pop();

    _notFull.notify();

    _mutex.unlock();

    return tmp;
}
```

Thread
```cpp
// Thread.h
#ifndef __THREAD_H__
#define __THREAD_H__

#include <pthread.h>

#include <iostream>

using std::cout;
using std::endl;

class Thread {
public:
    Thread();
    virtual ~Thread();
    void start();
    void join();

private:
    //线程入口函数
    static void *threadFunc(void *arg);
    //要实现的任务
    virtual void run() = 0;

private:
    pthread_t _thid;
    bool _isRunning;
};

#endif
```

```cpp
// Thread.cc
#include "Thread.h"

#include <stdio.h>

Thread::Thread()
    : _thid(0), _isRunning(false) {
    cout << "Thread()" << endl;
}

Thread::~Thread() {
    if (_isRunning) {
        // 分离线程
        pthread_detach(_thid);
    }
}

// unique_ptr<Thread> pth(new MyThread());
void Thread::start()  // this
{
    // shift + k
    int ret = pthread_create(&_thid, nullptr, threadFunc, this);
    if (ret) {
        perror("pthread_create");
        return;
    }

    _isRunning = true;
}

void Thread::join() {
    if (_isRunning) {
        pthread_join(_thid, nullptr);
        _isRunning = false;
    }
}

void *Thread::threadFunc(void *arg) {
    Thread *pth = static_cast<Thread *>(arg);
    if (pth) {
        // run方法如何调用，需要有对象，需要有Thread类型的对象或者指针
        //该指针可以从arg这里传进来,所以pthread_create第四个参数就不能
        //是nullptr
        pth->run();  //实现任务
    }

    /* return nullptr; */
    pthread_exit(nullptr);
}
```

Producer & consumer
```cpp
// PC.h
#ifndef __PC_H__
#define __PC_H__

#include <iostream>

#include "TaskQueue.h"
#include "Thread.h"

using std::cout;
using std::endl;

class Producer : public Thread {
public:
    Producer(TaskQueue &tq);
    ~Producer();

    void run() override;

private:
    TaskQueue &_taskQue;
};

class Consumer : public Thread {
public:
    Consumer(TaskQueue &tq);
    ~Consumer();

    void run() override;

private:
    TaskQueue &_taskQue;
};

#endif
```

```cpp
#include "PC.h"

#include <unistd.h>

#include "stdlib.h"

Producer::Producer(TaskQueue &tq)
    : _taskQue(tq) {
    cout << " Producer()" << endl;
}

Producer::~Producer() {}

void Producer::run() {
    int cnt = 20;
    /* ::srand(unsigned(NULL)); */
    ::srand(clock());
    while (cnt-- > 0) {
        int number = ::rand() % 100;
        _taskQue.push(number);
        cout << "producer >> number : " << number << endl;
        sleep(1);
    }
}

Consumer::Consumer(TaskQueue &tq)
    : _taskQue(tq) {
    cout << "Consumer()" << endl;
}

Consumer::~Consumer() {}

void Consumer::run() {
    int cnt = 20;
    while (cnt-- > 0) {
        int number = _taskQue.pop();
        cout << "consumer >> number : " << number << endl;
        sleep(1);
    }
}
```

测试： TestPC.cc
```cpp
// TestPC.cc
#include <iostream>
#include <memory>

#include "PC.h"

using std::cout;
using std::endl;
using std::unique_ptr;

int main(int argc, char **argv) {
    TaskQueue taskQue(10);
    unique_ptr<Thread> produce(new Producer(taskQue));
    unique_ptr<Thread> consume(new Consumer(taskQue));

    produce->start();
    consume->start();

    produce->join();
    consume->join();

    return 0;
}
```

```bash
$ g++ *.cc -lpthread
$ ./a.out 
constructor TaskQueue
Thread()
 Producer()
Thread()
Consumer()
producer >> number : 83
consumer >> number : 83
producer >> number : 86
consumer >> number : 86
producer >> number : 77
consumer >> number : 77
producer >> number : 15
consumer >> number : 15
producer >> number : 93
consumer >> number : 93
producer >> number : 35
consumer >> number : 35
producer >> number : 86
consumer >> number : 86
producer >> number : 92
consumer >> number : 92
producer >> number : 49
consumer >> number : 49
producer >> number : 21
consumer >> number : 21
producer >> number : 62
consumer >> number : 62
producer >> number : 27
consumer >> number : 27
producer >> number : 90
consumer >> number : 90
producer >> number : 59
consumer >> number : 59
producer >> number : 63
consumer >> number : 63
producer >> number : 26
consumer >> number : 26
producer >> number : 40
consumer >> number : 40
producer >> number : 26
consumer >> number : 26
producer >> number : 72
consumer >> number : 72
producer >> number : 36
consumer >> number : 36
destructor TaskQueue
```


优化版本：<br />锁 使用局部的栈对象托管资源（ RAII  ）<br />![image-20220618112322953.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655688164788-cf2d9ca5-0505-4926-b7b4-1fa3f4267068.png#clientId=uc26e4f5a-6aee-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=427&id=rq1KG&margin=%5Bobject%20Object%5D&name=image-20220618112322953.png&originHeight=587&originWidth=957&originalType=binary&ratio=1&rotation=0&showTitle=false&size=61388&status=done&style=none&taskId=u51a10b28-7e0f-4a0f-ae17-ceab8486421&title=&width=696)

```cpp
// TaskQueue.cc
#include "TaskQueue.h"

TaskQueue::TaskQueue(size_t queSize)
: _queSize(queSize)
, _que()
, _mutex()
, _notEmpty(_mutex)
, _notFull(_mutex) {
    
}

TaskQueue::~TaskQueue(){

}

bool TaskQueue::empty() const {
    return _que.size() == 0;
}

bool TaskQueue::full() const {
    return _que.size() == _queSize;
}

void TaskQueue::push(const int &value) {
    //lock与unlock必须要成对出现，否则会有死锁的困扰
    //利用RAII的思想
    /* _mutex.lock(); */
    MutexLockGuard autoLock(_mutex);//autoLock栈对象

    //当full为true的时候，_notFull会wait，假如wait被唤醒了，true
    /* if(full()) */
    while(full()) { //虚假唤醒    
        _notFull.wait();
    }

    _que.push(value);//队列中就有数据

    //retrun;
    _notEmpty.notify();

    /* _mutex.unlock(); */
}

int TaskQueue::pop() {
    /* _mutex.lock(); */
    //C++11,cppreference
    MutexLockGuard autoLock(_mutex);//autoLock栈对象

    /* if(empty()) */
    while(empty()) {
        _notEmpty.wait();//上半部与下半部
    }

    int tmp = _que.front();
    _que.pop();

    _notFull.notify();

    /* _mutex.unlock(); */

    return tmp;
}
```


<a name="4f104bfe"></a>
### 禁止复制
如果想体现对象语义的话，可以将类的拷贝构造函数与赋值运算符函数设置为私有的或者delete，还可以使用继承的观点，将基类的拷贝构造函数与赋值运算符函数删除或者设置为私有的，派生类继承基类的时候，就不能进行复制或者赋值。<br />![image-20220618114133089.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655688236298-799dfc69-1bfe-4b62-bd48-8ad118548ce9.png#clientId=uc26e4f5a-6aee-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=401&id=ua868c7ba&margin=%5Bobject%20Object%5D&name=image-20220618114133089.png&originHeight=551&originWidth=885&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29953&status=done&style=none&taskId=u395c8484-7351-4270-96b2-ac79bd71e7e&title=&width=643.6363636363636)


锁 不可复制 （ `class NoCopy` )
```cpp
// NoCopy.h
#ifndef  __NOCOPTABLE_H__
#define __NOCOPTABLE_H__

class NoCopyable {
public:
protected:
/* private: */
    NoCopyable(){}
    ~NoCopyable(){}

    NoCopyable(const NoCopyable &rhs) = delete;
    NoCopyable &operator=(const NoCopyable &rhs) = delete;
};

#endif
```



<a name="8abf822d"></a>
## C++Day29
<a name="rwXG4"></a>
### 一、问题回顾
1、设计模式？简单工厂、工厂方法、抽象工厂？观察者模式？<br />主要看使用场景，结合具体的例子进行理解

2、面向对象的思想与基于对象的思想解决问题？<br />基于对象的使用，就是使用bind与function结合使用的产物


将生产者与消费代码使用基于对象的思想进行改写？

<a name="VZFoI"></a>
#### 实现基于对象的生产者消费者问题 :
mutex & condition
```cpp
// condition.h
#ifndef __CONDITION_H__
#define __CONDITION_H__

#include <pthread.h>

class MutexLock {
public:
    MutexLock();
    ~MutexLock();
    //...
    void lock();
    void unlock();
    pthread_mutex_t* getMutexLockPtr();

private:
    //...
    pthread_mutex_t _mutex;
};

class Condition {
public:
    Condition(MutexLock&);
    ~Condition();
    //...
    void wait();
    void notify();
    void notifyAll();

private:
    //...
    // pthread_mutex_t _mutex;
    MutexLock& _mutex;
    pthread_cond_t _cond;
};

#endif
```

```cpp
// condition.cc
#include "condition.h"

#include <stdio.h>

#include <iostream>

using std::cout;
using std::endl;

// class MutexLock

MutexLock::MutexLock() {
    int ret = pthread_mutex_init(&_mutex, nullptr);
    if (ret) {
        perror("pthread_mutex_init");
    }
}

MutexLock::~MutexLock() {
    int ret = pthread_mutex_destroy(&_mutex);
    if (ret) {
        perror("pthread_mutex_destroy");
    }
}

void MutexLock::lock() {
    int ret = pthread_mutex_lock(&_mutex);
    if (ret) {
        perror("pthread_mutex_lock");
    }
}

void MutexLock::unlock() {
    int ret = pthread_mutex_unlock(&_mutex);
    if (ret) {
        perror("pthread_mutex_unlock");
    }
}

pthread_mutex_t* MutexLock::getMutexLockPtr() {
    return &_mutex;
}

// class Condition

Condition::Condition(MutexLock& mutex)
    : _mutex(mutex) {
    pthread_cond_init(&_cond, nullptr);
}

Condition::~Condition() {
    pthread_cond_destroy(&_cond);
}

void Condition::wait() {
    pthread_cond_wait(&_cond, _mutex.getMutexLockPtr());  //_mutex
}

void Condition::notify() {
    pthread_cond_signal(&_cond);
}

void Condition::notifyAll() {
    pthread_cond_broadcast(&_cond);
}
```

TaskQueue
```cpp
// TaskQueue.h
#ifndef __TASKQUEUE_H__
#define __TASKQUEUE_H__

#include <iostream>
#include <queue>

#include "condition.h"

using std::cout;
using std::endl;
using std::queue;

class TaskQueue {
public:
    TaskQueue(size_t n);
    ~TaskQueue();

    bool empty() const;
    bool full() const;
    void push(const int &val);
    int pop();

private:
    size_t _queSize;
    queue<int> _que;
    MutexLock _mutex;
    Condition _notEmpty;
    Condition _notFull;
};

#endif
```

```cpp
// TaskQueue.cc
#include "TaskQueue.h"

TaskQueue ::TaskQueue(size_t n)
    : _queSize(n)
    , _que()
    , _mutex()
    ,_notEmpty(_mutex)
    , _notFull(_mutex) {
    cout << "constructor TaskQueue" << endl;
}
TaskQueue ::~TaskQueue() {
    cout << "destructor TaskQueue" << endl;
}

bool TaskQueue ::empty() const {
    return _que.size() == 0;
}
bool TaskQueue ::full() const {
    return _que.size() == _queSize;
}
void TaskQueue ::push(const int& val) {
    _mutex.lock();

    /* if (full()) // 可能虚假唤醒 */
    while (full()) {
        _notFull.wait();
    }
    _que.push(val);
    // 此时队列中有数据
    _notEmpty.notify();

    _mutex.unlock();
}
int TaskQueue ::pop() {
    _mutex.lock();

    /* if (empty()) // 可能虚假唤醒 */
    while (empty()) {
        _notEmpty.wait();
    }

    int tmp = _que.front();
    _que.pop();

    _notFull.notify();

    _mutex.unlock();

    return tmp;
}
```

Thread(BO)
```cpp
// Thread.h
#ifndef __THREAD_H__
#define __THREAD_H__

#include <pthread.h>

#include <functional>
#include <iostream>

using std::bind;
using std::function;

using ThreadCallback = function<void()>;

using std::cout;
using std::endl;

class Thread {
public:
    Thread(ThreadCallback &&cb);
    ~Thread();
    void start();
    void join();

private:
    //线程入口函数
    static void *threadFunc(void *arg);
    //要实现的任务
    virtual void run() = 0;

private:
    pthread_t _thid;
    bool _isRunning;
    // 实现的任务的函数
    ThreadCallback _cb;
};

#endif
```

```cpp
// Thread.cc
#include "Thread.h"

#include <stdio.h>

Thread::Thread(ThreadCallback &&cb)
    : _thid(0), _isRunning(false), _cb(std::move(cb)) {
    cout << "Thread()" << endl;
}

Thread::~Thread() {
    if (_isRunning) {
        // 分离线程
        pthread_detach(_thid);
    }
}

// unique_ptr<Thread> pth(new MyThread());
void Thread::start()  // this
{
    // shift + k
    int ret = pthread_create(&_thid, nullptr, threadFunc, this);
    if (ret) {
        perror("pthread_create");
        return;
    }

    _isRunning = true;
}

void Thread::join() {
    if (_isRunning) {
        pthread_join(_thid, nullptr);
        _isRunning = false;
    }
}

void *Thread::threadFunc(void *arg) {
    Thread *pth = static_cast<Thread *>(arg);
    if (pth) {
        // run方法如何调用，需要有对象，需要有Thread类型的对象或者指针
        //该指针可以从arg这里传进来,所以pthread_create第四个参数就不能
        //是nullptr
        pth->_cb();  //回调函数
    }

    /* return nullptr; */
    pthread_exit(nullptr);
}
```

Productor & consumer (BO)
```cpp
// PC.h
#ifndef __PC_H__
#define __PC_H__

#include <iostream>

#include "TaskQueue.h"
#include "Thread.h"

using std::cout;
using std::endl;

class Producer {
public:
    Producer(TaskQueue &tq) : _taskQue(tq) {}
    ~Producer(){}
    // bo todo task
    void process();

private:
    TaskQueue &_taskQue;
};

class Consumer {
public:
    Consumer(TaskQueue &tq) : _taskQue(tq) {}
    ~Consumer(){};
    // bo todo task
    void process();

private:
    TaskQueue &_taskQue;
};

#endif
```

```cpp
#include "PC.h"

#include <unistd.h>

#include "stdlib.h"

void Producer::process() {
    int cnt = 20;
    ::srand(unsigned(NULL));
    while (cnt-- > 0) {
        int number = ::rand() % 100;
        _taskQue.push(number);
        cout << "producer >> number : " << number << endl;
        sleep(1);
    }
}

void Consumer::process() {
    int cnt = 20;
    while (cnt-- > 0) {
        int number = _taskQue.pop();
        cout << "consumer >> number : " << number << endl;
        sleep(1);
    }
}
```

测试： TestPC.cc(BO)
```cpp
#include <iostream>
#include <memory>

#include "PC.h"

using std::cout;
using std::endl;
using std::unique_ptr;

int main(int argc, char **argv) {
    TaskQueue taskQue(10);
    
    Producer produce(taskQue);
    Thread p(bind(&Producer::process, &produce));
    Consumer consume(taskQue);
    Thread c(bind(&Consumer::process, &consume));

    p.start();
    c.start();

    p.join();
    c.join();

    return 0;
}
```

```bash
$ g++ *.cc -lpthread
$ ./a.out 
constructor TaskQueue
Thread()
Thread()
producer >> number : 83
consumer >> number : 83
producer >> number : 86
consumer >> number : 86
producer >> number : 77
consumer >> number : 77
producer >> number : 15
consumer >> number : 15
producer >> number : 93
consumer >> number : 93
producer >> number : 35
consumer >> number : 35
producer >> number : 86
consumer >> number : 86
producer >> number : 92
consumer >> number : 92
producer >> number : 49
consumer >> number : 49
producer >> number : 21
consumer >> number : 21
producer >> number : 62
consumer >> number : 62
producer >> number : 27
consumer >> number : 27
producer >> number : 90
consumer >> number : 90
producer >> number : 59
consumer >> number : 59
producer >> number : 63
consumer >> number : 63
producer >> number : 26
consumer >> number : 26
producer >> number : 40
consumer >> number : 40
producer >> number : 26
consumer >> number : 26
producer >> number : 72
consumer >> number : 72
producer >> number : 36
consumer >> number : 36
destructor TaskQueue
```


对pthread_cond_signal的解释   查文档即可(`sudo apt install manpages-posix-dev`)<br />并且配套这个博客看看 [https://blog.csdn.net/u012351051/article/details/123783424](https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxcheckurl?requrl=https%3A%2F%2Fblog.csdn.net%2Fu012351051%2Farticle%2Fdetails%2F123783424&skey=%40crypt_d1b0a048_c65836ba3ec8aaed412520915f832d1c&deviceid=e677239400187942&pass_ticket=undefined&opcode=2&scene=1&username=@3a102e3a247ee4152405a21efc0fd0364c543f62ebd1f152980c4fef7291cf07)<br />![webwxgetmsgimg.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/916648/1655689443819-afbbd564-7efc-43de-b765-c9f44147749d.jpeg#clientId=uc26e4f5a-6aee-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=735&id=uf9ef27e2&margin=%5Bobject%20Object%5D&name=webwxgetmsgimg.jpg&originHeight=1011&originWidth=1455&originalType=binary&ratio=1&rotation=0&showTitle=false&size=220635&status=done&style=none&taskId=uae19012a-6108-4f93-bb20-15794a74467&title=&width=1058.1818181818182)


```bash
$ man pthread_cond_singal
       It is not safe to use the pthread_cond_signal() function in a signal handler that is invoked asynchronously. Even  if  it  were  safe,  there
       would still be a race between the test of the Boolean pthread_cond_wait() that could not be efficiently eliminated
Mutexes and condition variables are thus not suitable for releasing a waiting thread by signaling from code running in a signal handler.

RATIONALE
       If  an  implementation  detects  that  the value specified by the cond argument to pthread_cond_broadcast() or pthread_cond_signal() does not
       refer to an initialized condition variable, it is recommended that the function should fail and report an [EINVAL] error.
       
  Multiple Awakenings by Condition Signal
       On a multi-processor, it may be impossible for an implementation of pthread_cond_signal() to avoid the unblocking of  more  than  one  thread
       blocked on a condition variable. For example, consider the following partial implementation of pthread_cond_wait() and pthread_cond_signal(),
       executed by two threads in the order given. One thread is trying to wait  on  the  condition  variable,  another  is  concurrently  executing
       pthread_cond_signal(), while a third thread is already waiting.
       
       
       The  effect  is that more than one thread can return from its call to pthread_cond_wait() or pthread_cond_timedwait() as a result of one call
       to pthread_cond_signal().  This effect is called ``spurious wakeup''.  Note that the situation is  self-correcting  in  that  the  number  of
       threads that are so awakened is finite; for example, the next thread to call pthread_cond_wait() after the sequence of events above blocks.

       While this problem could be resolved, the loss of efficiency for a fringe condition that occurs only rarely is unacceptable, especially given
       that one has to check the predicate associated with a condition variable anyway. Correcting  this  problem  would  unnecessarily  reduce  the
       degree of concurrency in this basic building block for all higher-level synchronization operations.
```

<a name="fonZJ"></a>
# C++ day30

`unique_ptr`  只有移动语义，放入容器需要先`std::move(up)`

<a name="d41d8cd9"></a>
## 

<a name="cf94f3a4"></a>
### 基于对象的线程池代码
<a name="597fd978"></a>
#### 类图![image-20220620180025724.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655729632168-784c6ad9-65e2-4c76-919e-4801f18a8b6e.png#clientId=uc26e4f5a-6aee-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u0e03e672&margin=%5Bobject%20Object%5D&name=image-20220620180025724.png&originHeight=841&originWidth=1490&originalType=binary&ratio=1&rotation=0&showTitle=false&size=110043&status=done&style=none&taskId=ue0f23028-5fad-4fb8-a150-1e43669538f&title=)

<a name="83175ad0"></a>
#### 代码实现

1、如果保证任务队列TaskQueue中的任务全部都执行完毕？![image-20220620145406921.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655729658130-fc3537b5-d082-4351-8d50-e0ffeb9860b1.png#clientId=uc26e4f5a-6aee-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=udce4cc08&margin=%5Bobject%20Object%5D&name=image-20220620145406921.png&originHeight=493&originWidth=867&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36189&status=done&style=none&taskId=u405297e4-e3c6-4902-a37f-27604e52b5a&title=)

2、如何将线程池退出来？<br />工作线程执行getTask函数，如果执行的速度过慢，任务是可以执行完毕的，并且也可以退出；但是如果执行的速度非常快，就会卡在ThreadPool中的threadFunc中，也就是其中的getTask函数，也就是TaskQueue的pop方法上面，也就是卡在_notEmpty条件变量的wait上面，所以可以让这些线程不用睡眠，直接唤醒。可以使用notifyAll函数。<br />![image-20220620173058286.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655729686364-a016bfe0-2d50-493b-897c-0d52e9ddce3b.png#clientId=uc26e4f5a-6aee-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u6bebe145&margin=%5Bobject%20Object%5D&name=image-20220620173058286.png&originHeight=669&originWidth=1167&originalType=binary&ratio=1&rotation=0&showTitle=false&size=74121&status=done&style=none&taskId=ubc2b861c-6ea4-4105-940c-9d60398e8eb&title=)

但是又会有一个问题，虽然唤醒了子线程，但是判断条件仍然是while，所以需要进一步修改。<br />![image-20220620173356896.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655729702752-e1a0f773-1c4a-455a-8899-bc4da3195b75.png#clientId=uc26e4f5a-6aee-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u416b5b5f&margin=%5Bobject%20Object%5D&name=image-20220620173356896.png&originHeight=655&originWidth=944&originalType=binary&ratio=1&rotation=0&showTitle=false&size=82877&status=done&style=none&taskId=uc3c1130a-7b84-40fe-ae57-dbfc5c9d907&title=)

完整代码：

NoCopy.h
```cpp
// NoCopy.h
#ifndef __NOCOPTABLE_H__
#define __NOCOPTABLE_H__

class NoCopyable {
public:
protected:
    /* private:  // can't  */
    NoCopyable() {
    }
    ~NoCopyable() {
    }

    NoCopyable(const NoCopyable &rhs) = delete;
    NoCopyable &operator=(const NoCopyable &rhs) = delete;
};

#endif
```

MutexLock
```cpp
// MutexLock.h
#ifndef __MUTEXLOCK_H__
#define __MUTEXLOCK_H__

#include <pthread.h>

#include "NoCopyable.h"

class MutexLock
    : NoCopyable {
public:
    MutexLock();
    ~MutexLock();
    void lock();
    void unlock();

    pthread_mutex_t *getMuextLockPtr() {
        return &_mutex;
    }

private:
    pthread_mutex_t _mutex;
};

class MutexLockGuard {
public:
    MutexLockGuard(MutexLock &mutex)
        : _mutex(mutex) {
        _mutex.lock();
    }

    ~MutexLockGuard() {
        _mutex.unlock();
    }

private:
    MutexLock &_mutex;
};

#endif
```

```cpp
// MutexLock.cc
#include "MutexLock.h"

#include <stdio.h>

MutexLock::MutexLock() {
    int ret = pthread_mutex_init(&_mutex, nullptr);
    if (ret) {
        perror("pthread_mutex_init");
    }
}

MutexLock::~MutexLock() {
    int ret = pthread_mutex_destroy(&_mutex);
    if (ret) {
        perror("pthread_mutex_destroy");
    }
}

void MutexLock::lock() {
    int ret = pthread_mutex_lock(&_mutex);
    if (ret) {
        perror("pthread_mutex_lock");
    }
}

void MutexLock::unlock() {
    int ret = pthread_mutex_unlock(&_mutex);
    if (ret) {
        perror("pthread_mutex_unlock");
    }
}
```

Condition
```cpp
// Condition.h
#ifndef __CONDITION_H__
#define __CONDITION_H__

#include <pthread.h>

#include "NoCopyable.h"

class MutexLock;  //前向声明

class Condition
    : NoCopyable {
public:
    Condition(MutexLock &mutex);
    ~Condition();
    void wait();
    void notify();
    void notifyAll();

private:
    pthread_cond_t _cond;
    MutexLock &_mutex;
};

#endif
```

```cpp
// Condition.cc
#include "Condition.h"

#include "MutexLock.h"

Condition::Condition(MutexLock &mutex)
    : _mutex(mutex) {
    pthread_cond_init(&_cond, nullptr);
}

Condition::~Condition() {
    pthread_cond_destroy(&_cond);
}

void Condition::wait() {
    pthread_cond_wait(&_cond, _mutex.getMuextLockPtr());  //_mutex
}

void Condition::notify() {
    pthread_cond_signal(&_cond);
}

void Condition::notifyAll() {
    pthread_cond_broadcast(&_cond);
}
```

Task.h
```cpp
// Task.h
#ifndef __TASK_H__
#define __TASK_H__

class Task {
public:
    virtual void process() = 0;
    virtual ~Task() {}
};

#endif
```

TaskQueue.h
```cpp
// TaskQueue.h
#ifndef __TASKQUEUE_H__
#define __TASKQUEUE_H__

#include <queue>

#include "Condition.h"
#include "MutexLock.h"
#include "Task.h"

using std::queue;

using Elem = Task *;

class TaskQueue {
public:
    TaskQueue(size_t queSize);
    ~TaskQueue();
    bool empty() const;
    bool full() const;
    void push(const Elem &value);
    Elem pop();

    //将所有的等在在_notEmpty上的线程唤醒
    void wakeup();

private:
    size_t _queSize;
    queue<Elem> _que;
    MutexLock _mutex;
    Condition _notEmpty;
    Condition _notFull;
    bool _flag;
};

#endif
```

```cpp
// TaskQueue.cc
#include "TaskQueue.h"

TaskQueue::TaskQueue(size_t queSize)
    : _queSize(queSize)
    , _que()
    , _mutex()
    , _notEmpty(_mutex)
    , _notFull(_mutex)
    , _flag(true) /* 初始为true,因为原先while()里条件为true(可以直接加入括号中 &&),
    所有任务完成时, 只需将flag修改为false,while(flag && ... )就不满足了 */ {

}

TaskQueue::~TaskQueue() {

}

bool TaskQueue::empty() const {
    return _que.size() == 0;
}

bool TaskQueue::full() const {
    return _que.size() == _queSize;
}

void TaskQueue::push(const Elem &value) {
    MutexLockGuard autoLock(_mutex);  // autoLock栈对象

    // while() 避免虚假唤醒
    while (full()) { 
        _notFull.wait();
    }

    _que.push(value);  //队列中就有数据

    _notEmpty.notify();
}

Elem TaskQueue::pop() {
    MutexLockGuard autoLock(_mutex);  // autoLock栈对象
    
    // while() 避免虚假唤醒
    while (_flag && empty()) {
        _notEmpty.wait();  //上半部与下半部
    }

    if (_flag) {
        // flag == true  // to do task
        Elem tmp = _que.front();
        _que.pop();

        _notFull.notify();

        return tmp;
    } else {
        // flag == false  // tasks all completed
        return nullptr;
    }
}

void TaskQueue::wakeup() {
    _flag = false;
    _notEmpty.notifyAll();
}
```



Thread.h
```cpp
// Thread.h
#ifndef __THREAD_H__
#define __THREAD_H__

#include <pthread.h>

#include "NoCopyable.h"

class Thread
    : NoCopyable {
public:
    Thread();
    virtual ~Thread();
    void start();
    void join();

private:
    //线程入口函数
    static void *threadFunc(void *arg);
    //要去实现的任务
    virtual void run() = 0;

private:
    pthread_t _thid;
    bool _isRunning;
};

#endif
```

```cpp
// Thread.cc
#include "Thread.h"

#include <stdio.h>

Thread::Thread()
    : _thid(0), _isRunning(false) {
}

Thread::~Thread() {
    if (_isRunning) {
        pthread_detach(_thid);
    }
}

// unique_ptr<Thread> WorkThreaad(new wt(xx));
void Thread::start() /* this */ {
    int ret = pthread_create(&_thid, nullptr, threadFunc, this);
    if (ret) {
        perror("pthread_create");
        return;
    }

    _isRunning = true;
}

void Thread::join() {
    if (_isRunning) {
        pthread_join(_thid, nullptr);
        _isRunning = false;
    }
}

void *Thread::threadFunc(void *arg) {
    Thread *pth = static_cast<Thread *>(arg);
    if (pth) {
        // run方法如何调用，需要有对象，需要有Thread类型的对象或者指针
        //该指针可以从arg这里传进来,所以pthread_create第四个参数就不能
        //是nullptr
        pth->run();  //实现任务
    }

    /* return nullptr; */
    pthread_exit(nullptr);
}
```

WorkThread.h
```cpp
// WorkThread.h
#ifndef __WORKTHREAD_H__
#define __WORKTHREAD_H__

#include "Thread.h"
#include "ThreadPool.h"

/* class ThreadPool; */

class WorkThread
    : public Thread {
public:
    WorkThread(ThreadPool &threadPool)
        : _threadPool(threadPool) {}

    void run() override {
        //执行真正的任务
        _threadPool.threadFunc();
    }

    ~WorkThread() {}

private:
    ThreadPool &_threadPool;
};

#endif
```


ThreadPool.h
```cpp
// ThreadPool.h
#ifndef __THREADPOOL_H__
#define __THREADPOOL_H__

#include <memory>
#include <vector>

#include "TaskQueue.h"
#include "Thread.h"

using std::unique_ptr;
using std::vector;

class ThreadPool {
    friend class WorkThread;

public:
    ThreadPool(size_t threadNum, size_t queSize);
    ~ThreadPool();

    void start();
    void stop();

    void addTask(Task *ptask);
    Task *getTask();

private:
    void threadFunc();

private:
    size_t _threadNum;
    size_t _queSize;
    vector<unique_ptr<Thread>> _threads;
    TaskQueue _taskQue;
    bool _isExit;
};

#endif
```

```cpp
// ThreadPool.cc
#include "ThreadPool.h"

#include <unistd.h>

#include "WorkThread.h"

ThreadPool::ThreadPool(size_t threadNum, size_t queSize)
    : _threadNum(threadNum)
    , _queSize(queSize)
    , _taskQue(_queSize)
    , _isExit(false) {
    _threads.reserve(_threadNum);
}

ThreadPool::~ThreadPool() {
    if (!_isExit) {
        stop();
        _isExit = true;
    }
}

//线程池开始执行的时候，其实就是工作线程已经开启
void ThreadPool::start() {
    for (size_t idx = 0; idx < _threadNum; ++idx) {
        unique_ptr<Thread> up(new WorkThread(*this));
        _threads.push_back(std::move(up));
    }

    for (auto &th : _threads) {
        th->start();  //创建工作线程的id，将工作线程开始运行
    }
}

//等同于在生产者消费者例子里面的生产者
void ThreadPool::addTask(Task *ptask) {
    if (ptask) {
        _taskQue.push(ptask);
    }
}

Task *ThreadPool::getTask() {
    return _taskQue.pop();
}

//线程池的退出，其实就是线程池中几个工作线程的退出，而工作线程
// WorkThread就是从Thread继承过来的，所以每个工作线程执行join
//方法就可以了
void ThreadPool::stop() {
    //只要任务队列中有数据，线程池中的工作线程就不能退出，让其sleep(1)
    while (!_taskQue.empty()) {
        sleep(1);
    }

    _isExit = true;
    //将所有等在在_notEmpty上的工作线程全部唤醒
    _taskQue.wakeup();
    for (auto &th : _threads) {
        th->join();
    }
}

//在线程池中封装的任务，这个任务的实际执行者WorkThread
void ThreadPool::threadFunc() {
    //只要线程池没有退出，就可以一直获取任务，并且执行相应的process
    while (!_isExit) {
        // getTask如果执行的非常慢的话，线程池的stop有可能先执行，会将
        //_isExit设置为true
        //但是如果getTask执行的过快的话，来不及将_isExit设置为true，
        //一直卡在getTask，也就是卡在Condition中的wait上面
        Task *ptask = getTask();
        if (ptask) {
            ptask->process();
        }
    }
}
```


测试文件：
```cpp
#include <stdlib.h>
#include <unistd.h>

#include <iostream>

#include "ThreadPool.h"

using std::cout;
using std::endl;

class MyTask
    : public Task {
private:
    void process() override {
        ::srand(clock());
        int number = ::rand() % 100;
        cout << "number = " << number << endl;
        /* sleep(1); */
    }
};

int main(int argc, char **argv) {
    unique_ptr<Task> task(new MyTask());

    ThreadPool threadPool(5, 10);
    threadPool.start();  //五个子线程创建并运行

    int cnt = 20;
    while (cnt-- > 0) {
        threadPool.addTask(task.get());
        cout << "cnt = " << cnt << endl;
        /* sleep(1); */
    }

    threadPool.stop();  //五个子线程进行退出

    return 0;
}
```


<a name="de9580e4"></a>
### 基于对象的线程池
<a name="iJpbe"></a>
#### 类图
![image-20220620180025724.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655732271853-03e63c63-c992-4572-adfa-a8ec567d60cf.png#clientId=uc26e4f5a-6aee-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u2e69362e&margin=%5Bobject%20Object%5D&name=image-20220620180025724.png&originHeight=841&originWidth=1490&originalType=binary&ratio=1&rotation=0&showTitle=false&size=110043&status=done&style=none&taskId=uaf7efc72-e9bd-4bec-a165-a94aed1e068&title=)<br />基于对象的时候，bind绑定到成员函数的时候，可以使用值传递，也可以使用地址传递<br />![image-20220620163032834.png](https://cdn.nlark.com/yuque/0/2022/png/916648/1655729746780-7fd023fc-59c0-4c2e-9f9f-22b5b135adc8.png#clientId=uc26e4f5a-6aee-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u37798a48&margin=%5Bobject%20Object%5D&name=image-20220620163032834.png&originHeight=471&originWidth=1086&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53812&status=done&style=none&taskId=ue7934ea9-f285-403b-adec-3c67280f3e6&title=)


完整代码：

Nocopy.h
```cpp
// NoCopy.h
#ifndef __NOCOPTABLE_H__
#define __NOCOPTABLE_H__

class NoCopyable {
public:
protected:
    /* private: */
    NoCopyable() {
    }
    ~NoCopyable() {
    }

    NoCopyable(const NoCopyable &rhs) = delete;
    NoCopyable &operator=(const NoCopyable &rhs) = delete;
};

#endif
```

MutexLock.h
```cpp
// MutexLock.h
#ifndef __MUTEXLOCK_H__
#define __MUTEXLOCK_H__

#include <pthread.h>

#include "NoCopyable.h"

class MutexLock
    : NoCopyable {
public:
    MutexLock();
    ~MutexLock();
    void lock();
    void unlock();

    pthread_mutex_t *getMuextLockPtr() {
        return &_mutex;
    }

private:
    pthread_mutex_t _mutex;
};

class MutexLockGuard {
public:
    MutexLockGuard(MutexLock &mutex)
        : _mutex(mutex) {
        _mutex.lock();
    }

    ~MutexLockGuard() {
        _mutex.unlock();
    }

private:
    MutexLock &_mutex;
};

#endif
```

```cpp
// MutexLock.cc
#include "MutexLock.h"

#include <stdio.h>

MutexLock::MutexLock() {
    int ret = pthread_mutex_init(&_mutex, nullptr);
    if (ret) {
        perror("pthread_mutex_init");
    }
}

MutexLock::~MutexLock() {
    int ret = pthread_mutex_destroy(&_mutex);
    if (ret) {
        perror("pthread_mutex_destroy");
    }
}

void MutexLock::lock() {
    int ret = pthread_mutex_lock(&_mutex);
    if (ret) {
        perror("pthread_mutex_lock");
    }
}

void MutexLock::unlock() {
    int ret = pthread_mutex_unlock(&_mutex);
    if (ret) {
        perror("pthread_mutex_unlock");
    }
}
```

Condition.h
```cpp
// Condition.h
#ifndef __CONDITION_H__
#define __CONDITION_H__

#include <pthread.h>

#include "NoCopyable.h"

class MutexLock;  //前向声明

class Condition
    : NoCopyable {
public:
    Condition(MutexLock &mutex);
    ~Condition();
    void wait();
    void notify();
    void notifyAll();

private:
    pthread_cond_t _cond;
    MutexLock &_mutex;
};

#endif
```

```cpp
// Condition.cc
#include "Condition.h"

#include "MutexLock.h"

Condition::Condition(MutexLock &mutex)
    : _mutex(mutex) {
    pthread_cond_init(&_cond, nullptr);
}

Condition::~Condition() {
    pthread_cond_destroy(&_cond);
}

void Condition::wait() {
    pthread_cond_wait(&_cond, _mutex.getMuextLockPtr());  //_mutex
}

void Condition::notify() {
    pthread_cond_signal(&_cond);
}

void Condition::notifyAll() {
    pthread_cond_broadcast(&_cond);
}

```


Task.h(BO)
```cpp
// Task.h
#ifndef __TASK_H__
#define __TASK_H__

#include <functional>

using std::function;

using Task = function<void()>;

#endif
```

TaskQueue.h(BO)
```cpp
// TaskQueue.h
#ifndef __TASKQUEUE_H__
#define __TASKQUEUE_H__

#include <queue>

#include "Condition.h"
#include "MutexLock.h"
#include "Task.h"

using std::queue;

using Elem = function<void()>;

class TaskQueue {
public:
    TaskQueue(size_t queSize);
    ~TaskQueue();
    bool empty() const;
    bool full() const;
    void push(Elem &&value);
    Elem pop();

    //将所有的等在在_notEmpty上的线程唤醒
    void wakeup();

private:
    size_t _queSize;
    queue<Elem> _que;
    MutexLock _mutex;
    Condition _notEmpty;
    Condition _notFull;
    bool _flag;
};

#endif
```

```cpp
// TaskQueue.cc
#include "TaskQueue.h"

TaskQueue::TaskQueue(size_t queSize)
    : _queSize(queSize)
    , _que(), _mutex()
    , _notEmpty(_mutex)
    , _notFull(_mutex)
    , _flag(true) {
}

TaskQueue::~TaskQueue() {
}

bool TaskQueue::empty() const {
    return _que.size() == 0;
}

bool TaskQueue::full() const {
    return _que.size() == _queSize;
}

void TaskQueue::push(Elem &&value) {
    MutexLockGuard autoLock(_mutex);  // autoLock栈对象

    while (full())  //虚假唤醒
    {
        _notFull.wait();
    }

    _que.push(std::move(value));  //队列中就有数据

    _notEmpty.notify();
}

Elem TaskQueue::pop() {
    MutexLockGuard autoLock(_mutex);  // autoLock栈对象

    while (_flag && empty()) {
        _notEmpty.wait();  //上半部与下半部
    }

    if (_flag) {
        Elem tmp = _que.front();
        _que.pop();

        _notFull.notify();

        return tmp;
    } else {
        return nullptr;
    }
}

void TaskQueue::wakeup() {
    _flag = false;
    _notEmpty.notifyAll();
}
```

Thread.h (BO)
```cpp
// Thread.h
#ifndef __THREAD_H__
#define __THREAD_H__

#include <pthread.h>

#include <functional>

using std::bind;
using std::function;

using ThreadCallback = function<void()>;

class Thread {
public:
    Thread(ThreadCallback &&cb);
    ~Thread();
    void start();
    void join();

private:
    //线程入口函数
    static void *threadFunc(void *arg);

private:
    pthread_t _thid;
    bool _isRunning;
    //要去实现的任务
    ThreadCallback _cb;
};

#endif
```

```cpp
// Thread.cc
#include "Thread.h"

#include <stdio.h>

Thread::Thread(ThreadCallback &&cb)
    : _thid(0), _isRunning(false), _cb(std::move(cb)) {
}

Thread::~Thread() {
    if (_isRunning) {
        pthread_detach(_thid);
    }
}

// unique_ptr<Thread> pthread(new MyThread());
void Thread::start()  // this
{
    // shift + k
    int ret = pthread_create(&_thid, nullptr, threadFunc, this);
    if (ret) {
        perror("pthread_create");
        return;
    }

    _isRunning = true;
}

void Thread::join() {
    if (_isRunning) {
        pthread_join(_thid, nullptr);
        _isRunning = false;
    }
}

void *Thread::threadFunc(void *arg) {
    Thread *pth = static_cast<Thread *>(arg);
    if (pth) {
        pth->_cb();  //回调函数
    }

    // return nullptr
    pthread_exit(nullptr);
}
```

ThreadPool.h(BO)
```cpp
//ThreadPool.h
#ifndef __THREADPOOL_H__
#define __THREADPOOL_H__

#include <memory>
#include <vector>

#include "TaskQueue.h"
#include "Thread.h"

using std::unique_ptr;
using std::vector;

class ThreadPool {
public:
    ThreadPool(size_t threadNum, size_t queSize);
    ~ThreadPool();

    void start();
    void stop();

    void addTask(Task &&cb);
    Task getTask();

private:
    void threadFunc();

private:
    size_t _threadNum;
    size_t _queSize;
    vector<unique_ptr<Thread>> _threads;
    TaskQueue _taskQue;
    bool _isExit;
};

#endif
```

```cpp
// ThreadPool.cc
#include "ThreadPool.h"

#include <unistd.h>

ThreadPool::ThreadPool(size_t threadNum, size_t queSize)
    : _threadNum(threadNum)
    , _queSize(queSize)
    , _taskQue(_queSize)
    , _isExit(false) {
    _threads.reserve(_threadNum);
}

ThreadPool::~ThreadPool() {
    if (!_isExit) {
        stop();
        _isExit = true;
    }
}

//线程池开始执行的时候，其实就是工作线程已经开启
void ThreadPool::start() {
    for (size_t idx = 0; idx < _threadNum; ++idx) {
        /* unique_ptr<Thread> up(new WorkThread(*this)); */
        unique_ptr<Thread> up(new Thread(std::bind(&ThreadPool::threadFunc, this)));
        _threads.push_back(std::move(up));
    }

    for (auto &th : _threads) {
        th->start();  //创建工作线程的id，将工作线程开始运行
    }
}

//等同于在生产者消费者例子里面的生产者
void ThreadPool::addTask(Task &&task) {
    if (task) {
        _taskQue.push(std::move(task));
    }
}

Task ThreadPool::getTask() {
    return _taskQue.pop();
}

//线程池的退出，其实就是线程池中几个工作线程的退出，而工作线程
// WorkThread就是从Thread继承过来的，所以每个工作线程执行join
//方法就可以了
void ThreadPool::stop() {
    //只要任务队列中有数据，线程池中的工作线程就不能退出，让其
    // sleep
    while (!_taskQue.empty()) {
        sleep(1);
    }

    _isExit = true;
    //将所有等在在_notEmpty上的工作线程全部唤醒
    _taskQue.wakeup();
    for (auto &th : _threads) {
        th->join();
    }
}

//在线程池中封装的任务，这个任务的实际执行者WorkThread
void ThreadPool::threadFunc() {
    //只要线程池没有退出，就可以一直获取任务，并且执行
    //相应的process
    while (!_isExit) {
        // getTask如果执行的非常慢的话，线程池的stop有可能先执行，会将
        //_isExit设置为true
        //但是如果getTask执行的过快的话，来不及将_isExit设置为true，
        //一直卡在getTask，也就是卡在Condition中的wait上面
        Task taskcb = getTask();
        if (taskcb) {
            taskcb();
        }
    }
}
```

测试文件：
```cpp
#include <stdlib.h>
#include <unistd.h>

#include <iostream>

#include "ThreadPool.h"

using std::cout;
using std::endl;

class MyTask {
public:
    void process() {
        ::srand(clock());
        int number = ::rand() % 100;
        cout << "bo_threadpool.number = " << number << endl;
    }
};

int func(int *number) {
}

void test() {
    int a = 10;
    func(&a);
}
int main(int argc, char **argv) {
    MyTask task;

    ThreadPool threadPool(5, 10);
    threadPool.start();  //五个子线程创建并运行

    int cnt = 20;
    while (cnt-- > 0) {
        //如果在此处task的生命周期达到了，使用地址传递的话，
        //会有相应的空指针的问题
        threadPool.addTask(std::bind(&MyTask::process, &task));  //地址传递
        /* threadPool.addTask(std::bind(&MyTask::process, task));//值传递 */
        cout << "cnt = " << cnt << endl;
    }

    threadPool.stop();  //五个子线程进行退出

    return 0;
}
```
