'''
#数字的类型,支持整数,浮点数,固定精度的十进制,有理分数,集合,boolean, 无穷整数精度,各种数字内置函数
#允许使用二进制,八进制,十六进制表示整数
#python3.0以后,只有一种整数表示
b = 0b1000
o = 0o71
n16 = 0x11a
print(b, o, n16)
#表达式操作符:+ - * / >> ** &
#内置的数学函数 pow abs round hex bin
#公用模块 random math
b2 = b << 1
print(b2)
f = 0.333333
print('%4.2f'%f,'|')
#除法需要注意一下,分为传统除法,floor除法,和真除法, python3去掉了传统除法
c = 5 / 2 #真除法
print(c)
d = 5 // 2 # floor除法
print(d)
e = 5 // -2 #向下截断,结果是-3
print(e)

#函数转化为非十进制
dec = 16
print("Oct: ", oct(dec), " Hex: ", hex(dec), " Bin: ", bin(dec))
print(int('0b100', 2))

#其他常用的内置函数 min max sum pow abs
g = -1
print(abs(g))
print(pow(2,2))
print(sum([1,2,3,4]))
print(min([1,2,3]))
import math
print(round(2.3), round(2.51), math.trunc(2.5), math.trunc(-2.7), math.floor(2.3), math.floor(2.7))

#sqrt
print(math.sqrt(4), 4 ** .5, pow(4, .5))
# 小数数字
print(0.1 + 0.1 + 0.1 - 0.3)
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) #注意decimal的参数是字符串,且小数位数是结果期望的位数

# 集合类型
x = set('abcde')
y = set('bdxyz')
print(x, y)
print('a' in x, x - y, x | y, x & y, x ^ y)
for item in x:
    print(item)
#x.update(y)
#print(x)
z = set([1,2,3])
z.add(4)
print(z)

xx = {x ** 2 for x in [1,2,3]}
print(xx)
'''
#Bool类型
bl = 1==1
print(bl)
blf = 1 == 2
print(blf)
print(type(blf))