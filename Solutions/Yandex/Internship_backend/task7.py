import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return   
    
    n = int(input_data[0])
     
    if n < 3:
        print(2**n)
        
    else:
        f0, f1, f2 = 1, 2, 4
        
        for _ in range(n-2):
            f3 = f0 + f1 + f2
            f0, f1, f2 = f1, f2, f3
            
        print(f3)

        
if __name__ == '__main__':
    solve()