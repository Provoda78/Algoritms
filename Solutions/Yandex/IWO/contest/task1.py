import sys


def search_right(intervals, target, right):
    low = 0
    high = right - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if intervals[mid][1] <= target:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans + 1


def solve():
    input_d = sys.stdin.read().split()
    if not input_d:
        return

    n = int(input_d[0])

    intervals = []
    idx = 1
    for i in range(n):
        a = int(input_d[idx])
        b = int(input_d[idx + 1])
        idx += 2
        intervals.append((a, a + b, b, i))

    intervals.sort(key=lambda x: x[1])

    dp = [0] * (n + 1)
    choice = [False] * (n + 1)
    parent = [0] * (n + 1)
    
    for i in range(1, n + 1):
        start_i, end_i, b_i, id = intervals[i - 1]
        
        p = search_right(intervals, start_i, i-1)
        
        cur_max = dp[p] + b_i
        prev_max = dp[i-1]
        
        if cur_max > prev_max:
            dp[i] = cur_max
            parent[i] = p
            choice[i] = True
        else:
            dp[i] = prev_max
            parent[i] = i-1
    
    cur = n
    empls = []
    while cur > 0:
        if choice[cur]:
            empls.append(intervals[cur - 1][3])
            cur = parent[cur]
        else:
            cur = cur - 1

    print(dp[n])
    print(*empls)

if __name__ == '__main__':
    solve()