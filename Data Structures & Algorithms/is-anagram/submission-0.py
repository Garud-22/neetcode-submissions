class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        
        t_dict = {}
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        
        letters_s = list(s_dict.keys())
        letters_s.sort()
        letters_t = list(t_dict.keys())
        letters_t.sort()

        if not letters_s == letters_t:
            return False
        
        for letter in letters_s:
            if not s_dict[letter] == t_dict[letter]:
                return False
        return True