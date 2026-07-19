#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <cstdio>
#include <algorithm>

const int MAXN = 5000005;

int keys[MAXN];
int vals[MAXN];
int buf_k[MAXN];
int buf_v[MAXN];

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
        res = (res << 3) + (res << 1) + (c - '0');
        c = getchar_unlocked();
    }
    return res;
}

inline void writeInt(int x)
{
    if (x == 0)
    {
        putchar_unlocked('0');
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
}

void radix_sort(int n)
{
    int *k_src = keys;
    int *v_src = vals;
    int *k_dst = buf_k;
    int *v_dst = buf_v;

    for (int shift = 0; shift < 32; shift += 8)
    {
        int count[256] = {0};

        for (int i = 0; i < n; ++i)
            count[(k_src[i] >> shift) & 0xFF]++;

        int pref[256];
        pref[0] = 0;
        for (int i = 1; i < 256; ++i)
            pref[i] = pref[i - 1] + count[i - 1];

        for (int i = 0; i < n; ++i)
        {
            int byte = (k_src[i] >> shift) & 0xFF;
            int pos = pref[byte]++;
            k_dst[pos] = k_src[i];
            v_dst[pos] = v_src[i];
        }

        std::swap(k_src, k_dst);
        std::swap(v_src, v_dst);
    }

    if (k_src != keys)
    {
        for (int i = 0; i < n; ++i)
        {
            keys[i] = k_src[i];
            vals[i] = v_src[i];
        }
    }
}

int main()
{
    int m = readInt();
    if (m == -1)
        return 0;

    int total_records = 0;
    for (int i = 0; i < m; ++i)
    {
        int l = readInt();
        for (int j = 0; j < l; ++j)
        {
            keys[total_records] = readInt();
            vals[total_records] = readInt();
            total_records++;
        }
    }

    radix_sort(total_records);

    for (int i = 0; i < total_records; ++i)
    {
        if (i == total_records - 1 || keys[i] != keys[i + 1])
        {
            writeInt(keys[i]);
            putchar_unlocked(' ');
            writeInt(vals[i]);
            putchar_unlocked('\n');
        }
    }

    return 0;
}