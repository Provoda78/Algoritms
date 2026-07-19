#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <cstdio>
#include <cstdlib>
#include <cstring>

const int MAXN = 500005;

long long pref_sum[MAXN];
long long pref_xor[MAXN];
int dq_idx[MAXN];
long long dq_val[MAXN];

static char *ibuf = nullptr;
static char *iptr = nullptr;
static char *iend = nullptr;

inline void initInput()
{
    if (fseek(stdin, 0, SEEK_END) == 0)
    {
        long sz = ftell(stdin);
        if (sz > 0)
        {
            fseek(stdin, 0, SEEK_SET);
            ibuf = (char *)malloc((size_t)sz + 16);
            size_t got = fread(ibuf, 1, (size_t)sz, stdin);
            iptr = ibuf;
            iend = ibuf + got;
            return;
        }
        fseek(stdin, 0, SEEK_SET);
    }
    size_t cap = 1 << 22;
    ibuf = (char *)malloc(cap);
    size_t total = 0;
    for (;;)
    {
        if (total == cap)
        {
            cap *= 2;
            ibuf = (char *)realloc(ibuf, cap);
        }
        size_t got = fread(ibuf + total, 1, cap - total, stdin);
        if (got == 0)
            break;
        total += got;
    }
    iptr = ibuf;
    iend = ibuf + total;
}

inline long long readLong()
{
    while (iptr < iend && (*iptr < '0' || *iptr > '9'))
        ++iptr;
    if (iptr >= iend)
        return -1;
    long long res = 0;
    while (iptr < iend && *iptr >= '0' && *iptr <= '9')
    {
        res = res * 10 + (*iptr - '0');
        ++iptr;
    }
    return res;
}

static char *obuf = nullptr;
static size_t ocap = 0;
static size_t olen = 0;
static char digit_pairs[200];

inline void initDigitPairs()
{
    for (int i = 0; i < 100; i++)
    {
        digit_pairs[i * 2] = (char)('0' + i / 10);
        digit_pairs[i * 2 + 1] = (char)('0' + i % 10);
    }
}

inline void initOutput(size_t capacity)
{
    ocap = capacity;
    obuf = (char *)malloc(ocap);
    olen = 0;
}

inline void ensureOutputCapacity(size_t extra)
{
    if (olen + extra > ocap)
    {
        ocap = (ocap + extra) * 2;
        obuf = (char *)realloc(obuf, ocap);
    }
}

inline void writeLong(long long x, char endc)
{
    ensureOutputCapacity(24);
    if (x < 10)
    {
        obuf[olen++] = (char)('0' + x);
        obuf[olen++] = endc;
        return;
    }
    char buf[24];
    int i = 24;
    while (x >= 100)
    {
        int pos = (int)(x % 100) * 2;
        x /= 100;
        buf[--i] = digit_pairs[pos + 1];
        buf[--i] = digit_pairs[pos];
    }
    if (x < 10)
    {
        buf[--i] = (char)('0' + x);
    }
    else
    {
        int pos = (int)x * 2;
        buf[--i] = digit_pairs[pos + 1];
        buf[--i] = digit_pairs[pos];
    }
    int len = 24 - i;
    memcpy(obuf + olen, buf + i, len);
    olen += len;
    obuf[olen++] = endc;
}

inline void flushOutput()
{
    fwrite(obuf, 1, olen, stdout);
    olen = 0;
}

void approx()
{
    int n = (int)readLong();
    int k = (int)readLong();

    pref_sum[0] = 0;
    pref_xor[0] = 0;

    for (int i = 1; i <= n; i++)
    {
        long long val = readLong();
        pref_sum[i] = pref_sum[i - 1] + val;
        pref_xor[i] = pref_xor[i - 1] ^ val;
    }

    int num_windows = n - k + 1;

    int dq_head = 0, dq_tail = 0;
    int next_add = 1;

    for (int i = 1; i <= n; i++)
    {
        int rf = (num_windows < i) ? num_windows : i;
        while (next_add <= rf)
        {
            long long val = (pref_sum[next_add + k - 1] - pref_sum[next_add - 1]) - (pref_xor[next_add + k - 1] ^ pref_xor[next_add - 1]);
            while (dq_tail > dq_head && dq_val[dq_tail - 1] >= val)
                dq_tail--;
            dq_idx[dq_tail] = next_add;
            dq_val[dq_tail] = val;
            dq_tail++;
            next_add++;
        }
        int lf = (i - k + 1 > 1) ? i - k + 1 : 1;
        while (dq_idx[dq_head] < lf)
            dq_head++;

        writeLong(dq_val[dq_head], (i == n ? '\n' : ' '));
    }
}

int main()
{
    initDigitPairs();
    initInput();
    initOutput(1 << 21);

    int t = (int)readLong();
    while (t--)
        approx();

    flushOutput();
    return 0;
}