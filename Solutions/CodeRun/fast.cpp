#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

const int MAXN = 200005;
const int MAX_EDGES = 8000005;
const long long INF = 4e18;

inline long long abs_diff(long long a, long long b)
{
    return a > b ? a - b : b - a;
}

struct Point
{
    int id;
    long long x, y, r, u, v;
};

Point pts[MAXN];

int edge_u[MAX_EDGES];
int edge_v[MAX_EDGES];
long long edge_w[MAX_EDGES];
int edge_idx[MAX_EDGES];
int edge_tmp[MAX_EDGES];
int edge_cnt = 0;

int count_bucket[256];

inline void add_edge(int u, int v, long long w)
{
    if (edge_cnt >= MAX_EDGES)
        return;
    edge_u[edge_cnt] = u;
    edge_v[edge_cnt] = v;
    edge_w[edge_cnt] = w;
    edge_idx[edge_cnt] = edge_cnt;
    edge_cnt++;
}

int parent_req[MAXN];
int parent_final[MAXN];

int find_req(int i)
{
    return (parent_req[i] == i) ? i : (parent_req[i] = find_req(parent_req[i]));
}

bool unite_req(int i, int j)
{
    int root_i = find_req(i);
    int root_j = find_req(j);
    if (root_i != root_j)
    {
        parent_req[root_i] = root_j;
        return true;
    }
    return false;
}

int find_final(int i)
{
    return (parent_final[i] == i) ? i : (parent_final[i] = find_final(parent_final[i]));
}

bool unite_final(int i, int j)
{
    int root_i = find_final(i);
    int root_j = find_final(j);
    if (root_i != root_j)
    {
        parent_final[root_i] = root_j;
        return true;
    }
    return false;
}

inline long long readLong()
{
    long long res = 0;
    int c = getchar_unlocked();
    bool neg = false;
    while (c < '0' || c > '9')
    {
        if (c == EOF)
            return -1;
        if (c == '-')
            neg = true;
        c = getchar_unlocked();
    }
    while (c >= '0' && c <= '9')
    {
        res = res * 10 + (c - '0');
        c = getchar_unlocked();
    }
    return neg ? -res : res;
}

inline void writeLong(long long x)
{
    if (x == 0)
    {
        putchar_unlocked('0');
        return;
    }
    char s[20];
    int i = 0;
    while (x)
    {
        s[i++] = (x % 10) + '0';
        x /= 10;
    }
    while (--i >= 0)
        putchar_unlocked(s[i]);
}

inline void writeInt(int x)
{
    if (x == 0)
    {
        putchar_unlocked('0');
        return;
    }
    char s[12];
    int i = 0;
    while (x)
    {
        s[i++] = (x % 10) + '0';
        x /= 10;
    }
    while (--i >= 0)
        putchar_unlocked(s[i]);
}

int kd_p_indices[MAXN];
int kd_left[MAXN], kd_right[MAXN], kd_pid[MAXN];
long long kd_min_u[MAXN], kd_max_u[MAXN], kd_min_v[MAXN], kd_max_v[MAXN];
int kd_cnt = 0;

int build_kd(int l, int r, int depth)
{
    if (l > r)
        return -1;
    int mid = l + (r - l) / 2;
    nth_element(kd_p_indices + l, kd_p_indices + mid, kd_p_indices + r + 1, [&](int a, int b)
                { return (depth % 2 == 0) ? pts[a].u < pts[b].u : pts[a].v < pts[b].v; });

    int idx = kd_cnt++;
    int p = kd_p_indices[mid];
    kd_pid[idx] = p;

    kd_left[idx] = build_kd(l, mid - 1, depth + 1);
    kd_right[idx] = build_kd(mid + 1, r, depth + 1);

    kd_min_u[idx] = kd_max_u[idx] = pts[p].u;
    kd_min_v[idx] = kd_max_v[idx] = pts[p].v;

    int lc = kd_left[idx], rc = kd_right[idx];
    if (lc != -1)
    {
        kd_min_u[idx] = min(kd_min_u[idx], kd_min_u[lc]);
        kd_max_u[idx] = max(kd_max_u[idx], kd_max_u[lc]);
        kd_min_v[idx] = min(kd_min_v[idx], kd_min_v[lc]);
        kd_max_v[idx] = max(kd_max_v[idx], kd_max_v[lc]);
    }
    if (rc != -1)
    {
        kd_min_u[idx] = min(kd_min_u[idx], kd_min_u[rc]);
        kd_max_u[idx] = max(kd_max_u[idx], kd_max_u[rc]);
        kd_min_v[idx] = min(kd_min_v[idx], kd_min_v[rc]);
        kd_max_v[idx] = max(kd_max_v[idx], kd_max_v[rc]);
    }
    return idx;
}

void query_kd(int idx, long long q_min_u, long long q_max_u, long long q_min_v, long long q_max_v, int tid)
{
    if (idx == -1)
        return;
    if (kd_min_u[idx] > q_max_u || kd_max_u[idx] < q_min_u ||
        kd_min_v[idx] > q_max_v || kd_max_v[idx] < q_min_v)
        return;

    int p = kd_pid[idx];
    if (pts[p].u >= q_min_u && pts[p].u <= q_max_u && pts[p].v >= q_min_v && pts[p].v <= q_max_v)
    {
        add_edge(tid, pts[p].id, abs_diff(pts[tid].x, pts[p].x) + abs_diff(pts[tid].y, pts[p].y));
    }

    query_kd(kd_left[idx], q_min_u, q_max_u, q_min_v, q_max_v, tid);
    query_kd(kd_right[idx], q_min_u, q_max_u, q_min_v, q_max_v, tid);
}

struct TempPoint
{
    int id;
    long long x, y;
};
TempPoint sub_pts[MAXN];
TempPoint sp[MAXN];

TempPoint mst_tmp[MAXN];

long long coords[MAXN];
long long bit_val[MAXN];
int bit_id[MAXN];
int bit_n;

void init_bit(int n_)
{
    bit_n = n_;
    for (int i = 1; i <= n_; ++i)
    {
        bit_val[i] = INF;
        bit_id[i] = -1;
    }
}

void update_bit(int i, long long v, int idx)
{
    for (; i <= bit_n; i += i & -i)
    {
        if (v < bit_val[i])
        {
            bit_val[i] = v;
            bit_id[i] = idx;
        }
    }
}

pair<long long, int> query_bit(int i)
{
    long long m = INF;
    int mid = -1;
    for (; i > 0; i -= i & -i)
    {
        if (bit_val[i] < m)
        {
            m = bit_val[i];
            mid = bit_id[i];
        }
    }
    return {m, mid};
}

void find_mst_edges(int m)
{
    if (m <= 1)
        return;

    if (m <= 80)
    {
        for (int i = 0; i < m; ++i)
        {
            for (int j = i + 1; j < m; ++j)
            {
                int u = sub_pts[i].id;
                int v = sub_pts[j].id;

                add_edge(
                    u,
                    v,
                    abs_diff(sub_pts[i].x, sub_pts[j].x) +
                        abs_diff(sub_pts[i].y, sub_pts[j].y));
            }
        }
        return;
    }

    for (int dir = 0; dir < 4; ++dir)
    {
        for (int j = 0; j < m; ++j)
        {
            long long x = sub_pts[j].x;
            long long y = sub_pts[j].y;

            if (dir == 1)
            {
                y = -y;
            }
            else if (dir == 2)
            {
                swap(x, y);
            }
            else if (dir == 3)
            {
                swap(x, y);
                y = -y;
            }

            mst_tmp[j] = {sub_pts[j].id, x, y};
        }

        sort(
            mst_tmp,
            mst_tmp + m,
            [](const TempPoint &a, const TempPoint &b)
            {
                if (a.x != b.x)
                    return a.x < b.x;
                return a.y < b.y;
            });

        for (int j = 0; j < m; ++j)
            coords[j] = mst_tmp[j].y - mst_tmp[j].x;

        sort(coords, coords + m);

        int unique_sz = 0;
        for (int j = 0; j < m; ++j)
        {
            if (j == 0 || coords[j] != coords[j - 1])
                coords[unique_sz++] = coords[j];
        }

        init_bit(unique_sz);

        for (int j = 0; j < m; ++j)
        {
            long long val = mst_tmp[j].y - mst_tmp[j].x;

            mst_tmp[j].id =
                mst_tmp[j].id;
        }

        for (int j = m - 1; j >= 0; --j)
        {
            long long val = mst_tmp[j].y - mst_tmp[j].x;

            int pos =
                lower_bound(
                    coords,
                    coords + unique_sz,
                    val) -
                coords + 1;

            int q_pos = unique_sz - pos + 1;

            auto res = query_bit(q_pos);

            if (res.second != -1)
            {
                int u = mst_tmp[j].id;
                int v = res.second;

                add_edge(
                    u,
                    v,
                    abs_diff(pts[u].x, pts[v].x) +
                        abs_diff(pts[u].y, pts[v].y));
            }

            update_bit(
                q_pos,
                mst_tmp[j].x + mst_tmp[j].y,
                mst_tmp[j].id);
        }
    }
}

void radix_sort_edges()
{
    int n_e = edge_cnt;
    for (int shift = 0; shift < 40; shift += 8)
    {
        for (int i = 0; i < 256; ++i)
            count_bucket[i] = 0;
        for (int i = 0; i < n_e; ++i)
        {
            int byte_val = (edge_w[edge_idx[i]] >> shift) & 0xFF;
            count_bucket[byte_val]++;
        }
        int sum = 0;
        for (int i = 0; i < 256; ++i)
        {
            int temp = count_bucket[i];
            count_bucket[i] = sum;
            sum += temp;
        }
        for (int i = 0; i < n_e; ++i)
        {
            int byte_val = (edge_w[edge_idx[i]] >> shift) & 0xFF;
            edge_tmp[count_bucket[byte_val]++] = edge_idx[i];
        }
        for (int i = 0; i < n_e; ++i)
        {
            edge_idx[i] = edge_tmp[i];
        }
    }
}

int comp_head[MAXN];
int comp_next[MAXN];
int res_u[MAXN], res_v[MAXN];

void solve()
{
    long long n = readLong();
    if (n <= 0)
        return;

    edge_cnt = 0;
    kd_cnt = 0;
    for (int i = 1; i <= n; ++i)
    {
        parent_req[i] = i;
        parent_final[i] = i;
        comp_head[i] = -1;
    }

    for (int i = 1; i <= n; ++i)
    {
        long long x = readLong(), y = readLong(), r = readLong();
        pts[i] = {i, x, y, r, x + y, x - y};
        kd_p_indices[i - 1] = i;
    }

    int root = build_kd(0, n - 1, 0);

    for (int i = 1; i <= n; ++i)
    {
        query_kd(root, pts[i].u - pts[i].r, pts[i].u + pts[i].r,
                 pts[i].v - pts[i].r, pts[i].v + pts[i].r, pts[i].id);
    }

    int kd_edges_count = edge_cnt;

    for (int i = 0; i < kd_edges_count; ++i)
    {
        unite_req(edge_u[i], edge_v[i]);
    }

    edge_cnt = 0;

    for (int i = 1; i <= n; ++i)
    {
        int root_id = find_req(i);
        comp_next[i] = comp_head[root_id];
        comp_head[root_id] = i;
    }

    for (int i = 1; i <= n; ++i)
    {
        if (comp_head[i] != -1)
        {
            int curr = comp_head[i];
            int m = 0;
            while (curr != -1)
            {
                sub_pts[m++] = {pts[curr].id, pts[curr].x, pts[curr].y};
                curr = comp_next[curr];
            }
            find_mst_edges(m);
        }
    }

    radix_sort_edges();

    long long cost = 0;
    int res_cnt = 0;

    for (int i = 0; i < edge_cnt; ++i)
    {
        int idx = edge_idx[i];

        int u = edge_u[idx];
        int v = edge_v[idx];

        if (unite_final(u, v))
        {
            cost += edge_w[idx];
            res_u[res_cnt] = u;
            res_v[res_cnt] = v;
            res_cnt++;
        }
    }

    writeLong(cost);
    putchar_unlocked('\n');
    writeInt(res_cnt);
    putchar_unlocked('\n');
    for (int i = 0; i < res_cnt; ++i)
    {
        writeInt(res_u[i]);
        putchar_unlocked(' ');
        writeInt(res_v[i]);
        putchar_unlocked('\n');
    }
}

int main()
{
    int t = readLong();
    if (t <= 0)
        return 0;
    while (t--)
    {
        solve();
    }
    return 0;
}