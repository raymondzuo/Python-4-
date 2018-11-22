#在执行以下代码之前,先执行"编译",转成字节码,字节码的后缀是.pyc.字节码可以以文件的形式存在,也可以在内存中存在.然后转发到虚拟机
#pvm(python虚拟机不是一个独立的程序,无需安装, pvm时一个迭代运行字节码的一个大循环.python解释器的最后一步)
#pysco是一个类似与JIT的东西,能有效的加速字节码的解释速度.
#pvm + pyc字节码 + 必要的python支持文件 组成了可以分发的"冻结二进制文件" Frozen Binary. 比如:py2exe, pyinstaller
#python解释器就是运行python程序的程序
#/usr/bin/python3.5
print('hello, world!')
print(2**100)