# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head.next:
            return True
    
        def reverse(node):
            prev = None 

            while node:
                nxt = node.next

                node.next = prev
                prev = node

                node = nxt

            return prev

        
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        
        reverse_head = reverse(slow.next)
        temp = head

        while reverse_head:
            if reverse_head.val is not temp.val:
                return False
            
            reverse_head = reverse_head.next
            temp = temp.next

        return True

            

        




        