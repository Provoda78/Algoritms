from typing import List

class DSU:
    def __init__(self, nums: List[int]):
        self.parents = {num: num for num in nums}
        self.size = {num: 1 for num in nums}
        self.max_size = 1 if nums else 0
        
    def find(self, v: int) -> int:
        if self.parents[v] == v:
            return v
        
        self.parents[v] = self.find(self.parents[v])
        return self.parents[v]
    
    def union(self, u: int, v: int) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False
        
        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u
            
        self.parents[root_v] = root_u
        self.size[root_u] += self.size[root_v]
        
        if self.size[root_u] > self.max_size:
                self.max_size = self.size[root_u]
                    
        return True 


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        dsu = DSU(nums)
        
        for num in nums:
            if num - 1 in dsu.parents:
                dsu.union(num-1, num)
                
        return dsu.max_size
    
if __name__ == '__main__':
    solve = Solution()
    nums = list(map(int, input().split()))
    print(solve.longestConsecutive(nums))