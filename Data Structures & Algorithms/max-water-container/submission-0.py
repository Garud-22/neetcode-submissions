class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                length = j - i
                height = min(heights[i], heights[j])
                area = length * height
                res = max(res, area)
        return res