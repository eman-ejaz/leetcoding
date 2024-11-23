# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        p1, p2 = dummy, dummy.next

        for _ in range(n):
            p2 = p2.next

        while p2:
            p2 = p2.next
            p1 = p1.next

        p1.next = p1.next.next

        return dummy.next






























        # p1, p2 = head, head

        # count = 1

        # while count < n + 1:
        #     p1 = p1.next
        #     count += 1

        # if not p1:
        #     return None

        # while p1.next:
        #     p1 = p1.next
        #     p2 = p2.next

        # p2.next = p2.next.next

        # return head


        dummy = ListNode(0, head)
        prev, curr = dummy, head

        for i in range(n):
            curr = curr.next

        while curr:
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next
        