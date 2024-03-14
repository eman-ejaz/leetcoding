class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        # result = [0 for _ in range(len(arr))]

        # left, right = 0, len(arr) - 1
        # index = len(result) - 1

        # while left <= right:
        #     if math.pow(arr[left], 2) < math.pow(arr[right], 2):
        #         result[index] = int(math.pow(arr[right], 2))
        #         index -= 1
        #         right -= 1
        #     else:
        #         result[index] = int(math.pow(arr[left], 2))
        #         index -= 1
        #         left += 1
        
        # return result
        l, r = 0, len(arr) - 1

        result = [0] * len(arr)

        for i in range(len(result) - 1, -1, -1):
            if arr[l] ** 2 > arr[r] ** 2:
                result[i] = arr[l] ** 2
                l += 1
            else:
                result[i] = arr[r] ** 2
                r -= 1

        return result