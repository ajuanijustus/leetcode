class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        for t in tokens:
            if t == "+":
                op_stack.append(op_stack.pop() + op_stack.pop())
            elif t == "-":
                op_stack.append(op_stack.pop(-2) - op_stack.pop(-1))
            elif t == "*":
                op_stack.append(op_stack.pop() * op_stack.pop())
            elif t == "/":
                op_stack.append(int(op_stack.pop(-2) / op_stack.pop(-1)))
            else:
                op_stack.append(int(t))
        return op_stack[-1]