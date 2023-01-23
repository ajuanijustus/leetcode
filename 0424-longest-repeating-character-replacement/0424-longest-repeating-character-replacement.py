class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        mx = 0
        l = 0
        for r in range(len(s)):
            c[s[r]] = 1 + c.get(s[r], 0)
            if r-l+1-max(c.values()) > k:
                c[s[l]] -= 1
                l += 1
            mx = max(mx, r-l+1)
        return mx