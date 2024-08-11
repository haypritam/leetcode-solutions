class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        large=0
        current=0
        for i in gain:
            current+=i
            if current>large:
                large=current
        return large
