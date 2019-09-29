## 开源——Python测评工具

[Github仓库](https://github.com/SheepHuan/CPGJ)

本次实验作业的测评工具仅使用Python语言编写。

**程序思路是基于文本的快速匹配**。

**编译test.py运行**

## 1.GUI界面

GUI界面使用了PyQt5完成，简单、易用

## 2.操作逻辑

### 2.1 作业要求

​        首先要求同学代码统一使用循环读入字符串的形式读入数据，保证了数据读入的效率。

然后直接使用print(json.dumps(dic))的形式打印出答案，保证输出格式统一。

一行输入对于一行输出。主文件以学号命名，如 **‘041702324.py’**

### 2.2 代码获取

直接使用gitpython库，在测评工具下提取指定链接地址的github仓库。将作业代码及其依赖文件clone到本地文件夹。保证了程序运行时所需要的依赖文件，如.json .xlsx等

### 2.3 程序执行

在程序执行前，为保证程序输入，输出正确。我们使用了输入输出重定向的方式。   

但是，第一次时遇到了windows的致命问题，windows控制台下的中文编码并非是utf-8

格式式，并且无法正确转换编码。

于是借鉴了丁枢桐同学的思路，直接修改测评代码，正在代码前后分别加上以下代码。

```python
# -*- coding: utf-8 -*-
import sys,os
sys.stdin=open(r'./input.txt','r',encoding='utf-8')
sys.stdout=open(r'./output.txt','w',encoding='utf-8')
...
sys.stdout.close()
sys.stdin.close()

```

直接使用sys库的stdin,stdout，重定向input,print的数据接收和输出方向。

然后执行

```python
os.system('python '+文件名)
```

控制台下直接运行python程序

### 2.4 答案比对

获取到2.3的output.txt后，与标准答案 answer.txt逐行比对即可。



## 3.  程序的性能比较

本测评工具不仅在功能上包含了天枢星的单个测试点比较的功能，保证程序bug不会使你程序终止为0分，同时考虑到了**python性能较差**的方面，如果程序使用了大量的附加文件如xlsx,json等导致程序运行缓慢，如果单个输入输出，会导致测试较慢。于是我们使用快速程序直接单次运行下读入全部数据，和输出全部数据。
