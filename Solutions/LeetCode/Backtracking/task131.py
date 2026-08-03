from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return
        
        res = []
        
        def backtracking(start: int, path: List[str]):
            if start == len(s):
                res.append(path[:])
                return []
                
            for i in range(start+1, len(s)+1):
                substr = s[start:i]
                
                if substr == substr[::-1]:
                    path.append(substr)
                    backtracking(i, path)
                    path.pop()
          
        backtracking(0, [])             
        return res
    
if __name__ == '__main__':
    solve = Solution()
    ans = solve.partition(input())
    print(ans)
                        

                    