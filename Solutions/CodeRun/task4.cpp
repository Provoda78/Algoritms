#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <cstdio>

char arrived[10000005];

inline int readInt()
{
    int c = getchar_unlocked();
    while (c <= 32)
    {
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

int main()
{
    int n = readInt();

    int cur_num = 1;
    int cur_backstage = 0;
    int max_backstage = 0;

    for (int i = 0; i < n; i++)
    {
        int num = readInt();

        arrived[num] = 1;
        cur_backstage++;

        while (arrived[cur_num])
        {
            cur_backstage--;
            cur_num++;
            if (cur_num > n)
                break;
        }

        if (cur_backstage > max_backstage)
        {
            max_backstage = cur_backstage;
        }
    }

    writeInt(max_backstage);

    return 0;
}