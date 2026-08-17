import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  k = int(input_data[0])

  B = 56
  n = 115
  m = 115

  grid = [['#' for _ in range(m)] for _ in range(n)]

  for r in range(n):
    grid[r][m - 1] = '.'

  for i in range(B):
    r = 2 * i
    c = 2 * i
    grid[r][c] = '.'
    grid[r][c + 1] = '.'
    grid[r + 1][c] = '.'
    grid[r + 1][c + 1] = '.'
    grid[r + 2][c + 1] = '.'
    grid[r + 2][c + 2] = '.'

  grid[2 * B][2 * B] = '.'

  for i in range(B + 1):
    if (k >> i) & 1:
      r = 2 * i
      for c in range(2 * i, m):
        grid[r][c] = '.'

  print(f'{n} {m}')
  for row in grid:
    print(''.join(row))


if __name__ == '__main__':
  solve()