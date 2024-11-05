class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        length = 0

        ws = 0
        zeros = 0

        for i in range(len(arr)):
            if arr[i] == 0:
                zeros += 1

            while zeros > k:
                if arr[ws] == 0:
                    zeros -= 1

                ws += 1

            length = max(length, i - ws + 1)

        return length
        
        
        
        
        
        
        
        
        
        
        
        
        # maxL = 0
        # ws = 0
        # zeros = 0
        # ones = 0

        # for i in range(len(arr)):
        #     if arr[i] == 1:
        #         ones += 1

        #     while (i - ws + 1) - ones > k:
        #         if arr[ws] == 1:
        #             ones -= 1

        #         ws += 1

        #     maxL = max(maxL, i - ws + 1) 
        
        # return maxL
            