class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cf = [0] * 26

        ws = 0
        max_length = float('-inf')
        max_char = 0

        for i in range(len(s)):
            cf[ord(s[i]) - ord('A')] += 1

            max_char = max(cf)

            if (i - ws + 1) - max_char <= k:
                max_length = max(max_length, i - ws + 1)


            while (i - ws + 1) - max_char > k:
                cf[ord(s[ws]) - ord('A')] -= 1
                ws += 1

                max_char = max(cf)

        return max_length




            

        