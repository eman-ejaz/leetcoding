# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        res = dummy

        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next

            res = res.next

        if not list1 and list2:
            while list2:
                res.next = list2
                list2 = list2.next
                res = res.next
        else:
            while list1:
                res.next = list1
                list1 = list1.next
                res = res.next

        return dummy.next
