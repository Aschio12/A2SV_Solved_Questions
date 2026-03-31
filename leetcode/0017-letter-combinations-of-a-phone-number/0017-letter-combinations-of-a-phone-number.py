class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {2: "abc",3: "def",4: "ghi",5: "jkl",6: "mno",7: "pqrs", 8: "tuv",9: "wxyz"}

        ans=[]

        def phone(possible,index):
            if len(possible)==len(digits):
                ans.append(possible)
                return
            for char in phone_map[int(digits[index])]:
                phone(possible+char,index+1)


        if digits:
            phone("",0)
        return ans