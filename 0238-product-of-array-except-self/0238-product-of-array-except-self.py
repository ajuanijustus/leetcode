class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = list(accumulate(nums, mul))
        suf = list(accumulate(nums[::-1], mul))[::-1]
        
        return [(pre[i-1] if i else 1) * (suf[i+1] if i+1<(len(nums)) else 1) for i in range(len(nums))]