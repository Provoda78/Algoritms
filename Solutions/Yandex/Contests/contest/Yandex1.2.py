n = int(input())
oligarhi = list(map(int, input().split()))

new_sum = oligarhi[0]
last_winner = n
last_loser = 0

losers_winners = []

if n == 1:
    print(n)

for i in range(1, n-1):
    new_sum += oligarhi[i]
    if oligarhi[i-1] < oligarhi[i] and new_sum > oligarhi[i+1]:
        if last_winner == n:
            last_winner = i
    if oligarhi[i+1] >= new_sum:
        last_loser = i
    
garde = max(last_winner, last_loser+1)
    
losers_winners = [0] * garde + [1] * (n-garde) 

if oligarhi[n-1]>oligarhi[n-2]:
    losers_winners[n-1] = 1
    
for i in losers_winners:
    print(i)