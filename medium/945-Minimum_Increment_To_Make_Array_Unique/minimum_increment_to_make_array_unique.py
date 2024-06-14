class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        for i in range(0,len(nums)):
            if i>0:
                if nums[i]<=nums[i-1]:
                    incr=nums[i-1]-nums[i]+1
                    result+=incr
                    nums[i]+=incr
        return result
