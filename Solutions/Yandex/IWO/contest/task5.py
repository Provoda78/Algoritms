import sys
from heapq import heappush, heappop, heapify

def solve():
    input_d = sys.stdin.read().split()
    p, u = int(input_d[0]), int(input_d[1])
    mask = (1 << 14) - 1

    def ip2int(s):
        a, b, c, d = s.split('.')
        return (int(a) << 24) | (int(b) << 16) | (int(c) << 8) | int(d)

    free = []
    nets = {}
    for i in range(p):
        cidr, n = input_d[2 + i].split(',')
        addr, l = cidr.split('/')
        
        l = int(l)
        net = ip2int(addr) >> (32 - l)
        d = nets.setdefault(l, {})
        sid = d.get(net)
        
        if sid is None:
            sid = len(free)
            d[net] = sid
            free.append(0)
            
        free[sid] += int(n)
        
    levels = sorted(nets.items())
    m = len(free)

    names, starts_of, ends, keys, servers = [], [], [], [], []
    for i in range(u):
        name, st, en = input_d[2 + p + i].split(',')
        ip = ip2int(name)
        names.append(name)
        starts_of.append(int(st))
        ends.append(int(en))
        keys.append((ip << 14) | i)
        
        lst = []
        for l, d in levels:
            sid = d.get(ip >> (32 - l))
            if sid is not None:
                lst.append(sid)
        servers.append(lst)

    t_max = max(ends)
    starts = [[] for _ in range(t_max + 2)]
    for i in range(u):
        starts[starts_of[i]].append(i)

    release = [[] for _ in range(t_max + 2)]
    wait = [[] for _ in range(m)]
    done = [False] * u
    subscribed = [False] * u

    def b_waiter(s, t):
        h = wait[s]
        while h and (done[h[0] & mask] or ends[h[0] & mask] < t):
            heappop(h)
        return h[0] if h else -1

    for t in range(1, t_max + 1):
        cand = [keys[i] for i in starts[t]]
        heapify(cand)
        
        freed = set()
        for s in release[t]:
            free[s] += 1
            freed.add(s)
            
        for s in freed:
            k = b_waiter(s, t)
            if k >= 0:
                heappush(cand, k)

        while cand:
            k = heappop(cand)
            i = k & mask
            
            if done[i]:
                continue
            
            for s in servers[i]:
                if free[s] > 0:
                    free[s] -= 1
                    done[i] = True
                    release[ends[i] + 1].append(s)
                    break
                
            if done[i]:
                for s in servers[i]:

                    if free[s] > 0:
                        k2 = b_waiter(s, t)
                        
                        if k2 >= 0:
                            heappush(cand, k2)
                            
            elif not subscribed[i] and ends[i] > t:
                subscribed[i] = True

                for s in servers[i]:
                    heappush(wait[s], k)

    sys.stdout.write("\n".join(
        names[i] + (" SUCCESS" if done[i] else " REJECT") for i in range(u)) + "\n")


if __name__ == '__main__':
    solve()
