#include <iostream>
#include <vector>
#include <deque>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n, k;
    if (!(std::cin >> n >> k))
        return 0;

    std::vector<int> a(n);
    for (int i = 0; i < n; ++i)
    {
        std::cin >> a[i];
    }

    std::deque<int> dq;

    for (int i = 0; i < n; ++i)
    {
        if (!dq.empty() && dq.front() <= i - k)
        {
            dq.pop_front();
        }

        while (!dq.empty() && a[dq.back()] >= a[i])
        {
            dq.pop_back();
        }

        dq.push_back(i);

        if (i >= k - 1)
        {
            std::cout << a[dq.front()] << "\n";
        }
    }

    return 0;
}