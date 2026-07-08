#include <iostream>
#include <vector>
#include <set>
using namespace std;

void massiv()
{
    int n;
    cin >> n;

    vector<int> v(n + 1);
    for (int i; i < n; i++)
    {
        cin >> v[i];
    }

    vector<bool> used(n + 1, false);

    for (int start = 1; start <= n; start++)
    {
        if (used[start])
            continue;

        vector<int> pos;
        int p = start;
        while (p <= n)
        {
            used[p] = true;
            pos.push_back(v[p]);
            p *= 2;
        }

        set<int> original;
        for (int ps : pos)
        {
            original.insert(v[ps]);
        }

        set<int> targets;
        for (int ps : pos)
        {
            targets.insert(ps);
        }

        if (targets != original)
        {
            cout << "NO\n";
            return;
        }
    }

    cout << "YES\n";
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        massiv();
    }

    return 0;
}
