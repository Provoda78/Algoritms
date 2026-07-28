import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return 
    
    n = int(input_data[0])
    c = [int(x) for x in input_data[1:n+1]]
    
    if len(c) < 2:
        print(0)
        return
    
    goodness_len = 0
    
    for i in range(len(c) - 1):
        goodness_len += min(c[i], c[i+1])
        
    print(goodness_len)
    
if __name__ == '__main__':
    solve()