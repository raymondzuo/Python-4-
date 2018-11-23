#!/usr/bin/python3
# 第一行的含义是指定运行该文件的程序路径
# 可以使用交互命令行,来测试单条或者多条python代码,很方便
# 默认回车后,立刻执行当前一行代码.
# 多行复合代码的使用: 以":"结尾的语句会被认为是复合语句,需要两次回车才能产生结果 
# 每个python源代码文件,称之为模块.
import sys
print(sys.platform)
x = 'spam'
print(x * 8)
