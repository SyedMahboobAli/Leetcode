# We have introduced class ListNode, _remove and _insert functions
class ListNode:
    def __init__(self,key=0,value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node

        # Dummy head and tail
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove node from DLL 
    def _remove(self,node):
        prv = node.prev
        nxt = node.next
        nxt.prev = prv
        prv.next = nxt
    
    # Insert node right after head (most recent)
    def _insert(self,node):
        #ensure steps are correct in order
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


    def get(self, key: int) -> int:
        #need not create new nodes all the time
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = ListNode(key,value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            # Remove LRU
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key] #deleting key val pair from cache dictionary. Check here we are not using (). that is func. But we use [] as we are deleting that val from dict
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
