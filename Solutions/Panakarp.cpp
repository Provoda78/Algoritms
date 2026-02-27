#include <iostream>
#include <vector>

using namespace std;

vector<int> counter(int x)
{
    int count3 = 0;
    int num = x;

    while (num % 3 == 0)
    {
        count3++;
        num /= 3;
    }

    int count2 = 0;
    num = x;

    while (num % 2 == 0)
    {
        count2++;
        num /= 2;
    }

    return {count3 * (-1), count2};
}

int main()
{
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }

    return 1;
}