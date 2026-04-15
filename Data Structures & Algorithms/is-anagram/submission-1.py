class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # in Python, dict is hash map
        count_s, count_t = {}, {}

        for i in range(len(s)):
            if s[i] not in count_s:
                count_s[s[i]] = 1
            else:
                count_s[s[i]] += 1
            
            if t[i] not in count_t:
                count_t[t[i]] = 1
            else:
                count_t[t[i]] += 1
        
        if count_s == count_t:
            return True
        else:
            return False