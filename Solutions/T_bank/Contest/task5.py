import sys
import numpy as np


def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    a = np.array(data[2:2 + n], dtype=np.int64)
    a.sort()

    pos = a[a > 0]
    neg = a[a < 0]
    zero_count = n - pos.size - neg.size

    def count_l(x_val: int) -> int:
        ordered = 0
        if pos.size:
            t = x_val // pos
            c = np.searchsorted(a, t, side='right')
            ordered += int(c.sum())
        if neg.size:
            t = -((-x_val) // neg)
            c = neg.size + pos.size + zero_count - np.searchsorted(a, t, side='left')
            ordered += int(c.sum())
        if zero_count:
            ordered += zero_count * (n if x_val >= 0 else 0)

        self_count = int(np.count_nonzero(a * a <= x_val))
        return (ordered - self_count) // 2

    m = int(np.max(np.abs(a))) if n else 0
    l = -(m * m) - 1
    hi = m * m

    while l < hi:
        mid = l + (hi - l) // 2
        if count_l(mid) >= k:
            hi = mid
        else:
            l = mid + 1

    print(l)


if __name__ == "__main__":
    solve()