class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        
        def check(st):
            stack = []
            for i in range(len(st)):  # Fixed typo: removed extra ')'
                if st[i] == "(":
                    stack.append(st[i])
                elif st[i] == ")":    # FIX 1: Explicitly check for ")", ignore letters like 'a'
                    # FIX 2: Only pop if there is a matching "(" to pop
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(st[i])
            return len(stack)



        ma_remove=check(s)
        ans=[]
        visited=set()
        def rec(ss,m_remove):
            if ss in visited:
                return
            visited.add(ss)
            if m_remove<0:
                return
            if m_remove==0:
                
                if check(ss)==0:
                    ans.append(ss)
                return
            for i in range(len(ss)):
                if ss[i] in "()":
                    current=ss[:i]+ss[i+1:]
                    rec(current,m_remove-1)
                
        rec(s,ma_remove)
        return ans