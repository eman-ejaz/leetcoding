class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        result = []

        for i in range(len(arr) - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, len(arr) - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                left, right = j + 1, len(arr) - 1

                while left < right:
                    s = arr[i] + arr[j] + arr[left] + arr[right]

                    if s == target:
                        result.append([arr[i], arr[j], arr[left], arr[right]])
                        left += 1
                        right -= 1

                        while right > left and arr[right] == arr[right + 1]:
                            right -= 1

                    elif target > s:
                        left += 1
                    else:
                        right -= 1

        return result