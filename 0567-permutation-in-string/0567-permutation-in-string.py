class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)

        print(freq)

        matched = 0

        ws = 0

        for i in range(len(s2)):
            if s2[i] in freq:
                freq[s2[i]] -= 1

                if freq[s2[i]] == 0:
                    matched += 1

                
                if matched == len(freq):
                    return True

            if i - ws == len(s1) - 1:
                if s2[ws] in freq:
                    if freq[s2[ws]] == 0:
                        matched -= 1
                    freq[s2[ws]] += 1

                ws += 1

        return False
        