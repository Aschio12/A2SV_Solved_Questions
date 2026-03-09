class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for op in logs:
            if op[0]!=".":
                stack.append(op)
            elif len(op)==3:
                if stack:
                    stack.pop()
                        
        return len(stack)