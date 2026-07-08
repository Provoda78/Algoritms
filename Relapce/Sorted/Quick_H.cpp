#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &v, int low, int high)
{

    int p = v[low + (high - low) / 2];

    int l = low - 1;
    int r = high + 1;

    while (true)
    {

        do
        {
            l++;
        } while (v[l] < p);

        do
        {
            r--;
        } while (v[r] > p);

        if (l >= r)
        {
            return r;
        }

        swap(v[l], v[r]);
    }
}

void sort(vector<int> &v, int low, int high)
{
    if (low < high)
    {
        int pi = partition(v, low, high);

        sort(v, low, pi);
        sort(v, pi + 1, high);
    }
}

int main()
{
    vector<int> v = {7, 2, 1, 6, 8, 5, 3, 4};

    sort(v, 0, v.size() - 1);

    for (int x : v)
    {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}