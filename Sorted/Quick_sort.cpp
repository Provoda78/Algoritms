#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int> &v, int low, int high)
{
    int pivot = v[high];
    int i = low - 1;

    for (int j = low; j <= high; j++)
    {
        if (v[j] < pivot)
        {
            i++;
            swap(v[i], v[j]);
        }
    }

    swap(v[i + 1], v[high]);
    return i + 1;
}

void Quick_sort(vector<int> &v, int low, int high)
{
    if (low < high)
    {
        int pivot = partition(v, low, high);

        Quick_sort(v, low, pivot - 1);
        Quick_sort(v, pivot + 1, high);
    }
}

void sort(vector<int> &arr)
{
    if (!arr.empty())
    {
        Quick_sort(arr, 0, arr.size() - 1);
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