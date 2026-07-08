#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

struct Record
{
    int id;
    int score;
};

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int m;
    if (!(std::cin >> m))
        return 0;

    std::vector<Record> all_records;
    all_records.reserve(5000005);

    for (int i = 0; i < m; ++i)
    {
        int l;
        std::cin >> l;
        for (int j = 0; j < l; ++j)
        {
            int k, v;
            std::cin >> k >> v;
            all_records.push_back({k, v});
        }
    }

    std::unordered_map<int, int> unique_scores;
    unique_scores.reserve(5000005);

    for (int i = (int)all_records.size() - 1; i >= 0; --i)
    {
        unique_scores.emplace(all_records[i].id, all_records[i].score);
    }

    std::vector<Record> result;
    result.reserve(unique_scores.size());
    for (const auto &[id, score] : unique_scores)
    {
        result.push_back({id, score});
    }

    std::sort(result.begin(), result.end(), [](const Record &a, const Record &b)
              { return a.id < b.id; });

    for (const auto &rec : result)
    {
        std::cout << rec.id << " " << rec.score << "\n";
    }

    return 0;
}