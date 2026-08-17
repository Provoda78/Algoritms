from collections import deque
from typing import Optional

class NestedIterator:
    def __init__(self, nestedList):
        self.q = deque()
        self._flatten(nestedList)
        
    def _flatten(self, nestedList):
        for elem in nestedList:
            if elem.isInteger():
                self.q.append(elem.getInteger())
            else:
                self._flatten(elem.getList())
            
    def next(self) -> int:
        return self.q.popleft()
    
    def hasNext(self) -> bool:
        return len(self.q) > 0