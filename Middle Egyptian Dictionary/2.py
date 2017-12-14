#-*-coding:utf-8-*-
import re

content = raw_input('Signs:(eg:G X F)')
st = content.split(' ')
rex = '\d+\s-\s'.join(st)
print rex
fx = 'G1 - X1 - F9'

match = re.search(rex, 'G1 - X1 - F9')

if match:
        print match.group(0)