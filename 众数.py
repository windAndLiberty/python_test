n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
num={}
for i in range(n):
    if(l[i] not in num.keys):
         num.setdefault(l[i],1)
    else:
         num[l[i]]+=1
for i in range(num.len):
#TODO:select the biggest in num.values
    
    