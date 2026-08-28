class Node:

  def __init__(self, key: int = 0, val: int = 0):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None


class LRUCache:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}  #key -> Node

    self.head = Node()
    self.tail = Node()
    self.head.next = self.tail
    self.tail.prev = self.head

  def _remove(self, node: Node) -> None:
    '''Удалить узел из текущего места в двусвязном списке'''
    
    node.prev.next = node.next
    node.next.prev = node.prev

  def _add_to_tail(self, node: Node) -> None:
    '''Вставить узел перед tail (сделать его MRU)'''
    
    node.next = self.tail
    node.prev = self.tail.prev
    self.tail.prev.next = node
    self.tail.prev = node

  def get(self, key: int) -> int:
    if key not in self.cache:
        return -1
    
    node = self.cache[key] 
    self._remove(node)
    self._add_to_tail(node)
    
    return node.val

  def put(self, key: int, value: int) -> None:
    
    if key in self.cache:
        self._remove(self.cache[key])
        
    node = Node(key=key, val=value)
    self.cache[key] = node
    self._add_to_tail(node)
    
    if len(self.cache) > self.capacity:
        
        lru = self.head.next
        del self.cache[lru.key]
        self._remove(lru)