class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = nums[0]
        l, r = 1, len(nums)-1
        while(l<=r):
            i = l + ((r-l)//2)
            if nums[i] > m:
                l = i + 1
            else:
                m = nums[i]
                r = i - 1
        return m