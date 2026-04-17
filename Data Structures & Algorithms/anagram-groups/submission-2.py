class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)    # maps freq array to list of anagrams
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # counts now has the character frequencies of s
            res[tuple(count)].append(s)
        
        return list(res.values())