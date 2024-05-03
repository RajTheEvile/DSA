class Solution:
    def checkValidString(self, s: str) -> bool:
        ma=0
        mi=0
        for i in s:
            if i =='(':
                mi+=1
                ma+=1
            elif i==')':
                mi=max(0,mi-1)
                ma-=1
            else:
                mi=max(0,mi-1)
                ma+=1
            if ma<0:
                return False
        
        return mi==0