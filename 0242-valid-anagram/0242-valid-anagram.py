class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in seen_s.keys():
                seen_s[s[i]] += 1
            else:
                seen_s[s[i]] = 1
                
            if t[i] in seen_t.keys():
                seen_t[t[i]] += 1
            else:
                seen_t[t[i]] = 1
        print(seen_t)
        print(seen_s)
        
        return seen_s==seen_t