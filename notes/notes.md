## Linux
### 修改图片
```
// 把图缩放，最大边长2000像素，压缩比75%
convert -resize 2000 -quality 75% DSC_5795.JPG min_DSC_5795.JPG
```

### 安装软件
我们在使用Ubuntu安装程序时经常会遇到添加软件源的操作，最常见的是ppa软件源。ppa是Ubuntu Launchpad网站提供的一项服务，允许个人用户作为apt源供其他用户下载和更新。
```
sudo add-apt-repository ppa:rvm/smplayer
sudo apt-get update
sudo apt-get install ppa-name
```

deb包安装
```
sudo dpkg -i opera-stable_38.0.2220.29_i386.deb
```

下载文件使用wget命令
```
wget -r -np -pk -nH -P ./download http://www.baidu.com
```
安装rpm包
```
sudo alien flash-plugin-11.2.202.621-release.i386.rpm
```

### 网络
询进程占用哪些端口
```
netstat -nlap|grep 3573
```

### shell编程
```
for ((i=1;i<=41;i++))do echo filename$i.txt;done | xargs -i cat {} >> mynew.txt  //按顺序合并目录中的文件
```

### vim
[set the vim for python](http://www.linuxidc.com/Linux/2017-01/139565.htm)

[vim for C++](http://www.linuxidc.com/Linux/2016-06/132262.htm)

[ctags](http://www.cnblogs.com/zhangsf/archive/2013/06/13/3134409.html)
```
ctags -R *
Ctrl＋］  跳到当前光标下单词的标签
Ctrl＋O  返回上一个标签
Ctrl＋T  返回上一个标签
$	跳到行尾
```

## Git
```
git push origin master  //将修改提交到远端仓库
git remote add origin <server>  //添加远端仓库
git branch -a  //查询远程分支
git chenckout -b notes origin/notes   //获取远端分支
git config user.name "Kimi Athos"  //配置用户名
git add filename  //加入修改
git commit -s -m "Add info into notes.md"  //提交修改
git config user.email "sunx_2003@163.com"  //配置邮件地址
git push  //推送到远端分支
git diff origin/master  //比较与远端master分支的差异
```
git获取远程远程分支
```
git fetch origin notes  //把远程分之获取到本地
git log -p notes.. origin/notes   //查看本地分支与远程分支的差异
git merge origin/notes    //远程分支合并到本地
```

## ubuntu
```
gsettings set com.canonical.Unity.Launcher launcher-position Bottom  //任务栏底部
//点击任务栏最小化窗口
gsettings set org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/ launcher-minimize-window true
```
### FAQ
解决挂载NTFS分区失败
```
sudo apt-get install ntfs-3g //install ntfs-3g
locate ntfs-3g              //check the ntfs-3g is installed
sudo ntfsfix /dev/sda6      //fix the error disk partation
```

Fix the software-center exit:
```
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install --reinstall software-center
```

## java
```
jar vtf target/mvntest-1.0-SNAPSHOT.jar //查看jar包内容
java -jar target/mvntest-1.0-SNAPSHOT.jar   //执行jar包，jar包中要设置main-class
```
### maven
```
mvn archetype:generate  //生产maven工程
mvn install -Dmaven.test.skip = true  //-D是java的功能，设置一个java系统属性
```
[maven in action](http://hzbook.group.iteye.com/group/wiki/2872-Maven-in-action/)

在pom中增加plugin maven-shade-plugin，可以配置jar包的mainclass。main class带有main函数，可以通过java -jar命令直接执行jar包。

### IntelliJ IDEA
[IntelliJ IDEA使用教程](http://www.phperz.com/article/15/0923/159067.html)

## docker
```
docker images  //查询镜像
docker rm kimi  //删除容器
docker ps -a  //查询容器
docker commit 3dddc5237797 kimiubuntu  // 提交对容器做的修改，kimiubuntu为镜像名称
docker run -it --name kimi kimiubuntu /bin/bash // 启动一个容器
docker export 2a12b907f2b5 > kimiubuntu.tar  //将容器倒出
cat kimiubuntu.tar | docker import - kimi/ubuntu:1.0  // 倒入镜像
docker restart kimi
docker attach kimi
```

