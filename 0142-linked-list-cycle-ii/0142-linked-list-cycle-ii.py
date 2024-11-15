# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ns = set()
        curr = head

        while curr:
            if curr in ns:
                return curr
            
            ns.add(curr)

            curr = curr.next

        return None




        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                temp = head
                while temp is not slow:
                    temp = temp.next
                    slow = slow.next
                
                return temp
        return None