# Bronze 2 - 2231. 분해합 (https://www.acmicpc.net/problem/2231)

N = int(input())

for i in range(1, N+1):
    arr = list(map(int, str(i)))
    M = i + sum(arr)

    if M == N:
        print(i)
        break
    if i == N:
        print(0)