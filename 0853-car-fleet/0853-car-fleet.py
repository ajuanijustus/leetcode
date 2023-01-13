class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target-p)/s for p, s in sorted(zip(position, speed))][::-1]
        count = cur = 0
        for t in time:
            if t > cur:
                count += 1
                cur = t
        return count