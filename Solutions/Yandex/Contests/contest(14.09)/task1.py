import sys

def solve_for_one(sequence):
    res = []
    len_ = 0
    for char in sequence:
        if char == '#':
            len_ += 1
        else:
            if len_ > 0:
                res.append(len_)
                len_ = 0
    if len_ > 0:
        res.append(len_)
    
    if not res:
        return "0"
    else:
        return f"{len(res)} " + " ".join(map(str, res))


def main():
    input_ = sys.stdin.read().splitlines()
    if not input_:
        return
    
    n, m = map(int, input_[0].split())
    grid = input_[1:n+1]
    
    for i in range(n):
        row = grid[i]
        print(solve_for_one(row))
        
    print()
    
    for j in range(m):
        col = [grid[i][j] for i in range(n)]
        print(solve_for_one(col))


if __name__ == '__main__':
    main()