class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}    # num -> freq

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        counts_list = []
        for num, freq in counts.items():
            counts_list.append([num, freq])
        
        # counts_list is a list of lists
        counts_list.sort(key=lambda x: x[1])
        
        counts_list.reverse()

        ans = []
        for i in range(k):
            ans.append(counts_list[i][0])
        return ans