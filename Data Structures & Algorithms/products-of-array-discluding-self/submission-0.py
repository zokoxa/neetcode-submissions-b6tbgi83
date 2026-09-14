class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c_nums = list()
        c_nums.append(1)
        temp = nums[0]
        for i in range(1, len(nums)):
            c_nums.append(temp)
            temp *= nums[i]

        temp = 1

        for i in range(len(nums)-1,-1,-1):
            c_nums[i] *= temp
            temp *= nums[i]
            
           
        return c_nums
