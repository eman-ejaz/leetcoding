"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None


        oldToClone = {None: None}
        dummy = Node(0)

        temp = dummy
        curr = head

        while curr:
            temp.next = Node(curr.val)
            oldToClone[curr] = temp.next

            curr = curr.next
            temp = temp.next
        
        curr = head
        temp = dummy.next

        while curr:
            clone_random = oldToClone[curr.random]
            temp.random = clone_random

            curr = curr.next
            temp = temp.next

        return dummy.next


