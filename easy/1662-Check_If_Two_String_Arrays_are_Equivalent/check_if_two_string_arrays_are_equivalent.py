class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        re1=""
        re2=""
        for i in word1:
            re1+=i
        for i in word2:
            re2+=i
        if  re1==re2:
            return True
        else:
            return False
