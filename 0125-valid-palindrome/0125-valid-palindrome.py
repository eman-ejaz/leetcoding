class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string = ''

        # for char in s:
        #     if char.isalnum():
        #         string += char.lower()

        # l, r = 0, len(string) - 1

        # while l < r:
        #     if string[l] != string[r]:
        #         return False

        #     l += 1
        #     r -= 1

        # return True



        def is_alpha_num(s: str):
            return (ord('0') <= ord(s) <= ord('9') or
                    ord('A') <= ord(s) <= ord('Z') or
                    ord('a') <= ord(s) <= ord('z'))


        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not is_alpha_num(s[l]):
                l += 1

            while r > l and not is_alpha_num(s[r]):
                r -= 1

              

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


            