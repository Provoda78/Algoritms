#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int> &arr, int left, int middle, int right)
{
  int n1 = middle - left + 1;
  int n2 = right - middle;

  vector<int> L(n1), R(n2);

  for (int i = 0; i < n1; i++)
  {
    L[i] = arr[i + left];
  }

  for (int j = 0; j < n2; j++)
  {
    R[j] = arr[middle + 1 + j];
  }

  int i = 0, j = 0;
  int k = left;

  while (i < n1 && j < n2)
  {
    if (L[i] <= R[j])
    {
      arr[k] = L[i];
      i++;
    }
    else
    {
      arr[k] = R[j];
      j++;
    }
    k++;
  }

  while (i < n1)
  {
    arr[k] = L[i];
    i++;
    k++;
  }

  while (j < n2)
  {
    arr[k] = R[j];
    j++;
    k++;
  }
}

void Merge_sort(vector<int> &v, int left, int right)
{
  if (left < right)
  {
    int middle = left + (right - left) / 2;

    Merge_sort(v, left, middle);
    Merge_sort(v, middle + 1, right);

    merge(v, left, middle, right);
  }
}

int main()
{
  vector<int> arr = {38, 27, 43, 3, 9, 82, 10};

  cout << "Исходный массив: ";
  for (int num : arr)
    cout << num << " ";
  cout << endl;

  Merge_sort(arr, 0, arr.size() - 1);

  cout << "Отсортированный массив: ";
  for (int num : arr)
    cout << num << " ";
  cout << endl;

  return 0;
}