class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten=0,0
        for i in range(len(bills)):
            if bills[i]==5:
                five+=5
            elif bills[i]==10:
                if five<5:
                    return False
                five-=5
                ten+=10
            else:
                if ten>=10 and five>=5:
                    five-=5
                    ten-=10
                elif five>=15:
                    five-=15
                else:
                    return False
                    
        return True
        