class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        type_a=0
        type_b=0
        result_a=0
        result_b=0
        for i in colors:
            if i=="A":
                type_a+=1
                type_b=0
                if type_a>=3:
                    result_a+=1
            if i=="B":
                type_a=0
                type_b+=1
                if type_b>=3:
                    result_b+=1
        if result_a>result_b:
            return True
        else:
            return False