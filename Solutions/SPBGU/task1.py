import math
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
  
    p = float(input_data[0])
    n = int(input_data[1])
  
    dp = [0.0] * (n + 1)
    dp[1] = 1 - p

    for i in range(2, n + 1):
        sub_sum = sum(dp[k] * dp[i - k] for k in range(1, i))
        dp[i] = p * sub_sum

    ans = dp[n]
    print(f"{ans:.5f}")


if __name__ == "__main__":
  solve()