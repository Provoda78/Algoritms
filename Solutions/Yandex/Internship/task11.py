import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    nums = [int(x) for x in input_data]
    
    max1, max2 = -1e6, -1e6
    min1, min2 = 1e6, 1e6
       
    for x in nums:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x
            
        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x
                
    if max1 * max2 > min1 * min2:
        print(max2, max1)
    else:
        print(min1, min2)
        
if __name__ == '__main__':
    solve()