#include <iostream>
#include <map>
#include <string>
#include <utility>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::map<std::string, std::string> data;
    std::string word1, word2;
    std::string key;
    int n;

    for (int i = 0; i < n; i++)
    {
        if (std::cin >> word1 >> word2)
        {
            data[word1] = word2;
            data[word2] = word1;
        }
    }

    std::cin >> key;
    std::cout << data[key];

    return 0;
}