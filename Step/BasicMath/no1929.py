# Silver 3 - 1929. 소수 구하기 (https://www.acmicpc.net/problem/1929)

M, N = map(int, input().split(" "))

for num in range(M, N + 1):
    if num == 1:
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = False
            break
    else:
        print(num)
