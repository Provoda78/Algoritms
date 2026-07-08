#include <iostream>
#include <vector>

using namespace std;

void heapfi(vector<int> &v, int n, int i)
{

    int largest = i;
    int left = i * 2 + 1;
    int right = i * 2 + 2;

    if (left < n && v[largest] < v[left])
    {
        largest = left;
    }

    if (right < n && v[largest] < v[right])
    {
        largest = right;
    }

    if (largest != i)
    {
        swap(v[i], v[largest]);
        heapfi(v, n, largest);
    }
}

void sort(vector<int> &v)
{
    int n = v.size();
    for (int i = n / 2 - 1; i >= 0; i--)
    {
        heapfi(v, n, i);
    }

    for (int i = n - 1; i > 0; i--)
    {
        swap(v[0], v[i]);
        heapfi(v, i, 0);
    }
}

int main()
{
    vector<int> v = {38, 27, 43, 3, 9, 82, 10};

    sort(v);

    for (int x : v)
    {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}