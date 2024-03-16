class Solution:
    def threeSumClosest(self, arr: List[int], target_sum: int) -> int:
        # arr.sort()
        # result = float('inf')
        # for i in range(len(arr) - 2):
        #     left, right = i + 1, len(arr) - 1

        #     while left < right:
        #         target_diff = target_sum - arr[i] - arr[left] - arr[right]

        #         if target_diff == 0:
        #             return arr[i] + arr[left] + arr[right]

        #         if abs(target_diff) < abs(result):
        #             result = target_diff

        #         if target_diff > 0:
        #             left += 1
        #         else:
        #             right -= 1

        # return target_sum - result
            

        arr.sort()
        result = float('inf')

        for i in range(len(arr) - 2):
            left, right = i + 1, len(arr) - 1

            while left < right:
                target_diff = target_sum - arr[i] - arr[left] - arr[right]

                if target_diff == 0:
                    return target_sum - target_diff

                if abs(target_diff) < abs(result):
                    result = target_diff

                if target_diff > 0:
                    left += 1
                else:
                    right -= 1

        return target_sum - result