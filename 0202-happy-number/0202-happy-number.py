class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
            
        def cal_squares_sum(num):
            s = 0
            while num > 0:
                s += (num % 10) ** 2
                num //= 10

            return s

        f, s = n, n

        while True:
            s = cal_squares_sum(s)
            f = cal_squares_sum(cal_squares_sum(f))

            # if f == 1:
            #     return True

            if s == f:
                break

        return f == 1
            

        