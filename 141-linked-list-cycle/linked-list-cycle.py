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
            if temp in node_freq and node_freq.get(temp) > 1:
                return True
            
            node_freq[temp] = node_freq.get(temp, 0) + 1

            temp = temp.next
        
        return False

        