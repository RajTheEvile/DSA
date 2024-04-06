class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        s=sum(nums[:k])
        an=s
        for i in range(k,n):
            s+=nums[i]
            s-=nums[i-k]
            an=max(an,s)
        return an/k