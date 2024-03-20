class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        # l = 1

        # for r in range(1, len(arr)):
        #     if arr[r] != arr[r -1]:
        #         arr[l] = arr[r]
        #         l += 1

        # return l

        # next_unique = 1

        # for i in range(1, len(arr)):
        #     if arr[i] != arr[i - 1]:
        #         arr[next_unique] = arr[i]
        #         next_unique += 1

        # return next_unique
        

        a, b = 0, 1


        while b < len(arr):
            if arr[b] != arr[b -1]:
                arr[a + 1] = arr[b]
                a += 1
            
            b += 1

        return a + 1

