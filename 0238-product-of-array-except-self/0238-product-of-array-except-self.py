class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result_arr = [0] * len(nums)

        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue

        #         prod *= nums[j]

        #     result_arr[i] = prod

        # return result_arr


        # O(n)


        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)

        prod = nums[0]
        left_prod[0] = prod
        for i in range(1, len(nums)):
            prod *= nums[i]
            left_prod[i] = prod

        prod = nums[len(nums) - 1]
        right_prod[len(nums) - 1] = prod
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i]
            right_prod[i] = prod

        result = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = right_prod[i + 1]
            elif i == len(nums) - 1:
                result[i] = left_prod[i - 1]
            else:
                result[i] = left_prod[i - 1] * right_prod[i + 1]

        return result

        