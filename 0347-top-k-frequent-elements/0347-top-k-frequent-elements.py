class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # if len(nums) == 1:
        #     return [nums[0]]

        # nums_freq = Counter(nums)

        # sorted_nums_freq = sorted(nums_freq, key=lambda x: nums_freq[x], reverse=True)

        # print(sorted_nums_freq)


        
        # return sorted_nums_freq[:k]

             # bucket sort

        arr = [[] for i in range(len(nums) + 1)]

        nums_freq = Counter(nums)


        for num, freq in nums_freq.items():
            arr[freq].append(num)

        print('arr', arr)

        result = []
    
        for i in range(len(arr) - 1, -1 , -1):
            if len(arr[i]) != 0:
                for num in arr[i]:
                    if len(result) < k:
                        print(i, 'i')
                        print(num, 'num')
                        result.append(num)


        return result





