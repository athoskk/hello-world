## autoconf and automake
[操作指导](http://blog.csdn.net/u011596455/article/details/60479696)

操作步骤：
1. `autoscan`命令生产configure.scan
2. 修改configure.scan，保存为configure.in
3. `aclocal`和`autoconf`命令，生成configure脚本
4. 在根目录和模块目录中增加Makefile.am文件
5. `automake --add-missing` 生成Makefile.in
6. `./configure`，生成Makefile
7. `make`构建工程

## cmake
[操作指导](https://www.ibm.com/developerworks/cn/linux/l-cn-cmake/)

## effective cpp
* C++ 不是使用一套规则的单一语言，而是 federation of four sublanguages（四种子语言的联合体），每一种都有各自的规则。在头脑中保持这些 sublanguages（子语言），你会发现对 C++ 的理解会容易得多。
* 在头文件中定义一个 constant char*-based string（基于 char* 的字符串常量）时，你必须写两次 const：
```C++
const char * const authorName = "Scott Meyers";
```
* 对于 simple constants（简单常量），用 const objects（const 对象）或 enums（枚举）取代 #defines。
* 对于 function-like macros（类似函数的宏），用 inline functions（内联函数）取代 #defines。
* C++ returns objects by value（以传值方式返回对象）这一事实
* 这种根据 const member function（成员函数）实现它的 non-const 版本的技术却非常值得掌握。
* 定义在不同转换单元内的非局部静态对象的初始化的相对顺序是没有定义的
* 当一个 derived class object（派生类对象）通过使用一个 pointer to a base class with a non-virtual destructor（指向带有非虚拟析构函数的基类的指针）被删除，则结果是未定义的。
* 如果一个 class（类）不包含 virtual functions（虚拟函数），这经常预示不打算将它作为 base class（基类）使用。不作为基类的类，不要使用虚函数
