class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        
        def backtrack(current_string):
            if len(result) == k:
                return
            
            if len(current_string) == n:
                result.append(current_string)
                return
            
            for char in ['a', 'b', 'c']:
                if not current_string or current_string[-1] != char:
                    backtrack(current_string + char)
        
        backtrack("")
        
        if len(result) < k:
            return ""
        return result[-1]