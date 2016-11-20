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

远端仓库：
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

```

## ubuntu
```
gsettings set com.canonical.Unity.Launcher launcher-position Bottom  //任务栏底部
```

## maven
```
mvn archetype:generate  //生产maven工程
mvn install -Dmaven.test.skip = true  //-D是java的功能，设置一个java系统属性
```


