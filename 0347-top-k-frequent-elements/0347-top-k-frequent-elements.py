class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1:
            return [nums[0]]

        nums_freq = Counter(nums)

        sorted_nums_freq = sorted(nums_freq, key=lambda x: nums_freq[x], reverse=True)

        print(sorted_nums_freq)


        
        return sorted_nums_freq[:k]




