import sys


def euclid_div(a, b):
  r = a % abs(b)
  return (a - r) // b


def solve():
  input_text = sys.stdin.read().strip()
  if not input_text:
    return

  formatted_text = input_text.replace('(', ' ( ').replace(')', ' ) ')
  tokens = formatted_text.split()

  pos = 0

  def parse():
    nonlocal pos
    token = tokens[pos]
    pos += 1

    if token == '(':
      op = tokens[pos]
      pos += 1

      left = parse()

      if op == '-':
        if tokens[pos] == ')':
          pos += 1
          return -left
        else:
          right = parse()
          pos += 1
          return left - right

      right = parse()
      pos += 1

      if op == '+':
        return left + right
      elif op == '*':
        return left * right
      elif op == '/':
        return euclid_div(left, right)
    else:
      return int(token)

  print(parse())


if __name__ == '__main__':
  solve()