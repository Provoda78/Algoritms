import sys
sys.setrecursionlimit(2000)


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  M = int(input_data[0])
  L_val = int(input_data[1])
  R_val = int(input_data[2])

  R_digits = []
  temp = R_val
  while temp > 0:
    R_digits.append(temp % M)
    temp //= M
  R_digits.reverse()

  N = len(R_digits)

  L_digits = []
  temp = L_val
  while temp > 0:
    L_digits.append(temp % M)
    temp //= M
  L_digits.reverse()

  if len(L_digits) < N:
    L_digits = [0] * (N - len(L_digits)) + L_digits

  def untightened_max_diff(k, started, min_d, max_d):
    if k >= 2:
      return M - 1
    if k == 1:
      if started:
        return max(max_d, M - 1 - min_d)
      else:
        return 0
    return max_d - min_d if started else 0

  def solve_dfs(pos, tight_L, tight_R, started, min_d, max_d):
    if not tight_L and not tight_R:
      return untightened_max_diff(N - pos, started, min_d, max_d)

    if pos == N:
      return max_d - min_d if started else 0

    min_digit = L_digits[pos] if tight_L else 0
    max_digit = R_digits[pos] if tight_R else M - 1

    best = 0
    for d in range(min_digit, max_digit + 1):
      next_tight_L = tight_L and (d == L_digits[pos])
      next_tight_R = tight_R and (d == R_digits[pos])

      if not started:
        if d == 0:
          res = solve_dfs(
              pos + 1, next_tight_L, next_tight_R, False, 10000, -10000
          )
        else:
          res = solve_dfs(pos + 1, next_tight_L, next_tight_R, True, d, d)
      else:
        res = solve_dfs(
            pos + 1,
            next_tight_L,
            next_tight_R,
            True,
            min(min_d, d),
            max(max_d, d),
        )

      if res > best:
        best = res
        if best == M - 1:
          return M - 1

    return best

  ans = solve_dfs(0, True, True, False, 10000, -10000)
  print(ans)


if __name__ == "__main__":
  solve()