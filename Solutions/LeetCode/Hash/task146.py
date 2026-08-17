from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cash = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cash:
            return -1
        
        self.cash.move_to_end(key, last=True)
        return self.cash[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cash:
            self.cash.move_to_end(key, last=True)
            
        self.cash[key] = value
        
        if len(self.cash) > self.size:
            self.cash.popitem(last=False)