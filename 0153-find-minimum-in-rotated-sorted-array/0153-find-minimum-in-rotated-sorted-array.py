class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = None

        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] > nums[i + 1]:
                pivot = i
                break

        return nums[0] if pivot is None else nums[pivot + 1]
            