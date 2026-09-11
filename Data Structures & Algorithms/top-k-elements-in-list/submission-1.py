class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        res = []
        for num in nums:
            if num in counts:
                counts[num] += 1 
            else:
                counts[num] = 1
        
        s_keys = sorted(counts, key=counts.get, reverse=True)[0:k:]



        return s_keys
