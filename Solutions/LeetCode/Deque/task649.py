from typing import List
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad_q = deque()
        dir_q = deque()
        n = len(senate)
        
        for idx, senator in enumerate(senate):
            if senator == 'R':
                rad_q.append(idx)
            else:
                dir_q.append(idx)
        
        while rad_q and dir_q:
                
            r_idx = rad_q.popleft()
            d_idx = dir_q.popleft()
                
            if r_idx < d_idx:
                rad_q.append(r_idx + n)
            else:
                dir_q.append(d_idx + n)
        
        
        return "Radiant" if rad_q else "Dire"