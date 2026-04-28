class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = set()
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            # nums[j] + nums[k] == -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr = nums[j] + nums[k]
                target = (-1) * nums[i]
                if curr < target:
                    j += 1
                elif curr > target:
                    k -= 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet.sort()
                    triplet = tuple(triplet)
                    if triplet not in triplets:
                        triplets.add(tuple(triplet))
                    j += 1
                    k  = len(nums) - 1
        res = []
        for triplet in triplets:
            res.append(list(triplet))
        return res