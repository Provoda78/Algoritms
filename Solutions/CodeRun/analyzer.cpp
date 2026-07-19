#include <bits/stdc++.h>
using namespace std;

struct DSU
{
    vector<int> p;

    DSU(int n) : p(n + 1)
    {
        iota(p.begin(), p.end(), 0);
    }

    int find(int x)
    {
        return p[x] == x ? x : p[x] = find(p[x]);
    }

    void unite(int a, int b)
    {
        a = find(a);
        b = find(b);

        if (a != b)
            p[a] = b;
    }
};

long long dist(
    long long x1,
    long long y1,
    long long x2,
    long long y2)
{
    return llabs(x1 - x2) + llabs(y1 - y2);
}

int main()
{
    freopen("input.txt", "r", stdin);

    int T;
    cin >> T;

    while (T--)
    {
        int n;
        cin >> n;

        vector<long long> x(n + 1), y(n + 1), r(n + 1);

        for (int i = 1; i <= n; i++)
            cin >> x[i] >> y[i] >> r[i];

        DSU dsu(n);

        long long zones = 0;

        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                if (dist(x[i], y[i], x[j], y[j]) <= r[i])
                {
                    zones++;
                    dsu.unite(i, j);
                }
            }
        }

        map<int, int> cnt;

        for (int i = 1; i <= n; i++)
            cnt[dsu.find(i)]++;

        vector<int> sizes;

        for (auto [a, b] : cnt)
            sizes.push_back(b);

        sort(
            sizes.rbegin(),
            sizes.rend());

        cout << "n = " << n << "\n";
        cout << "components = " << sizes.size() << "\n";
        cout << "zones = " << zones << "\n";

        cout << "largest components:\n";

        for (int i = 0; i < min(20, (int)sizes.size()); i++)
            cout << sizes[i] << " ";

        cout << "\n";
    }
}