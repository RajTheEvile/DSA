class Solution:
    def decodeString(self, s: str) -> str:
        x=[]        
        out=''
        num=0
        
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            
            elif i=='[':
                x.append(out)
                x.append(num)
                out=''
                num=0
            
            elif i==']':
                pnum=x.pop()
                pstr=x.pop()
                out=pstr+pnum*out
            else:
                out+=i
        
        return out