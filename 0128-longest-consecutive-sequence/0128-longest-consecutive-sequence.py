class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # numSet = set(nums)

        # i = 0
        # longest_sequence = 0
        # for num in nums:
        #     if num - 1 not in numSet:
        #         counter = 1
        #         while (num + counter) in numSet:
        #             counter += 1

        #         longest_sequence = max(longest_sequence, counter)


        # return longest_sequence




        numSet = set(nums)
        result = 0
        for num in nums:
            if num - 1 not in numSet:
                seq_len = 1
                while num + seq_len in numSet:
                    seq_len += 1
                result = max(result, seq_len)

        return result






























