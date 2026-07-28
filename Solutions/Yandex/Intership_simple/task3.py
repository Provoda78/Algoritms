import sys

def solve():
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    curr_len = 0
    max_len = 0
    
    for i in range(1, n+1):
        num = int(input_data[i])

        if num == 1:
            curr_len += 1
            if max_len < curr_len:
                max_len = curr_len
                
        else:
            curr_len = 0
            
    print(max_len)