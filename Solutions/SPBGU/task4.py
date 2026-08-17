import math
import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])
  b = [float(x) for x in input_data[1 : n + 1]]

  A = []
  idx = n + 1
  for i in range(n):
    row = [float(x) for x in input_data[idx : idx + n]]
    A.append(row)
    idx += n

  S1 = sum(b)
  S2 = sum(x * x for x in b)

  gamma_sq = n * S2 - S1 * S1

  def mat_vec(M, v):
    res = [0.0] * n
    for i in range(n):
      s = 0.0
      row = M[i]
      for j in range(n):
        s += row[j] * v[j]
      res[i] = s
    return res

  def mat_transpose_vec(M, v):
    res = [0.0] * n
    for i in range(n):
      s = 0.0
      for j in range(n):
        s += M[j][i] * v[j]
      res[i] = s
    return res

  def dot(u, v):
    return sum(u[i] * v[i] for i in range(n))

  def norm_sq(v):
    return sum(x * x for x in v)

  u1 = [1.0 / math.sqrt(n)] * n

  if gamma_sq < 1e-12:
    if abs(S1) < 1e-12:
      print(0.0)
      return

    v1 = u1

    def p0_norm_sq_A(w):
      return max(0.0, norm_sq(w) - dot(u1, w) ** 2)

    Av1 = mat_vec(A, v1)
    ATv1 = mat_transpose_vec(A, v1)

    ans_sq = p0_norm_sq_A(Av1) + p0_norm_sq_A(ATv1)
    print(f"{math.sqrt(max(0.0, ans_sq)):.12f}")
    return

  g_len = math.sqrt(gamma_sq)
  m12 = g_len / math.sqrt(n)
  u2 = [(b[i] - S1 / n) / m12 for i in range(n)]

  val1 = math.sqrt(n * S2) - S1
  L1 = math.hypot(g_len, val1)
  c11, c12 = g_len / L1, val1 / L1

  val2 = -math.sqrt(n * S2) - S1
  L2 = math.hypot(g_len, val2)
  c21, c22 = g_len / L2, val2 / L2

  v1 = [c11 * u1[i] + c12 * u2[i] for i in range(n)]
  v2 = [c21 * u1[i] + c22 * u2[i] for i in range(n)]

  def p0_norm_sq_B(w):
    return max(0.0, norm_sq(w) - dot(u1, w) ** 2 - dot(u2, w) ** 2)

  Av1 = mat_vec(A, v1)
  ATv1 = mat_transpose_vec(A, v1)
  Av2 = mat_vec(A, v2)
  ATv2 = mat_transpose_vec(A, v2)

  ans_sq = 0.0

  ans_sq += dot(v1, Av2) ** 2
  ans_sq += dot(v2, Av1) ** 2

  ans_sq += p0_norm_sq_B(Av1)
  ans_sq += p0_norm_sq_B(ATv1)

  ans_sq += p0_norm_sq_B(Av2)
  ans_sq += p0_norm_sq_B(ATv2)

  print(f"{math.sqrt(max(0.0, ans_sq)):.12f}")


if __name__ == "__main__":
  solve()