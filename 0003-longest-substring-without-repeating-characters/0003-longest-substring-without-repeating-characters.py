class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force

        # if len(s) == 0:
        #     return 0

        # max_len = float('-inf')
        # freq = {}

        # for i in range(len(s)):
        #     freq[s[i]] = 1 + freq.get(s[i], 0)
        #     for j in range(i + 1, len(s)):
        #         if s[j] in freq:
        #             break
        #         else:
        #             freq[s[j]] = 1 + freq.get(s[j], 0)
        #     max_len = max(max_len, len(freq))
        #     freq = {}
            

        # return max_len


        if len(s) == 0:
            return 0
        freq = {}

        ws = 0
        max_len = float('-inf')

        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)

            while freq[s[i]] > 1:
                freq[s[ws]] -= 1
                ws += 1

            max_len = max(max_len, i - ws + 1)
            
        return max_len



        