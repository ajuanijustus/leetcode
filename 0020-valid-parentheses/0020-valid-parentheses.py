class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in ['(', '[', '{']:
                stack.append(p)
            elif len(stack) > 0:
                if stack[-1] == '(' and p == ')':
                    stack.pop()
                elif stack[-1] == '[' and p ==']':
                    stack.pop()
                elif stack[-1] == '{' and p =='}':
                    stack.pop()
                else:
                    return False
            else:
                return False
        return True if len(stack)==0 else False