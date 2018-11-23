# Python程序由模块构成,模块包含语句,语句包含表达式,表达式建立并处理对象, 对象是最基本的概念.
# 尽量使用内置对象类型,原因有:1.更容易编写 2.运行效率更高 3.标准化
# 内置对象包含:数字,字符串,列表,字典,元组,文件,集合等 ,所有处理的东西都是对象,包括函数,模块,类等,万物皆对象
# 像数字\字符串这类的对象类型,称之为核心数据类型
# python是强类型动态语言
# 数字类型 
'''
import math #数学模块
print(math.pi)
import random#随机模块
print(random.random())
print(random.choice([1,2,3,4]))
'''
s = 'spam'
print(len(s))
print(s[1])
print(s[-1])
print(s[0:3]) #切片操作, 左边界默认为0,右边界不填表示截到最后一位(包含)
print(s[0:])
s2 = 'haha'
print(s + s2)
#字符串是不可变的,所有的对字符串的以上操作,不过是生成了新的字符串,数字类型,字符串和元组类型是不可变的
#列表和字典是可变的

i = s.find('pa')
print(i)
s3 = s.replace('p', 'w') #此处仍然不会更改s的值,而是生成了一个新的字符串
print(s3)
print(s)

#print(dir(s))#可以查看字符串下相关的属性方法
print(s.upper())
print(s.isalpha())
print(s)
#字符串的格式化
print('%s, haha, %s' % (s, s3))
print('{0} heihei, {1}'.format(s3, s))
#print(help(s.replace))
#允许字符串包含在单引号,双引号中,效果相同.
#三引号用于跨行字符串
print(ord('a'))