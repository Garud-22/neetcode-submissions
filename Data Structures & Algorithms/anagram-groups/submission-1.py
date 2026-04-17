class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using sorting
        res = defaultdict(list)    # maps the sorted (canonical) form of each string to the list of strings which have that canonical form

        for s in strs:
            sorted_s = "".join(sorted(s))
            res[sorted_s].append(s)
        
        return list(res.values())