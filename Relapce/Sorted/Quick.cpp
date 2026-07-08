#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &v, int low, int high)
{

    int i = low - 1;
    int p = high;

    for (int j = low; j < high; j++)
    {
        if (v[j] < v[p])
        {
            i++;
            swap(v[i], v[j]);
        }
    }
    swap(v[i + 1], v[high]);
    return i + 1;
}

void quick(vector<int> &v, int low, int high)
{
    if (low < high)
    {
        int pi = partition(v, low, high);
        quick(v, low, pi - 1);
        quick(v, pi + 1, high);
    }
}

void sort(vector<int> &arr)
{
    if (!arr.empty())
    {
        quick(arr, 0, arr.size() - 1);
    }
}

void print_v(vector<int> &v)
{
    for (int x : v)
    {
        cout << x << " ";
    }
    cout << endl;
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

    print_v(v);
    sort(v);
    print_v(v);

    return 1;
}