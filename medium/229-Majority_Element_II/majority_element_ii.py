class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nd = {}
        size = int(len(nums) / 3)
        result = []

        for i in nums:
            if i in nd:
                nd[i] += 1
            else:
                nd[i] = 1

        for i in nd:
            if nd[i] > size:
                result.append(i)
        del nd,size
        return result
