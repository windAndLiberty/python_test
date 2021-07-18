def collatz(number):
    if(number%2==0):
        print(number//2)
        return number//2
    elif(number%2==1):
        print(3*number+1)
        return 3*number+1
print('please type an integer:')
while True:
    try:
        x=int(input())
        if(isinstance(x,int)):
               break
    except ValueError:
        print('you have to enter an integer')
        
while True:
    x=collatz(x)
    if(x==1):
        break
    
        
