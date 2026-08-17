import numpy as np
import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])

  dirs = []
  idx = 1
  for _ in range(n):
    dirs.append(input_data[idx : idx + n])
    idx += n

  puddles = []
  for _ in range(n):
    puddles.append(input_data[idx : idx + n])
    idx += n

  total_cells = n * n
  A = np.zeros((total_cells, total_cells))
  b = np.zeros(total_cells)

  dir_map = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}
  all_dirs = ['u', 'd', 'l', 'r']

  for r in range(n):
    for c in range(n):
      u_idx = r * n + c

      if puddles[r][c] == 'y':
        A[u_idx, u_idx] = 1.0
        b[u_idx] = 0.0
        continue

      if r == n - 1 and c == n - 1:
        A[u_idx, u_idx] = 1.0
        b[u_idx] = 1.0
        continue

      unwanted = dirs[r][c]
      available = [d for d in all_dirs if d != unwanted]

      valid_moves = []
      for d in available:
        dr, dc = dir_map[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
          valid_moves.append((nr, nc))

      k = len(valid_moves)

      if k == 0:
        A[u_idx, u_idx] = 1.0
        b[u_idx] = 0.0
        continue

      A[u_idx, u_idx] = float(k)
      for nr, nc in valid_moves:
        v_idx = nr * n + nc
        A[u_idx, v_idx] -= 1.0
      b[u_idx] = 0.0

  try:
    ans = np.linalg.solve(A, b)
    res = ans[0]
  except np.linalg.LinAlgError:
    ans, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    res = ans[0]

  print(f'{max(0.0, float(res)):.12f}')


if __name__ == '__main__':
  solve()