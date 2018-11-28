# 列表学习
# 任意类型的有序集合,没有固定的大小,可修改.
# 列表支持所有字符串的序列操作
l1 = [1, 'spam', 3.1415]
# 切片操作
'''
print(l1[0])
print(l1[0:2])
print(l1[-1])
# pop insert 以及 remove方法
print(l1.pop())
print(l1)
print(l1.pop(0))
print(l1)
print(l1.insert(0, 1))
print(l1)
print(l1.insert(2, 3.1415))
print(l1)
l1.remove(3.1415)
#l1.remove(3)
print(l1)
l2 = [2, 5, 7, 3]
l2.sort()
print(l2)
l2.reverse()
print(l2)
l2.append(100)
print(l2)
'''
# 列表可以支持任意类型的嵌套
m = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(m)
print(m[1][2])

# 列表解析表达式, 方便且处理速度快
col2 = [row[1] for row in m]
print(col2)
col2Plus = [row[1] + 1 for row in m]
print(col2Plus)
col2If = [row[1] + 1 for row in m if row[1] % 2 == 0]
print(col2If)

doublec = [c * 2 for c in 'spam']
print(doublec)

diag = [m[i][i] for i in [0,1,2]]
print(diag)

sum1 = [sum(row) for row in m]
print(sum1)
sum2 = list(map(sum, m))
print(sum2)