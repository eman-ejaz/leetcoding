class LinkedList:
    def __init__(self, key, val, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.head = LinkedList(0, 0)
        self.tail = LinkedList(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.list_map = {}
        self.capacity = capacity

    def remove(self, node):
        tprev = node.prev
        tnext = node.next

        node.prev.next = tnext
        node.next.prev = tprev
    
    def add_to_front(self, node):
        tnext = self.head.next

        self.head.next = node
        node.prev = self.head
        node.next = tnext
        tnext.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.list_map:
            return -1
        node = self.list_map[key]

        val = node.val

        self.remove(node)
        self.add_to_front(node)

        self.list_map[key] = node

        return val
        

    def put(self, key: int, value: int) -> None:
        if (key in self.list_map):
            node = self.list_map[key]

            node.val = value

            self.remove(node)
            self.add_to_front(node)
            
        else:
            if len(self.list_map) < self.capacity:
                node = LinkedList(key, value)
                self.list_map[key] = node

                self.add_to_front(node)
            else:
                del self.list_map[self.tail.prev.key]
                self.remove(self.tail.prev)

                node = LinkedList(key, value)
                self.add_to_front(node)
                self.list_map[key] = node
            
            
           

                
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)