class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             return [i, j]

        # return [-1, -1]

        # hashmap

        hash_map = {}


        for i in range(len(nums)):
            if (target - nums[i] in hash_map):
                return [i, hash_map[target - nums[i]]]
            
            hash_map[nums[i]] = i

        return [-1, -1]


        