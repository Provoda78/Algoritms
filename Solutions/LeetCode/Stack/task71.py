class Solution:
    
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        commamds = path.split('/')
        
        for ch in commamds:
            
            if ch == '.' or ch == '':
                continue
                
            elif ch == '..':
                if stack:
                    stack.pop()
                
            else:
                stack.append(ch)
        
        return '/' + '/'.join(stack)