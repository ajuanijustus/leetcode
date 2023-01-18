class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        c = 0
        temp_s = set()
        for i in range(len(s)):
            while s[i] in temp_s:
                temp_s.remove(s[c])
                c += 1
            temp_s.add(s[i])
            mx = max(mx, len(temp_s))
            print(temp_s)
        return mx