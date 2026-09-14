s = input()
s += '**'
num = 0
i = 0

de_s = []

while s[i] != "*":
    if s[i+2] == "#":
        num = s[i: i+2]
        i += 3
    else:
        num = s[i]
        i += 1
    de_s.append(chr(ord('a') + int(num) - 1))
    
print(''.join(de_s))
    