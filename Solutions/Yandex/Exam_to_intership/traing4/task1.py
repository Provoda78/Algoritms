from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str])->List[List[str]]:
    if not strs:
        return []
    
    groups = defaultdict(list)
    
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
        
    return list(groups.values())