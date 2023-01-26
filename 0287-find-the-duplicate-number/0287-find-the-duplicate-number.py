class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for n in nums:
            if n in seen.keys():
                return n
            else:
                seen[n] = 1