class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        result = []
        counter = 1
        while p1 < len(word1) and p2 < len(word2):
            if counter % 2 == 0:
                result.append(word2[p2])
                p2 += 1
            else:
                result.append(word1[p1])
                p1 += 1
            
            counter += 1

        if p1 != len(word1):
            while p1 < len(word1): 
                result.append(word1[p1])
                p1 += 1
        
        if p2 != len(word2):
            while p2 < len(word2): 
                result.append(word2[p2])
                p2 += 1

        return ''.join(result)

        