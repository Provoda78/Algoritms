#include <iostream>
#include <vector>

using namespace std;

// Концептуальная схема Timsort
void timSort(vector<int> &arr)
{
    int n = arr.size();
    int minRun = calculateMinRun(n); // Обычно 32-64

    // 1. Сортируем отдельные куски вставками
    for (int i = 0; i < n; i += minRun)
        insertionSort(arr, i, min(i + minRun - 1, n - 1));

    // 2. Сливаем куски (размером 32, затем 64, 128...)
    for (int size = minRun; size < n; size = 2 * size)
    {
        for (int left = 0; left < n; left += 2 * size)
        {
            int mid = left + size - 1;
            int right = min((left + 2 * size - 1), (n - 1));
            if (mid < right)
                merge(arr, left, mid, right);
        }
    }
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

    timSort(v);

    for (auto x : v)
    {
        cout << x;
    }

    return 1;
}