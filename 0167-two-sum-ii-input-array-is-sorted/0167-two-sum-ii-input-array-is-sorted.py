class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # left, right = 0, len(nums) -1

        # while left < right:
        #     sum = nums[left] + nums[right]

        #     if sum == target:
        #         return [left + 1, right + 1]
        #     elif sum < target:
        #         left += 1
        #     else:
        #         right -= 1

        # binary search solution
        
        for i, num in enumerate(nums):
            first_num = num

            left, right = i + 1, len(nums) - 1
            key = target - nums[i]
            while left <= right:
                mid = (right + left) // 2

                if nums[mid] == key:
                    return [i + 1, mid + 1]
                elif nums[mid] < key:
                    left = mid + 1
                else:
                    right = mid - 1

        