class Solution:
    def trap(self, arr: List[int]) -> int:
        total_water = 0
        pre = [0] * len(arr)
        suf = [0] * len(arr)

        preMax = float('-inf')
        for i in range(len(arr)):
            preMax = max(arr[i], preMax)
            pre[i] = preMax

        sufMax = float('-inf')
        for i in range(len(arr) - 1, -1, -1):
            sufMax = max(arr[i], sufMax)
            suf[i] = sufMax


        for i in range(len(arr)):
            water = (min(pre[i], suf[i]) - arr[i])
            total_water += water if water > 0 else 0
        
        return total_water

        