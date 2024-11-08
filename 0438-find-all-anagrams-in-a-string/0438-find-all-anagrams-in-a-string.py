class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = Counter(p)
        ws, matched = 0, 0

        res = []

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] -= 1

                if freq[s[i]] == 0:
                    matched += 1

                if matched == len(freq):
                    res.append(ws)

            if i - ws >= len(p) - 1:
                if s[ws] in freq:
                    if freq[s[ws]] == 0:
                        matched -= 1
                    
                    freq[s[ws]] += 1
                
                ws += 1

        return res
        