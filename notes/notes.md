## Linux

#### 安装软件

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
####网络
询进程占用哪些端口
```
netstat -nlap|grep 3573
```

## Git
