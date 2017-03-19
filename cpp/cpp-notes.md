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
