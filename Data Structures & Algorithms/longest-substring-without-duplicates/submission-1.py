class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 1
        l = 0
        r = 1
        while r < len(s):
            hash_set = set()
            hash_set.add(s[l])
            while r < len(s) and s[r] not in hash_set:
                hash_set.add(s[r])
                r += 1
            max_length = max(max_length, len(hash_set))
            l += 1
            r = l + 1
        return max_length
