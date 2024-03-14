class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        if len(arr) < 3:
            return [1, 2]
        left, right = 0, len(arr) - 1

        while left < right:
            s = arr[left] + arr[right]

            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else: 
                right -= 1
        
        return [-1, -1]