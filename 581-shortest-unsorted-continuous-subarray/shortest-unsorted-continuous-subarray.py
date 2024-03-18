class Solution:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == len(arr) - 1:
            return 0

        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        sub_array_min, sub_array_max = float('inf'), float('-inf')

        for i in range(left, right + 1):
            sub_array_min = min(sub_array_min, arr[i])
            sub_array_max = max(sub_array_max, arr[i])

        while left > 0 and arr[left - 1] > sub_array_min:
            left -= 1

        while right < len(arr) - 1 and arr[right + 1] < sub_array_max:
            right += 1

        return right - left + 1
            