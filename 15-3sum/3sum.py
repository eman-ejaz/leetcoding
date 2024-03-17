class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        target = 0
        # result = []

        # nums.sort()

        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue

        #     target = -nums[i]
        #     left, right = i + 1, len(nums) - 1

        #     while left < right:
        #         s = nums[left] + nums[right]

        #         if s == target:
        #             result.append([nums[i], nums[left], nums[right]])
        #             left += 1
        #             right -= 1

        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1
        #             while right > left and nums[right] == nums[right + 1]:
        #                 right -= 1

        #         elif s < target:
        #             left += 1
        #         else:
        #             right -= 1

        # return result


        result = []
        arr.sort()

        for i in range(len(arr) - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue;
            left, right = i + 1, len(arr) - 1

            while left < right:
                s = arr[i] + arr[left] + arr[right]

                if s == target:
                    result.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1

                    while right > left and arr[right] == arr[right + 1]:
                        right -= 1


                elif s > target:
                    right -= 1
                elif s < target:
                    left += 1
        return result

        