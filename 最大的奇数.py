intList=[]
for i in range(10):
    t=int(input("enter an integer:"))
    intList.append(t)
oddNumbers=[]
for i in range(10):
    if(intList[i]%2==1):
        oddNumbers.append(intList[i])
if(len(oddNumbers)==0):
    print("no odd number")
max=oddNumbers[0]
for i in range(1,len(oddNumbers)):
    if(oddNumbers[i]>max):
        max=oddNumbers[i]
print("maxium=",max)

    
    
