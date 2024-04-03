class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        s=[]
        res=[1]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            c=0
            while s and heights[s[-1]]<heights[i]:
                s.pop()
                c+=1
            if s:
                res[i]+=c
            else:
                res[i]=c  
            s.append(i)
        return res