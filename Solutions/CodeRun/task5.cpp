#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <cstdio>
#include <cstring>
#include <algorithm>

const int MAX_DIM = 1005;
const int MAX_CELLS = 1000005;

int bit[MAX_DIM * MAX_DIM];
int row_offset[MAX_DIM + 1];

int N, M;

struct Cell
{
    int r, c, val;
};
struct Query
{
    int r1, c1, r2, c2, x, id;
};

Cell cells[MAX_CELLS];
Cell cells_buf[MAX_CELLS];
Query queries[MAX_CELLS];

inline int readInt()
{
    int res = 0, c = getchar_unlocked();
    while (c < '0' || c > '9')
    {
        if (c == EOF)
            return -1;
        c = getchar_unlocked();
    }
    while (c >= '0' && c <= '9')
    {
        res = (res * 10) + (c - '0');
        c = getchar_unlocked();
    }
    return res;
}

inline void writeInt(int x)
{
    if (x == 0)
    {
        putchar_unlocked('0');
        putchar_unlocked('\n');
        return;
    }
    char buf[12];
    int i = 0;
    while (x > 0)
    {
        buf[i++] = (x % 10) + '0';
        x /= 10;
    }
    while (--i >= 0)
        putchar_unlocked(buf[i]);
    putchar_unlocked('\n');
}

void radix_sort_cells(int n)
{
    int count[65536];

    memset(count, 0, sizeof(count));
    for (int i = 0; i < n; i++)
        count[cells[i].val & 0xFFFF]++;
    for (int i = 1; i < 65536; i++)
        count[i] += count[i - 1];
    for (int i = n - 1; i >= 0; i--)
        cells_buf[--count[cells[i].val & 0xFFFF]] = cells[i];

    memset(count, 0, sizeof(count));
    for (int i = 0; i < n; i++)
        count[(cells_buf[i].val >> 16) & 0xFFFF]++;
    for (int i = 1; i < 65536; i++)
        count[i] += count[i - 1];
    for (int i = n - 1; i >= 0; i--)
        cells[--count[(cells_buf[i].val >> 16) & 0xFFFF]] = cells_buf[i];
}

inline void update(int r, int c, int val)
{
    for (int i = r; i <= N; i += i & -i)
    {
        int row = row_offset[i];

        for (int j = c; j <= M; j += j & -j)
            bit[row + j] += val;
    }
}

inline int query(int r, int c)
{
    int sum = 0;

    for (int i = r; i > 0; i -= i & -i)
    {
        int row = row_offset[i];

        for (int j = c; j > 0; j -= j & -j)
            sum += bit[row + j];
    }

    return sum;
}

void solve()
{
    N = readInt();
    M = readInt();
    int Q = readInt();
    int cell_count = N * M;

    for (int i = 0; i < cell_count; ++i)
    {
        cells[i] = {(i / M) + 1, (i % M) + 1, readInt()};
    }

    for (int i = 0; i < Q; ++i)
    {
        queries[i] = {readInt(), readInt(), readInt(), readInt(), readInt(), i};
    }

    radix_sort_cells(cell_count);

    std::sort(queries, queries + Q, [](const Query &a, const Query &b)
              { return a.x > b.x; });

    memset(bit, 0, sizeof(int) * (N + 1) * MAX_DIM);

    static int answers[MAX_CELLS];
    int cell_idx = cell_count - 1;

    for (int i = 0; i < Q; ++i)
    {
        while (cell_idx >= 0 && cells[cell_idx].val >= queries[i].x)
        {
            update(cells[cell_idx].r, cells[cell_idx].c, 1);
            cell_idx--;
        }
        int r1 = queries[i].r1, c1 = queries[i].c1, r2 = queries[i].r2, c2 = queries[i].c2;
        answers[queries[i].id] = query(r2, c2) - query(r1 - 1, c2) - query(r2, c1 - 1) + query(r1 - 1, c1 - 1);
    }

    for (int i = 0; i < Q; i++)
        writeInt(answers[i]);
}

int main()
{

    for (int d = 0; d <= MAX_DIM; d++)
    {
        row_offset[d] = d * MAX_DIM;
    }

    int T = readInt();
    while (T--)
        solve();
    return 0;
}