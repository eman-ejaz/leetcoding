# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None

        while slow:
            nxt = slow.next

            slow.next = prev
            prev = slow
            slow = nxt

        temp = head

        while prev.next and temp.next:
            nxt1 = temp.next
            nxt2 = prev.next

            temp.next = prev
            prev.next = nxt1

            temp = nxt1
            prev = nxt2


            

        