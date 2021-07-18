import copy
 
aList = ['1',2,'a',['b','c']]
bList = aList#将aList赋给bList
cList = copy.copy(aList)#浅拷贝
dList = copy.deepcopy(aList)#深拷贝
 
aList.append('test')#在aList末尾添加'test'
aList[3].append('list')#在aList中['b','c']的末尾添加'list'
 
print('aList:%s'% aList)
print('bList:%s'% bList)
print('cList:%s'% cList)
print('dList:%s'% dList)
