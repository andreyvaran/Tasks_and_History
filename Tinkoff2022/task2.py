from collections import defaultdict
winners = defaultdict(int)

n = int(input())

for i in range(n):
    winners[''.join(sorted(input().split()))] += 1

print(max(winners.values()))