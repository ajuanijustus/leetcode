class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while(l<=r):
            k = (l+r)//2
            t = 0
            for p in piles:
                t += math.ceil(p/k)
                if t > h:
                    break
            if t > h:
                l = k + 1
            else:
                r = k - 1
                ans = min(ans, k)
        return ans