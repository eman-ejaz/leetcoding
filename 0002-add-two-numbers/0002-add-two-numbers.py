# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val + carry

            carry = sum // 10 if sum >= 10 else 0
            num_to_add = sum % 10 if sum >= 10 else sum

            curr.next = ListNode(num_to_add)

            curr = curr.next

            l1 = l1.next
            l2 = l2.next
        
        while l1 and not l2:
            sum = l1.val + carry

            carry = sum // 10 if sum >= 10 else 0
            num_to_add = sum % 10 if sum >= 10 else sum

            curr.next = ListNode(num_to_add)

            curr = curr.next

            l1 = l1.next

        while l2 and not l1:
            sum = l2.val + carry

            carry = sum // 10 if sum >= 10 else 0
            num_to_add = sum % 10 if sum >= 10 else sum

            curr.next = ListNode(num_to_add)

            curr = curr.next

            l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry)

        return dummy.next
        


        