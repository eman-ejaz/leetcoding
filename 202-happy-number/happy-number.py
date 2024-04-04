class Solution:
    def sum_of_squares(self, num):
        s = 0

        while num > 0:
            right_pos_num = num % 10
            s += math.pow(right_pos_num, 2)

            num //= 10

        return s

    def isHappy(self, num):
        slow_ptr, fast_ptr = num, num

        while True:
            slow_ptr = self.sum_of_squares(slow_ptr)

            fast_ptr = self.sum_of_squares(self.sum_of_squares(fast_ptr))

            if slow_ptr == 1 and fast_ptr == 1:
                return True

            if slow_ptr == fast_ptr:
                return False

            if fast_ptr == 1:
                return True
                