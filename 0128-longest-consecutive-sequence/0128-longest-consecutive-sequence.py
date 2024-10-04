class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)

        i = 0
        longest_sequence = float('-inf')
        for num in nums:
            if num - 1 not in numSet:
                counter = 1
                while (num + counter) in numSet:
                    counter += 1

                longest_sequence = max(longest_sequence, counter)


        return longest_sequence