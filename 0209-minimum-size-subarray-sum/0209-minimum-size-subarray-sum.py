class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowStart = 0

        res = float('inf')
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

            while sum >= target:
                res = min(res, i - windowStart + 1)

                sum -= nums[windowStart]
                windowStart += 1

        if res == float('inf'):
            return 0
        else:
            return res
        