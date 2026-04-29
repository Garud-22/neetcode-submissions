class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force
        res = 0
        if len(height) == 1:
            return res
        
        for i in range(len(height)):
            left_max = 0
            right_max = 0

            for j in range(i):
                if height[j] > left_max:
                    left_max = height[j]
            
            for j in range(i+1, len(height)):
                if height[j] > right_max:
                    right_max = height[j]
            
            min_max = min(left_max, right_max)
            if min_max - height[i] > 0:
                res += min_max - height[i]
        
        return res