import sys
from collections import deque

def main():
    input_ = sys.stdin.read().splitlines()
    if not input_:
        return

    n = int(input_[0])
    queue = deque()
    
    idx_ = 1
    for _ in range(n):
        name, len_ = input_[idx_].split()
        queue.append((name, int(len_)))
        idx_ += 1

    m = int(input_[idx_])
    idx_ += 1
    
    events = []
    for _ in range(m):
        parts = input_[idx_].split()
        t = int(parts[0])
        name = parts[1]
        len_ = int(parts[2])
        events.append((t, name, len_))
        idx_ += 1

    current_time = 0
    event_idx = 0
    res = []

    while queue or event_idx < m:
        if not queue and event_idx < m:
            current_time = max(current_time, events[event_idx][0])

        while event_idx < m and events[event_idx][0] <= current_time:
            t, name, len_ = events[event_idx]
            queue.appendleft((name, len_))
            event_idx += 1

        if queue:
            current_name, current_len = queue.popleft()
            res.append(f"{current_name} {current_time}")
            
            end_time = current_time + current_len
            

            while event_idx < m and events[event_idx][0] <= end_time:
                t, name, len_ = events[event_idx]
                queue.appendleft((name, len_))
                event_idx += 1
                
            current_time = end_time

    print('\n'.join(res))

if __name__ == '__main__':
    main()