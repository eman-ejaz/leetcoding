class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums_freq = {}

        # for num in nums:
        #     if num not in nums_freq:
        #         nums_freq[num] = 0

        #     nums_freq[num] += 1

        #     if nums_freq[num] > 1:
        #         return True

        # return False


        # sort technique

        nums.sort()


        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1]):
                return True

        return False


            