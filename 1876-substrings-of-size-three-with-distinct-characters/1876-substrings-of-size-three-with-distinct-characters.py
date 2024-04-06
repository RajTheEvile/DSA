class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i=0
        j=3
        k=0
        while j<len(s)+1:
            c=s[i:j]
            c=list(c)
            d=set(c)
            if len(c)==len(d):
                k+=1
            i+=1
            j+=1
        return k
            