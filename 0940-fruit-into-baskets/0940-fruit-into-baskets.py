class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0

        ws = 0
        fmap = {}

        for i in range(len(fruits)):
            fmap[fruits[i]] = fmap.get(fruits[i], 0) + 1

            if len(fmap) <= 2:
                res = max(res, i - ws + 1)

            while len(fmap) > 2:
                fmap[fruits[ws]] = fmap.get(fruits[ws]) - 1

                if fmap[fruits[ws]] == 0:
                    del fmap[fruits[ws]]

                ws += 1

        return res


            