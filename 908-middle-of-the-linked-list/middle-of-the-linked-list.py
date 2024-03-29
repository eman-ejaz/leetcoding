# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head
        counter = 0

        while temp:
            temp = temp.next
            counter += 1
        
        temp = head
        i = 0
        while True:
            if i == math.floor(counter/2):
                return temp
            
            temp = temp.next
            i += 1
        
        return None


        # temp = head

        # slow, fast = temp, temp

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # return slow
        