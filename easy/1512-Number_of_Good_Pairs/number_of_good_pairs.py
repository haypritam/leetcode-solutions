class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dictn={}
        result=0
        for i in nums:
            try:
                dictn[i]+=1
            except:
                dictn[i]=1
        for i in dictn:
            if dictn[i]>=2:
                result+=int((dictn[i]*(dictn[i]-1))/2)
        return result