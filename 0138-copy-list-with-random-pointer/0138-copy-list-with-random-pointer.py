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




        # dummy = Node(0)
        # curr = head
        # temp = dummy

        # org_node_map = {}
        # new_node_map = {}
        # counter = 1

        # while curr:
        #     temp.next = Node(curr.val)

        #     org_node_map[curr] = counter
        #     arr = new_node_map.get(curr.val, [])
        #     arr.append((counter, temp.next))
        #     new_node_map[curr.val] = arr
        #     temp = temp.next
        #     curr = curr.next

        #     counter += 1
        
        # temp_clone = dummy.next
        # temp_head = head

        # print(org_node_map)

        # while temp_head:
        #     if not temp_head.random:
        #         temp_clone.random = temp.next
        #     else:
        #         random = temp_head.random
        #         random_index = org_node_map[random]

        #         clone_nodes = new_node_map[random.val]

        #         for n in clone_nodes:
        #             index, node = n
        #             if index == random_index:
        #                 temp_clone.random = node
        #                 break

        #     temp_head = temp_head.next
        #     temp_clone = temp_clone.next

        # return dummy.next
                
            

        

        
        