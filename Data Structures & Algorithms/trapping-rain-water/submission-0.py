class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        n = len(height)
        max_left_list = [0] * n
        max_left = 0

        for i in range(n):
            if i == 0:
                max_left_list[i] = 0
            else:
                if height[i-1] > max_left:
                    max_left = height[i-1]
                max_left_list[i] = max_left
        
        max_right_list = [0] * n
        max_right = 0
        for i in range(n-1, -1, -1):
            if i == n-1:
                max_right_list[i] = 0
            else:
                if height[i+1] > max_right:
                    max_right = height[i+1]
                max_right_list[i] = max_right
        
        min_left_right = [0] * n
        for i in range(n):
            min_left_right[i] = min(max_left_list[i], max_right_list[i])
        
        for i in range(n):
            water_amount = 0
            if min_left_right[i] - height[i] > 0:
                water_amount = min_left_right[i] - height[i]
            res += water_amount
        return res