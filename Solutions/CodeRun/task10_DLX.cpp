#pragma GCC optimize("O3,unroll-loops")

#include <cstdio>
#include <cstdint>

static inline int readInt()
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

static char outBuf[1 << 22];
static int outPos = 0;

static inline void writeInt(int x)
{
    if (x >= 10)
        outBuf[outPos++] = '0' + x / 10;
    outBuf[outPos++] = '0' + x % 10;
}

static inline void writeChar(char c) { outBuf[outPos++] = c; }

const int MAX_NODES = 20005;
int16_t L[MAX_NODES], R[MAX_NODES], U[MAX_NODES], D[MAX_NODES], C[MAX_NODES];
int16_t S[1030];
int16_t node_r[MAX_NODES], node_c[MAX_NODES], node_v[MAX_NODES];
int ans_r[300], ans_c[300], ans_v[300];
int grid[256];
int sz, ans_sz;
int n, N;

uint32_t rowMask[16];
uint32_t colMask[16];
uint32_t boxMask[16];
uint32_t FULL_MASK;

static inline void init(int n_cols)
{
    for (int i = 0; i <= n_cols; ++i)
    {
        L[i] = i - 1;
        R[i] = i + 1;
        U[i] = i;
        D[i] = i;
        C[i] = i;
        S[i] = 0;
    }
    L[0] = n_cols;
    R[n_cols] = 0;
    sz = n_cols + 1;
    ans_sz = 0;
}

static inline uint32_t getCandidates(int r, int c)
{
    int b = (r / n) * n + (c / n);

    return FULL_MASK &
           ~(rowMask[r] |
             colMask[c] |
             boxMask[b]);
}

static inline void addNode(int node, int col, int r, int c, int v)
{
    U[node] = U[col];
    D[node] = col;
    D[U[col]] = node;
    U[col] = node;
    C[node] = col;
    S[col]++;
    node_r[node] = r;
    node_c[node] = c;
    node_v[node] = v;
}

static inline __attribute__((always_inline)) void cover(int c)
{
    L[R[c]] = L[c];
    R[L[c]] = R[c];
    for (int i = D[c]; i != c; i = D[i])
    {
        for (int j = R[i]; j != i; j = R[j])
        {
            U[D[j]] = U[j];
            D[U[j]] = D[j];
            S[C[j]]--;
        }
    }
}

static inline __attribute__((always_inline)) void uncover(int c)
{
    for (int i = U[c]; i != c; i = U[i])
    {
        for (int j = L[i]; j != i; j = L[j])
        {
            S[C[j]]++;
            U[D[j]] = j;
            D[U[j]] = j;
        }
    }
    L[R[c]] = c;
    R[L[c]] = c;
}

bool dfs()
{
    if (R[0] == 0)
        return true;

    int c = R[0];
    int best = S[c];
    for (int i = R[c]; i != 0; i = R[i])
    {
        if (S[i] < best)
        {
            c = i;
            best = S[i];
            if (best == 0)
                break;
        }

        else if (S[i] == best)
        {
            if (i > 3 * N * N)
            {
                c = i;
            }
        }
    }

    if (best == 0)
        return false;

    cover(c);
    for (int i = D[c]; i != c; i = D[i])
    {
        ans_r[ans_sz] = node_r[i];
        ans_c[ans_sz] = node_c[i];
        ans_v[ans_sz] = node_v[i];
        ans_sz++;

        for (int j = R[i]; j != i; j = R[j])
            cover(C[j]);

        if (dfs())
            return true;

        for (int j = L[i]; j != i; j = L[j])
            uncover(C[j]);

        ans_sz--;
    }
    uncover(c);
    return false;
}

void solve()
{
    n = readInt();
    if (n == -1)
        return;

    N = n * n;

    FULL_MASK = (1u << N) - 1;

    for (int i = 0; i < 16; i++)
    {
        rowMask[i] = 0;
        colMask[i] = 0;
        boxMask[i] = 0;
    }

    for (int r = 0; r < N; r++)
    {
        for (int c = 0; c < N; c++)
        {
            int val = readInt();

            grid[r * N + c] = val;

            if (val)
            {
                uint32_t bit = 1u << (val - 1);

                rowMask[r] |= bit;
                colMask[c] |= bit;

                int b = (r / n) * n + c / n;
                boxMask[b] |= bit;
            }
        }
    }

    bool changed;

    do
    {
        changed = false;

        for (int r = 0; r < N; r++)
        {
            for (int c = 0; c < N; c++)
            {
                if (grid[r * N + c])
                    continue;

                uint32_t mask = getCandidates(r, c);

                if (mask == 0)
                {
                    writeChar('N');
                    writeChar('O');
                    writeChar('\n');
                    return;
                }

                if ((mask & (mask - 1)) == 0)
                {
                    int v = __builtin_ctz(mask) + 1;

                    grid[r * N + c] = v;

                    uint32_t bit = mask;

                    rowMask[r] |= bit;
                    colMask[c] |= bit;

                    int b = (r / n) * n + c / n;
                    boxMask[b] |= bit;

                    changed = true;
                }
            }
        }

    } while (changed);

    init(4 * N * N);

    for (int r = 0; r < N; r++)
    {
        for (int c = 0; c < N; c++)
        {
            int val = grid[r * N + c];

            int v_start = 0;
            int v_end = N - 1;

            if (val)
            {
                v_start = val - 1;
                v_end = val - 1;
            }
            else
            {
                uint32_t mask = getCandidates(r, c);

                v_start = 0;
                v_end = N - 1;

                for (int v = 0; v < N; v++)
                {
                    if (!(mask & (1u << v)))
                        continue;

                    int b = (r / n) * n + c / n;

                    int c1 = r * N + c + 1;
                    int c2 = N * N + r * N + v + 1;
                    int c3 = 2 * N * N + c * N + v + 1;
                    int c4 = 3 * N * N + b * N + v + 1;

                    int first = sz;

                    addNode(first, c1, r, c, v + 1);
                    addNode(first + 1, c2, r, c, v + 1);
                    addNode(first + 2, c3, r, c, v + 1);
                    addNode(first + 3, c4, r, c, v + 1);

                    for (int i = 0; i < 4; i++)
                    {
                        L[first + i] = first + (i + 3) % 4;
                        R[first + i] = first + (i + 1) % 4;
                    }

                    sz += 4;
                }

                continue;
            }

            for (int v = v_start; v <= v_end; v++)
            {
                int b = (r / n) * n + c / n;

                int c1 = r * N + c + 1;
                int c2 = N * N + r * N + v + 1;
                int c3 = 2 * N * N + c * N + v + 1;
                int c4 = 3 * N * N + b * N + v + 1;

                int first = sz;

                addNode(first, c1, r, c, v + 1);
                addNode(first + 1, c2, r, c, v + 1);
                addNode(first + 2, c3, r, c, v + 1);
                addNode(first + 3, c4, r, c, v + 1);

                for (int i = 0; i < 4; i++)
                {
                    L[first + i] = first + (i + 3) % 4;
                    R[first + i] = first + (i + 1) % 4;
                }

                sz += 4;
            }
        }
    }

    if (dfs())
    {
        writeChar('Y');
        writeChar('E');
        writeChar('S');
        writeChar('\n');

        for (int i = 0; i < ans_sz; i++)
        {
            grid[ans_r[i] * N +
                 ans_c[i]] = ans_v[i];
        }

        for (int r = 0; r < N; r++)
        {
            for (int c = 0; c < N; c++)
            {
                writeInt(grid[r * N + c]);
                writeChar(c == N - 1 ? '\n' : ' ');
            }
        }
    }
    else
    {
        writeChar('N');
        writeChar('O');
        writeChar('\n');
    }
}

int main()
{
    int T = readInt();
    if (T == -1)
        return 0;

    while (T--)
        solve();

    fwrite(outBuf, 1, outPos, stdout);

    return 0;
}