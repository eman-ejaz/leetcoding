class Solution:
    def maxArea(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        max_area = float('-inf')
        while l < r:
            area = (r - l) * min(arr[l], arr[r])
            max_area = max(max_area, area)

            if arr[l] < arr[r]:
                l += 1
            else:
                r -= 1

        return max_area


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(arr) < 2:
        #     return -1
        
        # result_area = float('-inf')

        # right = len(arr) - 1
        # left = 0

        # while left < right:
        #     temp_area = (right - left) * min(arr[left], arr[right])
        #     result_area = max(result_area, temp_area)

        #     if arr[left] < arr[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return result_area

        