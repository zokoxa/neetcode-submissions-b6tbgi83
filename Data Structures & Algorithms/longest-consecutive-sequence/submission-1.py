class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in s:
            temp = 1
            if (num-1) not in s:
                counter = 1
                while num+counter in s:
                    temp += 1
                    counter += 1
            res = max(res,temp)

        return res


        
