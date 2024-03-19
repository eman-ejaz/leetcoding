class Solution:
    def maxArea(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return -1
        
        result_area = float('-inf')

        right = len(arr) - 1
        left = 0

        while left < right:
            temp_area = (right - left) * min(arr[left], arr[right])
            result_area = max(result_area, temp_area)

            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return result_area

        