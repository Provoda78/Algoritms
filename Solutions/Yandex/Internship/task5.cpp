#include <iostream>
#include <vector>
#include <algorithm>

struct Event
{
    int data;
    int type;
    int id;
    Event(int data, int type, int id = -1) : data(data), type(type), id(id) {}
};

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::vector<Event> timeline;
    int n, m;
    if (!(std::cin >> n >> m))
        return 0;

    for (int i = 0; i < n; i++)
    {
        int start, end;
        if (std::cin >> start >> end)
        {
            if (start > end)
                std::swap(start, end);

            timeline.push_back(Event(start, -1));
            timeline.push_back(Event(end, 1));
        }
    }

    for (int i = 0; i < m; i++)
    {
        int point;
        if (std::cin >> point)
        {
            timeline.push_back(Event(point, 0, i));
        }
    }

    std::sort(timeline.begin(), timeline.end(), [](const Event &a, const Event &b)
              {
        if (a.data != b.data) return a.data < b.data;
        return a.type < b.type; });

    int active_segments = 0;
    std::vector<int> ans(m);

    for (const auto &event : timeline)
    {
        if (event.type == 0)
        {
            ans[event.id] = active_segments;
        }
        else
        {
            active_segments -= event.type;
        }
    }

    for (int i = 0; i < m; i++)
    {
        std::cout << ans[i] << (i == m - 1 ? "" : " ");
    }

    std::cout << "\n";
    return 0;
}