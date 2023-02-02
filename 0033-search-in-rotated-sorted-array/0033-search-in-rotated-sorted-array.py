class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while(l<=r):
            i = (l+r)//2
            if nums[i] == target:
                return i
            elif nums[i] >= nums[l]:
                if target > nums[i] or target < nums[l]:
                    l = i + 1
                else:
                    r = i - 1
            else:
                if target < nums[i] or target > nums[r]:
                    r = i - 1
                else:
                    l = i + 1
        return -1    