#include <iostream>
#include <algorithm>

inline int readInt()
{
    int c = getchar_unlocked();
    while (c <= 32)
    {
        if (c == EOF)
            return -1;
        c = getchar_unlocked();
    }
    int res = 0;
    while (c > 32)
    {
        res = res * 10 + (c - '0');
        c = getchar_unlocked();
    }
    return res;
}

int n, N, all_mask;
int grid[256];

int masks[48];
int block_map[256];

struct Rollback
{
    int idx;
};

bool propagate(Rollback *changed_cells, int &changed_cnt)
{
    while (true)
    {
        bool changed = false;

        for (int i = 0; i < N * N; ++i)
        {
            if (grid[i] != 0)
                continue;

            int r = i / N;
            int c = i % N;
            int b = block_map[i];

            int used = masks[r] | masks[16 + c] | masks[32 + b];
            int mask = all_mask & ~used;

            if (mask == 0)
                return false;

            if ((mask & (mask - 1)) == 0)
            {
                int val = __builtin_ctz(mask);
                int bit = (1 << val);

                grid[i] = val;
                masks[r] |= bit;
                masks[16 + c] |= bit;
                masks[32 + b] |= bit;

                changed_cells[changed_cnt++] = {i};
                changed = true;
            }
        }
        if (!changed)
            break;
    }
    return true;
}

bool dfs()
{
    int min_cnt = 99;
    int best_idx = -1;
    int best_mask = 0;

    for (int i = 0; i < N * N; ++i)
    {
        if (grid[i] == 0)
        {
            int r = i / N;
            int c = i % N;
            int b = block_map[i];
            int mask = all_mask & ~(masks[r] | masks[16 + c] | masks[32 + b]);
            int cnt = __builtin_popcount(mask);

            if (cnt == 0)
                return false;

            if (cnt < min_cnt)
            {
                min_cnt = cnt;
                best_mask = mask;
                best_idx = i;
                if (min_cnt == 1)
                    break;
            }
        }
    }

    if (best_idx == -1)
        return true;

    int r = best_idx / N;
    int c = best_idx % N;
    int b = block_map[best_idx];

    Rollback changed_cells[256];

    while (best_mask > 0)
    {
        int val = __builtin_ctz(best_mask);
        int bit = (1 << val);
        best_mask ^= bit;

        grid[best_idx] = val;
        masks[r] |= bit;
        masks[16 + c] |= bit;
        masks[32 + b] |= bit;

        int changed_cnt = 0;

        if (propagate(changed_cells, changed_cnt))
        {
            if (dfs())
                return true;
        }

        for (int i = changed_cnt - 1; i >= 0; --i)
        {
            int idx = changed_cells[i].idx;
            int cr = idx / N;
            int cc = idx % N;
            int cb = block_map[idx];
            int cval = grid[idx];
            int cbit = (1 << cval);

            masks[cr] ^= cbit;
            masks[16 + cc] ^= cbit;
            masks[32 + cb] ^= cbit;
            grid[idx] = 0;
        }

        masks[r] ^= bit;
        masks[16 + c] ^= bit;
        masks[32 + b] ^= bit;
        grid[best_idx] = 0;
    }

    return false;
}

void solve()
{
    n = readInt();
    if (n == -1)
        return;
    N = n * n;
    all_mask = (1 << (N + 1)) - 2;

    std::fill(grid, grid + 256, 0);
    std::fill(masks, masks + 48, 0);

    bool initial_conflict = false;

    for (int r = 0; r < N; r++)
    {
        for (int c = 0; c < N; c++)
        {
            int val = readInt();
            int idx = r * N + c;
            grid[idx] = val;
            block_map[idx] = (r / n) * n + (c / n);

            if (val != 0)
            {
                int bit = (1 << val);
                int b = block_map[idx];
                if ((masks[r] & bit) || (masks[16 + c] & bit) || (masks[32 + b] & bit))
                {
                    initial_conflict = true;
                }
                masks[r] |= bit;
                masks[16 + c] |= bit;
                masks[32 + b] |= bit;
            }
        }
    }

    Rollback dummy[256];
    int dummy_cnt = 0;
    if (initial_conflict || !propagate(dummy, dummy_cnt))
    {
        std::cout << "NO\n";
        return;
    }

    if (dfs())
    {
        std::cout << "YES\n";
        for (int r = 0; r < N; r++)
        {
            for (int c = 0; c < N; c++)
            {
                std::cout << grid[r * N + c] << (c == N - 1 ? "" : " ");
            }
            std::cout << "\n";
        }
    }
    else
    {
        std::cout << "NO\n";
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int T = readInt();
    if (T == -1)
        return 0;
    while (T--)
        solve();

    return 0;
}