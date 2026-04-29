class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer approach (time and space efficient)
        res = 0
        if len(height) == 1:
            return res
        
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                water = max_left - height[l]
                res += water
            else:    # max_right <= max_left
                r -= 1
                max_right = max(max_right, height[r])
                water = max_right - height[r]
                res += water
        return res