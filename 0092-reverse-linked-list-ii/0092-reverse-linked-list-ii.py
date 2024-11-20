# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        lp, ln = dummy, head

        for i in range(left - 1):
            lp = lp.next
            ln = ln.next

        prev = None
        curr = ln

        for i in range(right -  left + 1):
            nxt = curr.next

            curr.next = prev

            prev = curr
            curr = nxt

        lp.next = prev
        ln.next = curr

        return dummy.next


        
























        count = 1

        leftNode = head
        reverseHead = head
        while count < left:
            leftNode = reverseHead
            reverseHead = reverseHead.next
            count += 1

        
        rightNode = head
        count = 1
        while count < right + 1:
            rightNode = rightNode.next
            count += 1
        
        prev = None
        curr = reverseHead
        nxt = None

        while curr is not rightNode:
            nxt = curr.next

            curr.next = prev

            prev = curr
            curr = nxt

        leftNode.next = prev
        reverseHead.next = nxt

        print('test')

        return head
        