# 브론즈3 - 2501. 약수 구하기 (https://www.acmicpc.net/problem/2501)

N, K = map(int, input().split(" "))

answer = [i for i in range(1, N + 1) if N % i == 0]

if len(answer) < K:
    print(0)
else:
    print(answer[K-1])
