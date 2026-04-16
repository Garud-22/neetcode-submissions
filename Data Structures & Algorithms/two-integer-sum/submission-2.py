class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using two-pointer approach
        A = []
        for i, n in enumerate(nums):
            A.append([n, i])

        # A is now a list of lists

        A.sort()

        i, j = 0, len(nums)-1    # initializing the two pointers

        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1    # increment the left pointer
            else:    # cur > target
                j -= 1    # decrement the right pointer

