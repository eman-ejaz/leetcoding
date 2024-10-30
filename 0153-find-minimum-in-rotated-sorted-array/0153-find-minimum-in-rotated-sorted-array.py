class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        min_num = float('inf')

        while l <= r:
            m = (l + r)//2

            min_num = min(min_num, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return min_num






































        # l, r = 0, len(nums) - 1

        # min_n = float('inf')
        # while l <= r:
        #     m = (l + r) // 2

        #     min_n = min(min_n, nums[m])

        #     print(nums[m], nums[r])

        #     if nums[m] < nums[r]:
        #         r = m - 1
        #     else:
        #         l = m + 1
        
        # return min_n































        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            mid = (r + l) // 2

            if (nums[mid] > nums[mid + 1]):
                return nums[mid + 1]
            
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            else:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        
            