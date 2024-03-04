class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        l = 1

        for r in range(1, len(arr)):
            if arr[r] != arr[r -1]:
                arr[l] = arr[r]
                l += 1

        return l
        