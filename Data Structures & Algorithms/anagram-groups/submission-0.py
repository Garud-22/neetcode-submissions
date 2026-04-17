class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            
            if len(s) == 0:
                return True

            A = [0] * 26

            for i in range(len(s)):
                letter_s = s[i]
                letter_t = t[i]

                A[ord(letter_s) - ord('a')] += 1
                A[ord(letter_t) - ord('a')] -= 1
            
            for num in A:
                if num != 0:
                    return False
            return True
        
        already_added = set()
        list_of_lists = []

        for i in range(len(strs)):
            if i in already_added:
                continue
            
            anagram_list = [strs[i]]

            for j in range(i+1, len(strs)):
                if j in already_added:
                    continue    # which for loop will this effect?
                
                if isAnagram(strs[i], strs[j]):
                    anagram_list.append(strs[j])
                    already_added.add(j)

            list_of_lists.append(anagram_list)
        
        return list_of_lists