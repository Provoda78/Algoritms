import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    n = int(next(iterator))
    num_prt = 1 << n

    c = [[0] * (n + 1) for _ in range(num_prt + 1)]
    for i in range(1, num_prt + 1):
        for j in range(1, n + 1):
            c[i][j] = int(next(iterator))

    dp = [0] * (num_prt + 1)

    for k in range(1, n + 1):
        block_size = 1 << k
        half_size = 1 << (k - 1)
        next_dp = [0] * (num_prt + 1)

        for start in range(1, num_prt + 1, block_size):
            left_range = range(start, start + half_size)
            right_range = range(start + half_size, start + block_size)

            max_right = max(dp[j] + c[j][k - 1] for j in right_range)
            max_left = max(dp[i] + c[i][k - 1] for i in left_range)

            for i in left_range:
                next_dp[i] = dp[i] + max_right

            for j in right_range:
                next_dp[j] = dp[j] + max_left

        dp = next_dp

    ans = max(dp[i] + c[i][n] for i in range(1, num_prt + 1))
    print(ans)

if __name__ == '__main__':
    solve()