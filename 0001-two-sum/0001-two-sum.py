class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target-num in seen.keys():
                return [i, seen[target-num]]
            else:
                seen[num] = i