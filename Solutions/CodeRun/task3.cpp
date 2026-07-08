#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    if (!(std::cin >> n))
        return 0;

    std::vector<bool> arrived(n + 1, false);

    int cur_num = 1;
    int cur_backstage = 0;
    int max_backstage = 0;

    for (int i = 0; i < n; i++)
    {
        int num;
        std::cin >> num;

        arrived[num] = true;
        cur_backstage++;

        if (cur_backstage > max_backstage)
        {
            max_backstage = cur_backstage;
        }

        while (cur_num <= n && arrived[cur_num])
        {
            cur_backstage--;
            cur_num++;
        }
    }

    std::cout << max_backstage << "\n";

    return 0;
}