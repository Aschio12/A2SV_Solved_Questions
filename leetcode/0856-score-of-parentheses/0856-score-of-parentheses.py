class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack,ans=[],0
        for index,val in enumerate(s):
            if val=="(":
                stack.append(val)
            else:
                stack.pop()
                if s[index-1]=="(":
                    ans+=(2**len(stack))
        return ans