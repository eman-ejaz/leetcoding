class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        if (len(s_count) != len(t_count)):
            return False

        for char in s:
            if(s_count[char] != t_count[char]):
                return False

        return True
        