class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = [0] * len(nums)
        rprod = [0] * len(nums)
        res = [0] * len(nums)

        pre = 1
        post = 1

        for i in range(len(nums)):
            lprod[i] = pre

            pre *= nums[i]


        for i in range(len(nums) - 1, -1, -1):
            rprod[i] = post
            res[i] = lprod[i] * rprod[i]

            post *= nums[i]

        return res


        # result_arr = [0] * len(nums)

        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue

        #         prod *= nums[j]

        #     result_arr[i] = prod

        # return result_arr


        # O(n) time and space
        # left_prod = [1] * len(nums)
        # right_prod = [1] * len(nums)

        # prod = nums[0]
        # left_prod[0] = prod
        # for i in range(1, len(nums)):
        #     prod *= nums[i]
        #     left_prod[i] = prod

        # prod = nums[len(nums) - 1]
        # right_prod[len(nums) - 1] = prod
        # for i in range(len(nums) - 2, -1, -1):
        #     prod *= nums[i]
        #     right_prod[i] = prod

        # result = [0] * len(nums)
        # for i in range(len(nums)):
        #     if i == 0:
        #         result[i] = right_prod[i + 1]
        #     elif i == len(nums) - 1:
        #         result[i] = left_prod[i - 1]
        #     else:
        #         result[i] = left_prod[i - 1] * right_prod[i + 1]

        # return result

        # O(n) time, O(1) space


        # result = [1] * len(nums)

        # prefix = 1

        # for i in range(len(nums)):
        #     result[i] = prefix
        #     prefix *= nums[i]

        # postfix = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     result[i] *= postfix
        #     postfix *= nums[i]

        # return result

            

        







        result = [1] * len(nums)

        # traversal for prefix product

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # second traversal for postfix product
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result



            