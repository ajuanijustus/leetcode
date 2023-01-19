class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win_len = len(s1)
        check = Counter(s1)
        for l in range(len(s2)-win_len+1):
            r = l + win_len
            if Counter(s2[l:r]) == check:
                return True
        return False