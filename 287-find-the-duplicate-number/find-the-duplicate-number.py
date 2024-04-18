class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return num
            
            nums_set.add(num)
        return -1
        

        i = 0

        while i < len(nums):
            j = nums[i] - 1

            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(nums):
            if nums[i] != i + 1:
                return nums[i]