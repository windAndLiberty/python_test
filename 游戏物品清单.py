inventory={'rope':1,'trigger':3,'torch':2,'gun':2}
dragonLoot=['rope','ruby','torch','torch']
def displayInventory(inv):
    print('inventory list:')
    num=0
    for k,v in inv.items():
        print(k+' '+str(v))
        num+=v
    print('Total number:'+str(num))
def addToInventory(inv,loot):
    for i in range(len(loot)):
        if(loot[i] in inv):
            inv[loot[i]]+=1
        else:
            inv.setdefault(loot[i],1)
displayInventory(inventory)
addToInventory(inventory,dragonLoot)
displayInventory(inventory)
