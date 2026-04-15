class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_unique = []
        for num in nums:
            if num not in nums_unique:
                nums_unique.append(num)
            else:
                return True
        return False
