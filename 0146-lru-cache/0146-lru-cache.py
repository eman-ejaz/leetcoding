class LinkedList:
    def __init__(self, key, val, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.head = LinkedList(0, 0)  # Dummy head
        self.tail = LinkedList(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.list_map = {}
        self.capacity = capacity

    def remove(self, node):
        """Remove a node from its current position."""
        tprev = node.prev
        tnext = node.next
        tprev.next = tnext
        tnext.prev = tprev

    def add_to_front(self, node):
        """Add a node right after the head."""
        tnext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tnext
        tnext.prev = node

    def get(self, key: int) -> int:
        if key not in self.list_map:
            return -1
        node = self.list_map[key]

        # Move the accessed node to the front
        self.remove(node)
        self.add_to_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.list_map:
            # Update value and move node to front
            node = self.list_map[key]
            node.val = value
            self.remove(node)
            self.add_to_front(node)
        else:
            if len(self.list_map) >= self.capacity:
                # Remove the least recently used (LRU) node
                lru_node = self.tail.prev
                self.remove(lru_node)
                del self.list_map[lru_node.key]

            # Add the new node
            new_node = LinkedList(key, value)
            self.add_to_front(new_node)
            self.list_map[key] = new_node
