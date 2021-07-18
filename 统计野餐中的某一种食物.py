#对野餐的食物进行建模
allGuests={'alice':{'apple':3,'pie':6},
           'bob':{'pie':3,'sausage':5},
           'kachy':{'pretzel':4,'juice':6}}
def totalBrought(guests,item):
    num=0
    for k,v in allGuests.items():
        num+=v.get(item,0)
    return num
print('we have '+str(totalBrought(allGuests,'apple'))+' apples')
