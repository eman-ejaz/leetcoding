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

        temp = head
        slow, fast = temp, temp

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        head_first_half = head
        head_second_half = self.reverse_list(slow)

        print(head_second_half.val)

        while head_first_half and head_second_half:
            nxt = head_first_half.next
            head_first_half.next = head_second_half
            head_first_half = nxt

            nxt = head_second_half.next
            head_second_half.next = head_first_half
            head_second_half = nxt

        if head_first_half is not None:
            head_first_half.next = None


    

    def reverse_list(self, head):
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        
        return prev
        