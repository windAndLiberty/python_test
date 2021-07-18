#字符计数
import pprint
def characterCount(message):
    count={}
    if(not isinstance(message,str)):
        return
    for c in message:
        count.setdefault(c,0)
        count[c]+=1
    return pprint.pformat(count)
message='It was a bright cold day in April, and the clocks are striking thirteen.'
print(characterCount(message))
