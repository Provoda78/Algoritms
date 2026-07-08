#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n, t;
    if (!(std::cin >> n >> t))
        return 0;

    std::vector<long long> timeline(t + 2, 0);

    for (int i = 0; i < n; i++)
    {
        int a;
        int f;
        int s;
        std::cin >> a >> f >> s;

        timeline[a] += s;
        timeline[f] -= s;
    }

    long long current_bikes = 0;
    long long max_bikes = 0;

    for (int i = 0; i <= t; ++i)
    {
        current_bikes += timeline[i];
        if (current_bikes > max_bikes)
        {
            max_bikes = current_bikes;
        }
    }

    std::cout << max_bikes << "\n";

    return 0;
}