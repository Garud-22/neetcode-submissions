class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                height = heights[l]
                length = r - l
                l += 1
            else:
                height = heights[r]
                length = r - l
                r -= 1
            area = height * length
            res = max(res, area)
        return res