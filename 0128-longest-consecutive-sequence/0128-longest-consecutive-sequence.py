class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        set_nums = set(nums)
        for num in nums:
            if num-1 not in set_nums:
                current_streak = 1
                while (num+1) in set_nums:
                    current_streak += 1
                    num += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak