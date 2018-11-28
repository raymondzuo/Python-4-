# 字典承载的是一种映射关系
# 字典可以改变
# 字典时没有顺序的
dic = {1:"haha", "2x":"hahahaha", 3:"heihei"}
print(dic)
print(dic[1])
print(dic['2x'])
dic[4] = '4th'
print(dic)

#字典嵌套
rec = {'name':{'first':'ray', 'last':'zuo'},
       'job':['dev', 'mgr'],
       'age':30}
print(rec)
print(rec['name']['first'])
print(rec['job'][0])
print(rec['age'])
rec['job'].append('player')
print(rec)

#python垃圾回收,一旦一个对象的最后一次引用被移除,那么空间会立刻释放
#对字典的键进行排序
#先把key放到list中,然后排序,然后获取value
k = list(rec.keys())
k.sort()
for myk in k:
    print(myk, '=>', rec[myk])
#直接使用sorted
for k in sorted(rec):
    print(k, '....', rec[k])
if not 'haha' in rec:
    print('hasnot haha in rec dictionary')