#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int k;
        cin >> k;
        const int target = k - 2;
        std::vector<int> v(k);
        std::unordered_map<int, int> mp;
        for (int i = 0; i < k; i++)
        {
            cin >> v[i];
            mp[v[i]]++;
        }

        for (int i = 0; i < k; i++)
        {
            int n = v[i];
            if (target % n == 0)
            {
                int m = target / n;
                if (mp.count(m))
                {
                    if (m == n && mp[n] < 2)
                    {
                        continue;
                    }
                    cout << n << " " << m << endl;
                    break;
                }
            }
        }
    }

    return 1;
}