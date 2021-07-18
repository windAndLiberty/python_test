#! /usr/bin/python3
#一位数随机乘法式:show input outcome (loop)
import random
def toInt(z):
   if z=='#':
      return -1
   try:
     return int(z)
   except ValueError:
     print('请输入一个数字')
     return 0
   
print('随机一位数乘法运算开始（输入#结束程序） ：')
x,y=(0,0)
while True:
   x=random.randint(1,10)
   y=random.randint(1,10)
   print(str(x)+'X'+str(y)+'=',end='')
   z=toInt(input())
   if(z==-1):
      break
   elif(z==0):
      continue
   if(z==x*y):
      print('恭喜你，答对了')
   else:
      print('答错了，正确答案是'+str(x*y))
      
      
   