class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        j=k
        mi=[]
        while j<len(nums)+1:
            c=nums[i:j]
            x=max(c)-min(c)
            mi.append(x)
            i+=1
            j+=1
        return min(mi)