class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            c=0
            for j in range(nums2.index(i),len(nums2)):
                if nums2[j]>i:
                    res.append(nums2[j])
                    c+=1
                    break
            if c==0:
                res.append(-1)

        return res
        