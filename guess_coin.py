import random
guess==''
while guess not in ('heads','tails'):
    print('guess the coin toss,enter heads or tails:')
    guess=input()
toss = random.randint(0,1) #0-tails,1-heads
if toss == guess:
head=0
for i in range(1,1001):
    if random.randint(0,1)==1:
        head+=1
    if i == 500:
        print('half done.')
print('head up '+str(head)+' times.')
