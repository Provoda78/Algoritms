#include <bits/stdc++.h>
using namespace std;

mt19937 rng((uint32_t)chrono::steady_clock::now().time_since_epoch().count());

int rnd(int l, int r)
{
    return uniform_int_distribution<int>(l, r)(rng);
}

int main()
{
    int n = 100000;

    for (int i = 0; i < n; i++)
    {
        int x, y;

        if (rnd(0, 100) < 30)
        {
            x = 500000;
            y = 500000;
        }
        else
        {
            x = rnd(0, 1000000);
            y = rnd(0, 1000000);
        }

        int r = rnd(0, 10);

        cout << x << " " << y << " " << r << "\n";
    }
}