class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b = 0, 0
        
        while b < len(nums):
            if nums[b] != 0:
                nums[a] = nums[b]
                a += 1
            
            b += 1
        
        while a < len(nums):
            nums[a] = 0
            a += 1
        
        return nums
        