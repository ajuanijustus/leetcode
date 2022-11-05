class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {x: 0 for x in set(nums)}
        for n in nums:
            counter[n] += 1
        for k, v in counter.items():
            if v == 1:
                return k