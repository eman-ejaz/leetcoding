class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # mlogn
        # for arr in matrix:

        #     if arr[0] <= target <= arr[-1]:

        #         l = 0
        #         r = len(arr) - 1

        #         while l <= r:
        #             mid = l + (r - l)//2

        #             if target > arr[mid]:
        #                 l = mid + 1
        #             elif target < arr[mid]:
        #                 r = mid - 1
        #             else:
        #                 return True
        
        # return False

        # log(m * n)
        p1, p2 = 0, len(matrix) - 1

        def search_target(nums):
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        while p1 <= p2:
            mid = p1 + (p2 - p1) // 2
            mid_arr = matrix[mid]

            if mid_arr[0] <= target <= mid_arr[-1]:
                return search_target(mid_arr)
            elif mid_arr[0] > target:
                p2 = mid - 1
            else:
                p1 = mid + 1

        return False



            