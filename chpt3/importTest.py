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

#from xxx import yyy 这种方式,直接复制了模块的属性, 使得simple中的x变量成为了该模块的直接变量.
#使用imoprt这种方式,则需要使用simple.x书写, 是对属性x的一个引用.