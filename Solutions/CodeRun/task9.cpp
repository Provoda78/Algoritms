#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <iostream>
#include <algorithm>

const int MAXN = 2000005;
const int MAXLOG = 21;

unsigned int starts[MAXN];
unsigned int ends[MAXN];

int up[MAXLOG][MAXN];
int order_by_end[MAXN];
int suff_best_idx[MAXN];

int buffer[MAXN];

void radix_sort(int *arr, int n)
{
    int count[256];
    for (int shift = 0; shift < 32; shift += 8)
    {
        for (int i = 0; i < 256; i++)
            count[i] = 0;
        for (int i = 0; i < n; i++)
            count[(ends[arr[i]] >> shift) & 0xFF]++;
        int pref = 0;
        for (int i = 0; i < 256; i++)
        {
            int tmp = count[i];
            count[i] = pref;
            pref += tmp;
        }
        for (int i = 0; i < n; i++)
            buffer[count[(ends[arr[i]] >> shift) & 0xFF]++] = arr[i];
        for (int i = 0; i < n; i++)
            arr[i] = buffer[i];
    }
}

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

void solve()
{
    int n = readInt();
    if (n == -1)
        return;
    unsigned int T = (unsigned int)readInt();

    for (int i = 0; i < n; i++)
    {
        starts[i] = readInt();
        unsigned int d = readInt();
        ends[i] = starts[i] + d;
    }
    for (int i = 0; i < n; i++)
    {
        starts[i + n] = starts[i] + T;
        ends[i + n] = ends[i] + T;
    }

    int total = 2 * n;

    starts[total] = 2e9 + 7;
    ends[total] = 2e9 + 7;

    for (int i = 0; i < total; i++)
        order_by_end[i] = i;
    radix_sort(order_by_end, total);

    suff_best_idx[total - 1] = total - 1;
    for (int i = total - 2; i >= 0; i--)
    {
        suff_best_idx[i] = (ends[i] < ends[suff_best_idx[i + 1]]) ? i : suff_best_idx[i + 1];
    }

    int log_h = 0;
    while ((1 << log_h) <= n)
        log_h++;
    log_h++;

    int r = 0;
    for (int i = 0; i < total; i++)
    {
        int l = order_by_end[i];
        while (r < total && starts[r] < ends[l])
            r++;

        up[0][l] = (r < total) ? suff_best_idx[r] : total;
    }
    up[0][total] = total;

    for (int j = 1; j < log_h; j++)
    {
        for (int i = 0; i <= total; i++)
        {
            up[j][i] = up[j - 1][up[j - 1][i]];
        }
    }

    int max_tasks = 0;
    for (int i = 0; i < n; i++)
    {
        unsigned int limit = starts[i] + T;

        if (ends[i] > limit)
            continue;

        int curr = i;
        int count = 1;

        for (int j = log_h - 1; j >= 0; j--)
        {
            int next = up[j][curr];

            if (next < total && ends[next] <= limit)
            {
                count += (1 << j);
                curr = next;
            }
        }

        if (count > max_tasks)
            max_tasks = count;
    }

    std::cout << (max_tasks > n ? n : max_tasks) << "\n";
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int Tc = readInt();
    while (Tc--)
        solve();
    return 0;
}