class Solution:
    def maxArea(self, x1: List[int]) -> int:
        x=0
        y=len(x1)-1
        z=0
        while x<y:
            a=min(x1[x],x1[y])*(y-x)
            z=max(z,a)
            if x1[x]<x1[y]:
                x+=1
            else:
                y-=1
        return z
        