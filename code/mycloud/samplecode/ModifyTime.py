import os
import datetime

t = os.path.getmtime('/home/akash/mycloud/document.txt')
u = os.path.getmtime('document.txt')
print(t)
if t<u:
	print(datetime.datetime.fromtimestamp(t))
else:
	print('hello')


