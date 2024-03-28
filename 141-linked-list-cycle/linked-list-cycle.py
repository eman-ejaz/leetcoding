# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        node_freq = {}

        while temp:
            node_freq[temp] = node_freq.get(temp, 0) + 1

            if node_freq.get(temp) > 1:
                return True
                
            temp = temp.next
        
        return False

        