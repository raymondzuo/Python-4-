import simple
#from simple import x
#from imp import reload #py2.6
import imp


#print(x)
print(simple.x)
print(dir(simple)) #dir函数,返回指定模块的所有的属性
print(simple.__file__)
print(simple.__name__)
print(simple.__cached__) #pyc缓存的信息
print(simple.__package__)
#imp.reload(simple)
#reload(simple)#py2.6

# from xxx import yyy 这种方式,直接复制了模块的属性, 使得simple中的x变量成为了该模块的直接变量.
# 使用imoprt这种方式,则需要使用simple.x书写, 是对属性x的一个引用.
# from 复制的变量能够使本模块的同名变量失效.且没有任何警告
# 无论from还是import方式,都不需要加.py后缀名
# 除了以上两种方式以外,还可以使用exec(open(simple.py).read())来执行
# 但这种方式可能会覆盖本地的变量,因为这种方式更象是一种c语言的宏
# 命名空间 = 模块名 = 文件名去掉.py后缀
'''
x = 'heihei'
print(x)
exec(open('/home/rayzuo/test/python/chpt3/simple.py').read())
print(x)
'''