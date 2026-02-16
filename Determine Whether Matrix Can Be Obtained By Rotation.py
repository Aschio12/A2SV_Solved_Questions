class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat==target:
            return True

        def check(matt):
            cop=[num.copy() for num in matt]
            for i in range(len(matt)):
                for j in range(len(matt[0])):
                    cop[i]
                    [j]=matt[j][len(matt)-1-i]
            return cop
        
        

        current=mat
        for i in range(3):
            current=check(current)
            if check(current)==target:
                return True

        return False