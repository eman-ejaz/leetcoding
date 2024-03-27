class Solution:
    def sortColors(self, arr: List[int]) -> None:
        # result = []
        # nums_freq = {}

        # for num in arr:
        #     nums_freq[num] = nums_freq.get(num, 0) + 1

        # for i in range(len(arr)):
        #     if 0 in nums_freq and nums_freq[0] > 0:
        #         arr[i] = 0
        #         nums_freq[0] -= 1
        #     elif 1 in nums_freq and nums_freq[1] > 0:
        #         arr[i] = 1
        #         nums_freq[1] -= 1
        #     else:
        #         arr[i] = 2

        # print(arr)

        # return result


        l, r = 0, len(arr) - 1

        i = 0

        while i <= r:
            if arr[i] == 0:
                arr[i], arr[l] = arr[l], arr[i]
                i += 1
                l += 1
            elif arr[i] == 2:
                arr[i], arr[r] = arr[r], arr[i]
                r -= 1
            else:
                i += 1
        
        return arr


























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

        # left, right = 0, len(arr) - 1
        # i = 0
        # while i <= right:
        #     if arr[i] == 0:
        #         arr[i], arr[left] = arr[left], arr[i]
        #         left += 1
        #         i += 1
        #     elif arr[i] == 2:
        #         arr[i], arr[right] = arr[right], arr[i]
        #         right -= 1
        #     else:
        #         i += 1

        # return arr
        