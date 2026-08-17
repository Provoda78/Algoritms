import sys


def solve():
  input_data = sys.stdin.read().split()
  s = input_data[0] if input_data else ""

  matching = {')': '(', ']': '[', '>': '<', '}': '{'}
  type_map = {'(': 0, '[': 1, '<': 2, '{': 3}
  max_dist = [-1, -1, -1, -1]

  stack = []

  for i, char in enumerate(s):
    if char in type_map:
      stack.append((char, i))
    elif char in matching:
      if not stack or stack[-1][0] != matching[char]:
        print("incorrect")
        return

      open_char, open_idx = stack.pop()
      b_type = type_map[open_char]

      dist = i - open_idx - 1

      if dist > max_dist[b_type]:
        max_dist[b_type] = dist
    else:
      print("incorrect")
      return

  if stack:
    print("incorrect")
    return

  print(*max_dist)


if __name__ == "__main__":
  solve()