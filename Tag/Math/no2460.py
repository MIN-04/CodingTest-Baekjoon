# 브론즈3 - 2460. 주사위 세개 (https://www.acmicpc.net/problem/2460)

result = 0
sum = 0
for _ in range(10):
    off, on = map(int, input().split(" "))
    sum = sum - off + on
    result = max(sum, result)
print(result)
