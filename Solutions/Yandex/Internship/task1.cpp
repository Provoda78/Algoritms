#include <iostream>
#include <string>
#include <set>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::set<std::string> unique_words;
    std::string word;

    while (std::cin >> word)
    {
        unique_words.insert(word);
    }

    std::cout << unique_words.size();

    return 0;
}
