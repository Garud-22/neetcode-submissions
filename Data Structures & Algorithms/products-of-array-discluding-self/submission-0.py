class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zero = 0
        all_prod = 1
        single_zero_idx = None

        for i, num in enumerate(nums):
            if num == 0:
                num_zero += 1
                if num_zero == 2:
                    break
                single_zero_idx = i
                continue
            all_prod *= num

        else:
            if num_zero == 1:
                res = [0] * len(nums)
                res[single_zero_idx] = all_prod
                return res
            
            res = [0] * len(nums)
            for i, num in enumerate(nums):
                res[i] = int(all_prod/num)
            return res
        
        # if two or more zeros are in nums
        return [0] * len(nums)