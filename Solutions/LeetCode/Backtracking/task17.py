from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc',  '3': 'def',   '4': 'ghi',
            '5': 'jkl',  '6': 'mno',   '7': 'pqrs',
            '8': 'tuv',  '9': 'wxyz'
        }
        
        result = []
        
        def backtracking(idx: int, path: List):
            if idx == len(digits):
                result.append("".join(path))
                return
            
            dig = digits[idx]   
            for ch in phone_map[dig]:
                path.append(ch)
                backtracking(idx+1, path)
                path.pop()
              
        backtracking(0, [])        
        return result
    
if __name__ == '__main__':
    solve = Solution()
    ans = solve.letterCombinations(digits='23')                    
    print(ans)  
                
                
            