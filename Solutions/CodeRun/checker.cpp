#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct Point
{
    ll x, y, r;
};

struct Edge
{
    int u, v;
    ll w;

    bool operator<(const Edge &other) const
    {
        return w < other.w;
    }
};

struct DSU
{
    vector<int> p;

    DSU(int n = 0)
    {
        p.resize(n + 1);
        iota(p.begin(), p.end(), 0);
    }

    int find(int x)
    {
        return p[x] == x ? x : p[x] = find(p[x]);
    }

    bool unite(int a, int b)
    {
        a = find(a);
        b = find(b);

        if (a == b)
            return false;

        p[a] = b;
        return true;
    }
};

ll dist(const Point &a, const Point &b)
{
    return llabs(a.x - b.x) + llabs(a.y - b.y);
}

// проверка требований задачи
bool valid(
    int n,
    vector<Point> &p,
    vector<pair<int, int>> &edges)
{
    DSU dsu(n);

    for (auto [a, b] : edges)
    {
        if (!dsu.unite(a, b))
            return false; // цикл
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (dist(p[i], p[j]) <= p[i].r)
            {
                if (dsu.find(i) != dsu.find(j))
                    return false;
            }
        }
    }

    return true;
}

ll optimum(
    int n,
    vector<Point> &p)
{
    // 1. Находим обязательные компоненты

    DSU req(n);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (dist(p[i], p[j]) <= p[i].r)
            {
                req.unite(i, j);
            }
        }
    }

    vector<vector<int>> comp(n + 1);

    for (int i = 1; i <= n; i++)
    {
        comp[req.find(i)].push_back(i);
    }

    ll ans = 0;

    // 2. Для каждой компоненты обычный MST

    for (auto &c : comp)
    {
        int m = c.size();

        if (m <= 1)
            continue;

        vector<Edge> edges;

        for (int i = 0; i < m; i++)
        {
            for (int j = i + 1; j < m; j++)
            {
                int u = c[i];
                int v = c[j];

                edges.push_back({u,
                                 v,
                                 dist(p[u], p[v])});
            }
        }

        sort(
            edges.begin(),
            edges.end());

        DSU dsu(n);

        int cnt = 0;

        for (auto &e : edges)
        {
            if (dsu.unite(e.u, e.v))
            {
                ans += e.w;
                cnt++;

                if (cnt == m - 1)
                    break;
            }
        }
    }

    return ans;
}

int main()
{
    string fast = "fast.out";

    ifstream in("input.txt");

    int T;
    in >> T;

    for (int tc = 1; tc <= T; tc++)
    {
        int n;
        in >> n;

        vector<Point> p(n + 1);

        for (int i = 1; i <= n; i++)
        {
            in >> p[i].x >> p[i].y >> p[i].r;
        }

        ifstream out(fast);

        ll answer;
        int m;

        out >> answer;
        out >> m;

        vector<pair<int, int>> edges;

        ll real_cost = 0;

        for (int i = 0; i < m; i++)
        {
            int a, b;
            out >> a >> b;

            edges.push_back({a, b});

            real_cost += dist(p[a], p[b]);
        }

        // проверка стоимости
        if (real_cost != answer)
        {
            cout << "Wrong cost\n";
            cout << "Test " << tc << "\n";
            return 0;
        }

        // проверка структуры
        if (!valid(n, p, edges))
        {
            cout << "Invalid solution\n";
            cout << "Test " << tc << "\n";
            return 0;
        }

        // оптимальность только для маленьких
        if (n <= 8)
        {
            ll opt = optimum(n, p);

            if (opt != answer)
            {
                cout << "Not optimal\n";
                cout << "Test " << tc << "\n";
                cout << "fast = " << answer << "\n";
                cout << "opt  = " << opt << "\n";
                return 0;
            }
        }

        cout << "OK " << tc << "\n";
    }
}