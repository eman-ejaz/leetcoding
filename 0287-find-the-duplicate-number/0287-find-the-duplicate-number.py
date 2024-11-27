class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1

            if nums[correct_index] != correct_index + 1:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            elif nums[correct_index] == correct_index + 1:
                i += 1

        print('nums', nums)
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]

        return 0

        # nums_set = set()

        # for num in nums:
        #     if num in nums_set:
        #         return num
        #     else:
        #         nums_set.add(num)
        