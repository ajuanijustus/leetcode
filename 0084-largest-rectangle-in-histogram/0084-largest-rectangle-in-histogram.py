class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[(i, h, start)]
        ar_max = max(heights)
        for i, h in enumerate(heights):
            start = i
            while(stack and stack[-1][1] > h):
                ar_max = max(ar_max,
                             # (h*(i-stack[-1][0]+1)),
                             stack[-1][1]*(i-stack[-1][0]))
                start = stack.pop()[0]
            stack.append((start, h))
        for i, h in stack:
            ar_max = max(ar_max, h * (len(heights)-i))
        return ar_max