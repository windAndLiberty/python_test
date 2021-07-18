#! /usr/bin/python3
#getPassword.pw  (insecure password locker)
Passwords={'emails':'sdnfionfiosa',
           'blog':'j14jo1h42h./'}
import sys,pyperclip
if(len(sys.argv)!=2):
    print('usage: python getPassword.py [account] - copy account password')
    sys.exit()
account=sys.argv[1]
if account in Passwords:
     pyperclip.copy(Passwords[account])
     print('Password of '+account+' had been copied to clipBoard')
else: 
     print('Cannot find the password of '+account) 