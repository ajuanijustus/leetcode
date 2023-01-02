class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                op_stack.append(int(t))
            else:
                if t == "+":
                    ans = op_stack[-2] + op_stack[-1]
                    op_stack = op_stack[:-2]+[ans]
                elif t == "-":
                    ans = op_stack[-2] - op_stack[-1]
                    op_stack = op_stack[:-2]+[ans]
                elif t == "*":
                    ans = op_stack[-2] * op_stack[-1]
                    op_stack = op_stack[:-2]+[ans]
                elif t == "/":
                    ans = int(op_stack[-2] / op_stack[-1])
                    op_stack = op_stack[:-2]+[ans]
        return op_stack[-1]