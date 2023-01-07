class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        l = 0
        r = len(height)-1
        while l < r:
            vol = (r - l) * min(height[r], height[l])
            max_vol = max(max_vol, vol)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_vol
            