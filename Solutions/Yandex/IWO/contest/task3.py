import sys

def solve():
    input_d = sys.stdin.read().split()
    if not input_d:
        return

    n = int(input_d[0])
    c = [int(input_d[1]), int(input_d[2]), int(input_d[3])]
    a = input_d[4]
    b = input_d[5]

    char_id = {'D': 0, 'G': 1, 'S': 2}
    id_char = {0: 'D', 1: 'G', 2: 'S'}
    
    options = []
    count_dif = {(0, 1): 0, (0, 2): 0, (1, 2): 0}

    for i in range(n):
        r1 = char_id[a[i]]
        r2 = char_id[b[i]]
        
        opts = []
        for x in range(3): #DGS
            if x != r1 and x != r2:
                opts.append(x)
        
        options.append(opts)
        
        if len(opts) == 1:
            c[opts[0]] -= 1
        else:
            count_dif[(opts[0], opts[1])] += 1

    if c[0] < 0 or c[1] < 0 or c[2] < 0:
        print("-1")
        return
        
    if c[0] > count_dif[(0, 1)] + count_dif[(0, 2)]:
        print("-1")
        return
    if c[1] > count_dif[(0, 1)] + count_dif[(1, 2)]:
        print("-1")
        return
    if c[2] > count_dif[(0, 2)] + count_dif[(1, 2)]:
        print("-1")
        return

    ans = []
    
    for i in range(n):
        opts = options[i]
        if len(opts) == 1:
            ans.append(id_char[opts[0]])
        else:
            x, y = opts[0], opts[1]
            
            choose_x = False
            if c[x] > 0:
                if y == 1:
                    if c[1] <= count_dif[(0, 1)] - 1 + count_dif[(1, 2)]:
                        choose_x = True
                elif y == 2:
                    if x == 0:
                        if c[2] <= count_dif[(0, 2)] - 1 + count_dif[(1, 2)]:
                            choose_x = True
                    else:
                        if c[2] <= count_dif[(0, 2)] + count_dif[(1, 2)] - 1:
                            choose_x = True
            
            if choose_x:
                ans.append(id_char[x])
                c[x] -= 1
                count_dif[(x, y)] -= 1
            else:
                ans.append(id_char[y])
                c[y] -= 1
                count_dif[(x, y)] -= 1

    print("".join(ans))

if __name__ == '__main__':
    solve()