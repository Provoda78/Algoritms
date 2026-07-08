#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    if (!(std::cin >> n))
        return 0;

    std::priority_queue<int, std::vector<int>, std::greater<int>> group_heap;

    int next_expected = 1;
    int max_len = 0;

    for (int i = 0; i < n; i++)
    {
        int num;
        std::cin >> num;

        group_heap.push(num);

        int cur_len = group_heap.size();
        if (cur_len > max_len)
        {
            max_len = cur_len;
        }

        while (!group_heap.empty() && group_heap.top() == next_expected)
        {
            group_heap.pop();
            next_expected++;
        }
    }

    std::cout << max_len - 1 << "\n";

    return 0;
}