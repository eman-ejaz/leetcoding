class Solution:
    def backspaceCompare(self, str1: str, str2: str) -> bool:
        p1, p2 = len(str1) - 1, len(str2) - 1

        while p1 >= 0 or p2 >= 0:
            updated_pointer1 = self.remove_bkspc(p1, str1)
            updated_pointer2 = self.remove_bkspc(p2, str2)

            if updated_pointer1 < 0 and updated_pointer2 < 0:
                return True

            if updated_pointer1 < 0 or updated_pointer2 < 0:
                return False

            if str1[updated_pointer1] != str2[updated_pointer2]:
                return False

            p1 = updated_pointer1 - 1
            p2 = updated_pointer2 - 1
        
        return True

    
    def remove_bkspc(self, index, s):
        bkspc_counter = 0

        while index >= 0:
            if s[index] == '#':
                bkspc_counter += 1
            elif bkspc_counter > 0:
                bkspc_counter -= 1
            else:
                break
            
            index -= 1
        
        return index




























    #     p1, p2 = len(str1) - 1, len(str2) - 1


    #     while p1 >= 0 or p2 >= 0:
    #         np1 = self.remove_bkspc(p1, str1)
    #         np2 = self.remove_bkspc(p2, str2)

    #         if np1 < 0 and np2 < 0:
    #             return True

    #         if np1 < 0 or np2 < 0:
    #             return False

    #         if str1[np1] != str2[np2]:
    #             return False

    #         p1 = np1 - 1
    #         p2 = np2 - 1
        
    #     return True

    # def remove_bkspc(self, index, s):
    #     num_bkspc = 0
    #     while index >= 0:
    #         if s[index] == '#':
    #             num_bkspc += 1
    #         elif num_bkspc > 0:
    #             num_bkspc -= 1
    #         else:
    #             break

    #         index -= 1
        
    #     return index





































    #     p1, p2 = len(str1) - 1, len(str2) - 1

    #     while p1 >= 0 or p2 >= 0:
    #         nP1 = self.index_after_removing_space(str1, p1)
    #         nP2 = self.index_after_removing_space(str2, p2)

    #         if nP1 < 0 and nP2 < 0:
    #             return True

    #         if nP1 < 0:
    #             return False

    #         if nP2 < 0:
    #             return False

    #         if str1[nP1] != str2[nP2]:
    #             return False

    #         p1, p2 = nP1 - 1, nP2 - 1

    #     return True


    # def index_after_removing_space(self, s: str, index):
    #     num_bkspc = 0
    #     while index >= 0:
    #         if s[index] == '#':
    #             num_bkspc += 1
    #         elif num_bkspc > 0:
    #             num_bkspc -= 1
    #         else:
    #             break
    #         index -= 1
    #     return index
        