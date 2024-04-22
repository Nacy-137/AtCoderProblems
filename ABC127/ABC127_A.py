age, fee = map(int, input().split())
rate = 1

if age <= 5:
    rate = 0
elif 6 <= age <= 12:
    rate = 0.5

print(round(fee * rate))