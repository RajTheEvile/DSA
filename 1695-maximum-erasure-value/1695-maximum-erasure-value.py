class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        ans=0
        sum=0
        i=0
        for j in range(len(nums)):
            while nums[j] in s:
                s.remove(nums[i])
                sum-=nums[i]
                i+=1
            s.add(nums[j])
            sum+=nums[j]
            ans=max(ans,sum)
        return ans
                
        