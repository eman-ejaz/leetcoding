class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True

    #     return False


    def containsDuplicate(self, nums):
        # nums_freq = {}

        # for i in range(len(nums)):
        #     if nums[i] not in nums_freq:
        #         nums_freq[nums[i]] = 0

        #     nums_freq[nums[i]] = nums_freq[nums[i]] + 1

        #     if nums_freq[nums[i]] > 1:
        #         return True

        # return False

        s = set(nums)

        return len(s) != len(nums)



        