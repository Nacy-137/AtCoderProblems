n, m = map(int, input().split())
n_min = 1
n_max = n

for j in range(m):
    l, r = map(int, input().split())

    if n_min <= l:
        n_min = l
    if r <= n_max:
        n_max = r

if n_max < n_min:
    n_max = n_min - 1
print(n_max - n_min + 1)

"""
n, m = map(int, input().split())
L = 0
R = n

for j in range(m):
    l, r = map(int, input().split())
    L = max(L, l)
    R = min(R, r)

if R < L:
    R = L - 1

num = range(L, R+1)
print(len(num))
"""