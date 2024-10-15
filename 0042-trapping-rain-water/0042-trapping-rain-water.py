class Solution:
    def trap(self, height: List[int]) -> int:
        # maxLeft = [0] * len(height)
        # maxRight = [0] * len(height)

        # maxLeft[0] = height[0]
        # maxRight[len(height) - 1] = height[len(height) - 1]

        # result = 0

        # for i in range(1, len(height)):
        #     if height[i] > maxLeft[i - 1]:
        #         maxLeft[i] = height[i]
        #     else:
        #         maxLeft[i] = maxLeft[i - 1]

        # for i in range(len(height) - 2, -1, -1):
        #     if height[i] > maxRight[i + 1]:
        #         maxRight[i] = height[i]
        #     else:
        #         maxRight[i] = maxRight[i + 1]

        # for i in range(len(height)):
        #     water_trapped = min(maxLeft[i], maxRight[i]) - height[i]

        #     result += water_trapped if water_trapped > 0 else 0

        # return result


        
        maxL = [0] * len(height)
        maxR = [0] * len(height)

        maxL[0] = height[0]
        maxR[-1] = height[-1]

        for i in range(1, len(height)):
            if height[i] > maxL[i - 1]:
                maxL[i] = height[i]
            else:
                maxL[i] = maxL[i - 1]

        for i in range(len(height) - 2, -1, -1):
            if height[i] > maxR[i + 1]:
                maxR[i] = height[i]
            else:
                maxR[i] = maxR[i + 1]

        
        result = 0

        for i in range(len(height)):
            potential = min(maxL[i], maxR[i])
            actual_water_stored = potential - height[i]

            result += max(actual_water_stored, 0)

        return result





























        