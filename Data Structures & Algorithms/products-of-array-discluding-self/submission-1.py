class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        for i in nums:
            if i == 0: 
                zeros += 1
            else: prod *= i

        if zeros == 0:
            for i in range(len(nums)):
                nums[i] = round(prod / nums[i])
            return nums

        elif zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0: nums[i] = prod
                else: nums[i] = 0
            return nums
        
        return [0]*len(nums)