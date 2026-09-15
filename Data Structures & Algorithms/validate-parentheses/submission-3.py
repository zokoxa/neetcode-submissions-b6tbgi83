class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        try:
            for i in range(0,len(s)):
                if s[i] in '[{(':
                    stk.append(s[i])
                else:
                    if s[i] == ']' and stk.pop() == '[':
                        continue
                    if s[i] == '}' and stk.pop() == '{':
                        continue 
                    if s[i] == ')' and stk.pop() == '(':
                        continue
                    return False
        except Exception:
            return False
        if len(stk) != 0: return False 
        return True
