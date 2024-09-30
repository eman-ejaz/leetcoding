class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_freq = {}

        for num in nums:
            if num not in nums_freq:
                nums_freq[num] = 0

            nums_freq[num] += 1

            if nums_freq[num] > 1:
                return True

        return False
            