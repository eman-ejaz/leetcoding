class Solution:
    def sortColors(self, arr: List[int]) -> None:
        # if len(arr) < 2:
        #     return arr
        # """
        # Do not return anything, modify nums in-place instead.
        # """
        # left, right = 0, len(arr) - 1

        # i = 0   

        # while i <= right:
        #     if arr[i] == 0:
        #         arr[left], arr[i] = arr[i], arr[left]
        #         left += 1
        #     elif arr[i] == 2:
        #         arr[right], arr[i] = arr[i], arr[right]
        #         right -= 1
        #         i -= 1
        
        #     i += 1
        # return arr

        left, right = 0, len(arr) - 1
        i = 0
        while i <= right:
            if arr[i] == 0:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
                i += 1
            elif arr[i] == 2:
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
            else:
                i += 1

        return arr
        