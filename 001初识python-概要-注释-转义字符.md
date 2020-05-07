####官方发布python版本定义
Python的版本号分为三段，形如A.B.C。其中A表示大版本号，一般当整体重写，或出现不向后兼容的改变时，增加A；B表示功能更新，出现新功能时增加B；C表示小的改动（例如：修复了某个Bug），只要有修改就增加C。

####安装Python解释器
想要开始Python编程之旅，首先得在自己使用的计算机上安装Python解释器环境，下面将以安装官方的Python解释器为例，讲解如何在不同的操作系统上安装Python环境。官方的Python解释器是用C语言实现的，也是使用最为广泛的Python解释器，通常称之为CPython。除此之外，Python解释器还有Java语言实现的Jython、C#语言实现的IronPython以及PyPy、Brython、Pyston等版本。

####确认Python的版本
在windows环境下，在cmd命令行提示符中输入python --version
或者在交互式环境中，输入以下：
python
import sys
print(sys.version_info)
-->sys.version_info(major=3, minor=6, micro=4, releaselevel='final', serial=0)
print(sys.version)
-->3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)]

####两种执行python文件的方法
python 1.py
./1.py
在程序的1.py文本里加入#!/usr/bin/python（linux环境下）
再加上print("ni hao"),然后 ./1.py就可以执行解释这个程序

####代码中的注释
#我是单行注释
"""
我是多行注释
不参与运算、逻辑
"""
'''
这也是多行注释
也是
'''

变量的类型            数字---------int
                          ----------long（长整型，也可以代表8进制或者16进制）
                          ----------float
                          ----------complex（复数）(4+5j->4代表实部，5代表虚部，j代表虚部单位)
                    布尔类型
                    string
                    list
                    tuple
                    dictionary
如果想要看变量a的类型type(a)

#标识符用大小驼峰法，myName小驼峰，MyName大驼峰

#转义字符
\\    反斜杠
\‘    单引号
\“    双引号
\b    退格
\000  空
\n    换行
\v    纵向制表符
\t    横向制表符
\r    回车



####print打印hello world
print('hello world!')
-->hello world!
print('hello','world!')
--->hello world!
print('hello','world',sep=', ',end='!\n')  #默认sep为空格，end为换行
-->hello,world!
