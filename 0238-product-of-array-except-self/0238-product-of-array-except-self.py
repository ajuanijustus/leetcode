import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        if 0 in nums:
            for i in range(len(nums)):
                prod_list = nums[0:i]+nums[i+1:]
                ans.append(math.prod(prod_list))
            return ans
        else:
            prod = math.prod(nums)
            return [int(prod/num) for num in nums]