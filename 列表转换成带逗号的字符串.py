#逗号代码
def hebing(l1):
    if(not isinstance(l1,list)):
        return
    s1=''
    for i in range(len(l1)-1):
        s1+=str(l1[i])+', '
    s1+='and '+str(l1[++i])
    return s1
spam=['apples','bananas','tofu','cats']
print(hebing(spam))
        
    
    
