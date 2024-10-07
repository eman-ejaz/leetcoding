class Solution:
    def maxArea(self, height: List[int]) -> int:

        # brute force

        # max_a = 0

        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         area = (j - i) * (min(height[j], height[i]))
        #         max_a = max(max_a, area)

        # return max_a


        # linear time solution
        l, r = 0, len(height) - 1

        max_area = float('-inf')

        while l < r:
            area = (r - l) * (min(height[l], height[r]))
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
        