import sys

def solve(s: str) -> int:
    need = len(set(s))
    cnt = {}
    have = 0
    ans = 0
    r = 0
    n = len(s)

    for l in range(n):
        while r < n and have < need:
            ch = s[r]
            cnt[ch] = cnt.get(ch, 0) + 1
            if cnt[ch] == 1:
                have += 1
            r += 1

        if have == need:
            ans += n - r + 1

        ch = s[l]
        cnt[ch] -= 1
        if cnt[ch] == 0:
            have -= 1
            del cnt[ch]

    return ans

if __name__ == "__main__":
    s = sys.stdin.read().rstrip("\n")
    print(solve(s))