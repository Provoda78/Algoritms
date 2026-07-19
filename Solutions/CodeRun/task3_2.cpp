#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <cstdio>
#include <cstdint>

static unsigned char present[10000005];

static char buffer[1 << 22];
static char *ptr = buffer;
static char *endPtr = buffer;

inline void refill()
{
    size_t sz = fread(buffer, 1, sizeof(buffer), stdin);
    ptr = buffer;
    endPtr = buffer + sz;
}

inline uint32_t readInt()
{
    while (ptr >= endPtr)
        refill();

    while (*ptr <= ' ')
    {
        ++ptr;
        if (ptr >= endPtr)
            refill();
    }

    uint32_t x = 0;

    while (*ptr >= '0')
    {
        x = x * 10u + uint32_t(*ptr - '0');
        ++ptr;

        if (ptr >= endPtr)
            refill();
    }

    return x;
}

inline void writeUInt(uint32_t x)
{
    char out[12];
    int len = 0;

    do
    {
        out[len++] = char('0' + x % 10);
        x /= 10;
    } while (x);

    while (len--)
        putchar_unlocked(out[len]);

    putchar_unlocked('\n');
}

int main()
{
    uint32_t n = readInt();

    uint32_t next = 1;
    uint32_t waiting = 0;
    uint32_t answer = 0;

    for (uint32_t i = 0; i < n; i++)
    {
        uint32_t x = readInt();

        present[x] = 1;
        ++waiting;

        while (next <= n && present[next])
        {
            present[next] = 0;
            --waiting;
            ++next;
        }

        if (waiting > answer)
            answer = waiting;
    }

    writeUInt(answer);

    return 0;
}