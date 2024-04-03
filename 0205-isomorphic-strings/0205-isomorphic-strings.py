class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l1=[]
        l2=[]
        for i in s:
            l1.append(s.index(i))
        for i in t:
            l2.append(t.index(i))
        return l1==l2
        