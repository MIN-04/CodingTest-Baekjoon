# 브론즈4 - 2480. 주사위 세개 (https://www.acmicpc.net/problem/1920)

lst = sorted(list(map(int, input().split())))

price = 0

if len(set(lst)) == 1:
    price = 10000 + lst[0] * 1000
elif len(set(lst)) == 2:
    price = 1000 + lst[1] * 100
else :
    price = lst[-1] * 100

print(price)
