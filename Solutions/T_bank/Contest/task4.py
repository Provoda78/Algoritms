import sys

def solve(n, k):
    
    right = n
    left = 1
    res = []
    
    while left <= right:
        count_per = right - left
        
        if count_per <= k:
            res.append(right)
            k -= count_per
            right -= 1
        else:
            res.append(left)
            left += 1
    
    print(*(res))
    
if __name__ == '__main__':
    
    input_d = sys.stdin.read().split()
    if input_d:
        n = int(input_d[0])
        k = int(input_d[1])
    
    solve(n, k)