class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for i in range(1, max(piles) + 1):
        #     hours = 0
        #     for j in range(len(piles)):
        #         rate = math.ceil(piles[j] / i)
        #         print(i, rate)
        #         hours += rate

        #     if hours <= h:
        #         return i

        # return -1

        # optimized

        l, r = 1, max(piles)
        min_rate = float('inf')
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for i in range(len(piles)):
                rate = math.ceil(piles[i] / mid)
                hours += rate

                if hours > h:
                    break

            
            
            if hours > h:
                l = mid + 1
            else:
                min_rate = min(min_rate, mid)
                r = mid - 1

        return min_rate

































        # brute force, O(m * n)
        # if len(piles) > h:
        #     return -1

        # for speed in range(1, max(piles) + 1):
        #     hours_taken = 0

        #     for i in range(len(piles)):
        #         hours_taken += math.ceil(piles[i] / speed)

        #         if hours_taken > h:
        #             break

        #     if hours_taken == h:
        #         return speed
        

        #binary search solution O(log m * n)

        # l, r = 1, max(piles)
        # min_speed = float('inf')

        # while l <= r:
        #     mid = (r + l) // 2
        #     hours_taken = 0
        #     for i in range(len(piles)):
        #         hours_taken += math.ceil(piles[i] / mid)

        #         if hours_taken > h:
        #             break

        #     if hours_taken <= h:
        #         r = mid - 1
        #         min_speed = min(min_speed, mid)
        #     else:
        #         l = mid + 1

        return min_speed