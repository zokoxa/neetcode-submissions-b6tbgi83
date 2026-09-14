class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in s:
            if (num-1) not in s:
                counter = 0
                while num+counter in s:
                    counter += 1
                res = max(counter,res)

        return res


        
