class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num=str(num)
        k1=0
        i=0
        j=k
        while (j<=len(num)):
            c=num[i:j]
            c=int(c)
            if c!=0:
                if int(num)%int(c)==0:
                    k1+=1
            i+=1
            j+=1
        return k1