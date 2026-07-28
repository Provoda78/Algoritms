#include <iostream>
#include <string>

void generate(int n, int left, int right, std::string path)
{
    if (left + right == 2 * n)
    {
        std::cout << path << '\n';
        return;
    }

    if (left < n)
    {
        path.push_back('(');
        generate(n, left + 1, right, path);
        path.pop_back();
    }

    if (right < n && right < left)
    {
        path.push_back(')');
        generate(n, left, right + 1, path);
        path.pop_back();
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    if (std::cin >> n)
    {
        std::string path = "";
        generate(n, 0, 0, path);
    }

    return 0;
}