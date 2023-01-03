class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {')': '(', ']': '[', '}': '{'}
        for p in s:
            if p in ['(', '[', '{']:
                stack.append(p)
            else:
                if stack and stack[-1] == p_map[p]:
                    stack.pop()
                else:
                    return False
        
        return True if len(stack)==0 else False