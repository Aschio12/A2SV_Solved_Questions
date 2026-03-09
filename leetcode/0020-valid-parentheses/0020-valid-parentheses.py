class Solution:
    def isValid(self, s: str) -> bool:

        close={")":"(","]":'[',"}":"{"}

        stack=[]

        for ch in s:
            if ch in close:
                if stack:
                    if close[ch]==stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

            else:
                stack.append(ch)
        return not stack
