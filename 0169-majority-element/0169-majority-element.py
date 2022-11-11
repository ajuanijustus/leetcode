class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        majority = len(nums)/2
        for x in nums:
            if x in counter.keys():
                counter[x] += 1
                if (counter[x] > majority):
                    return x
            else:
                counter[x] = 1
        return nums[0]