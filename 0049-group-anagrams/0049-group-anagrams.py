from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for word in strs:
            ans[frozenset(Counter(word).items())].append(word)
            
        return ans.values()