class Solution:
    def isPalindrome(self, s: str) -> bool:      
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char
        
        if len(clean_s) <= 1:
            return True
        
        clean_s = clean_s.lower()
        i = 0
        j = len(clean_s) - 1
        res = True
        while i < j:
            if clean_s[i] == clean_s[j]:
                i += 1
                j -= 1
                continue
            else:
                res = False
                break
        return res