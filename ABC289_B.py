n, m = map(int, input().split())
if n == 0:
    p = []
else:
    p = list(map(int, input().split()))

num = 0
l_num = 0
flag = False

for i in range(1,n+1):
    if i > num:
        if i in p:
            flag = True
            num = i
        else:
            if i == n:
                print(i)
            else:
                print(i, end=' ')
            l_num = i

        while flag:
            if num not in p:
                for j in range(num):
                    if j == n:
                        print(num-j)
                    elif num-j > l_num:
                        print(num-j, end=' ')
                l_num = num
                flag = False
            else:
                num += 1
