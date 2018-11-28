#字符串的模式匹配
import re
s = 'Hello      python world'
match = re.match('Hello[ \t]*(.*)world', s)
print(match.groups())

s1 = '/usr/bin/abc'
match2 = re.match('/(.*)/(.*)/(.*)', s1)
print(match2.groups())