#文件对象,核心类型,使用open函数创建该对象,使用'w'选项写文件
f = open('./test.dat','w')
f.writelines('haha')
f.close()

of = open('./test.dat')
lines = of.readlines()
for l in lines:
    print(l)
#print(of.read())
of.close()
#import os
#print(os.getcwd())