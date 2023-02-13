import itertools

N, M = map(int, input().split())
sets = []
numbers = set(list(range(1,N+1)))
ans = 0

for i in range(M):
    C = int(input())
    s = list(map(int, input().split()))
    sets.append(s)

for i in range(M):
    for team in itertools.combinations(sets, i+1):
        select = []
        for element in team:
            select += element

        select = set(select)
        if numbers == select:
            ans += 1

print(ans)
