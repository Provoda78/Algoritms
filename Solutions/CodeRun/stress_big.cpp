#include <bits/stdc++.h>
using namespace std;

mt19937 rng(
    chrono::steady_clock::now()
        .time_since_epoch()
        .count());

int rnd(int l, int r)
{
    return uniform_int_distribution<int>(l, r)(rng);
}

struct Test
{
    int n;
    vector<array<int, 3>> p;
};

Test make_clusters()
{
    Test t;

    int clusters = rnd(5, 20);
    int per = rnd(2000, 5000);

    t.n = clusters * per;

    for (int c = 0; c < clusters; c++)
    {
        int cx = rnd(0, 100000000);
        int cy = rnd(0, 100000000);

        for (int i = 0; i < per; i++)
        {
            int x = cx + rnd(-50, 50);
            int y = cy + rnd(-50, 50);

            int r = rnd(80, 150);

            t.p.push_back({x, y, r});
        }
    }

    return t;
}

Test make_line()
{
    Test t;

    t.n = 100000;

    t.p.reserve(t.n);

    for (int i = 0; i < t.n; i++)
    {
        t.p.push_back({i * 100,
                       i * 100,
                       rnd(0, 300)});
    }

    return t;
}

Test make_same_points()
{
    Test t;

    t.n = 100000;

    t.p.reserve(t.n);

    for (int i = 0; i < t.n; i++)
    {
        t.p.push_back({500000,
                       500000,
                       rnd(0, 10)});
    }

    return t;
}

Test make_sparse()
{
    Test t;

    t.n = 100000;

    t.p.reserve(t.n);

    for (int i = 0; i < t.n; i++)
    {
        t.p.push_back({rnd(0, 1000000000),
                       rnd(0, 1000000000),
                       0});
    }

    return t;
}

int main()
{
    vector<Test (*)(void)> gens =
        {
            make_clusters,
            make_line,
            make_same_points,
            make_sparse};

    for (int test = 1;; test++)
    {
        auto gen = gens[rnd(0, (int)gens.size() - 1)];

        Test t = gen();

        ofstream out("input.txt");

        out << 1 << "\n";
        out << t.n << "\n";

        for (auto [x, y, r] : t.p)
        {
            out << x << " "
                << y << " "
                << r << "\n";
        }

        out.close();

        auto start =
            chrono::steady_clock::now();

        int code = system(
            "./fast < input.txt > fast.out");

        auto finish =
            chrono::steady_clock::now();

        if (code != 0)
        {
            cout << "CRASH\n";
            return 0;
        }

        long long ms =
            chrono::duration_cast<
                chrono::milliseconds>(finish - start)
                .count();

        cout
            << "Test "
            << test
            << " n="
            << t.n
            << " time="
            << ms
            << " ms\n";

        if (ms > 300)
        {
            cout << "SLOW TEST SAVED\n";
            return 0;
        }

        cout << "saved input.txt\n";
    }
}