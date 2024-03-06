class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        result = [0 for _ in range(len(arr))]

        left, right = 0, len(arr) - 1
        index = len(result) - 1

        while left <= right:
            if math.pow(arr[left], 2) < math.pow(arr[right], 2):
                result[index] = int(math.pow(arr[right], 2))
                index -= 1
                right -= 1
            else:
                result[index] = int(math.pow(arr[left], 2))
                index -= 1
                left += 1
        
        return result
        