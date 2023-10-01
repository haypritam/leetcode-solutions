class Solution:
    def reverseWords(self, s: str) -> str:
        result=""
        b=s.split()
        for i in b:
            result=result+i[::-1]+" "
        return result.rstrip()