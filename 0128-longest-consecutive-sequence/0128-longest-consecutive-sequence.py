class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)

        i = 0
        longest_sequence = float('-inf')
        while i < len(nums):
            if nums[i] - 1 not in numSet:
                counter = 1
                while (nums[i] + counter) in numSet:
                    counter += 1

                longest_sequence = max(longest_sequence, counter)

            i += 1

        return longest_sequence