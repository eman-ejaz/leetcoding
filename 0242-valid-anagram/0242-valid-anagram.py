class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq1 = {}
        freq2 = {}

        
        for ch in s:
            freq1[ch] = freq1.get(ch, 0) + 1

        for ch in t:
            freq2[ch] = freq2.get(ch, 0) + 1

        for i in range(len(s)):
            ch = s[i]

            if ((ch in freq1 and ch not in freq2) or (ch in freq2 and ch not in freq1) or freq1[ch] != freq2[ch]):
                return False

        
        return True
        






























        return Counter(s) == Counter(t)
        