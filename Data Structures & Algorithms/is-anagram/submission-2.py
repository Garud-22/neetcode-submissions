class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26

        for i in range(len(s)):
            s_index = ord(s[i]) - ord("a")
            counts[s_index] += 1

            t_index = ord(t[i]) - ord("a")
            counts[t_index] -= 1
        
        for num in counts:
            if num != 0:
                return False
        return True