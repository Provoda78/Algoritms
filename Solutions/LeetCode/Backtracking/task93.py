from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        
        res = []
        
        def backtracking(start: int, path: List[str]):
            
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return
            
            for i in range(start+1, len(s)+1):
                sub = s[start:i]
                
                if len(sub) > 1 and sub[0] == '0':
                    break
                
                if int(sub) <= 255:
                    path.append(sub)
                    backtracking(i, path)
                    path.pop()
                    
        backtracking(0, [])             
        return res
                    
if __name__ == '__main__':
    solve = Solution()
    ans = solve.restoreIpAddresses(input())
    print(ans)