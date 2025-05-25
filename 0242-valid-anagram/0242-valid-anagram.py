class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}

        for ch in s:
            m1[ch] = 1 + m1.get(ch, 0)

        for ch in t:
            m2[ch] = 1 + m2.get(ch, 0)

        if len(m1) != len(m2):
            return False
        
        for ch in m1:
            if ch not in m2:
                return False
            if m2.get(ch, 0) != m1[ch]:
                return False
        
        return True









































        if len(s) != len(t):
            return False

        freq1 = {}
        freq2 = {}

        
        for ch in s:
            freq1[ch] = freq1.get(ch, 0) + 1

        for ch in t:
            freq2[ch] = freq2.get(ch, 0) + 1


        for ch in freq1:
            if freq1[ch] != freq2.get(ch, 0):
                return False

        # for i in range(len(s)):
        #     ch = s[i]

        #     if ((ch in freq1 and ch not in freq2) or (ch in freq2 and ch not in freq1) or freq1[ch] != freq2[ch]):
        #         return False

        
        return True
        






























        return Counter(s) == Counter(t)
        