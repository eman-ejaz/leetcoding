class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for arr in matrix:

            if arr[0] <= target <= arr[-1]:

                l = 0
                r = len(arr) - 1

                while l <= r:
                    mid = l + (r - l)//2

                    if target > arr[mid]:
                        l = mid + 1
                    elif target < arr[mid]:
                        r = mid - 1
                    else:
                        return True
        
        return False



        