#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int k = 0; k < t; k++)
    {
        int n;
        cin >> n;
        std::vector<std::string> bitmaps(n);

        for (int j = 0; j < n; j++)
        {
            cin >> bitmaps[j];
        }
        for (int i = n - 1; i >= 0; i--)
        {
            for (int j = 0; j < 4; j++)
            {
                if (bitmaps[i][j] == '#')
                {
                    std::cout << j + 1;
                    break;
                }
            }
        }
    }

    return 1;
}