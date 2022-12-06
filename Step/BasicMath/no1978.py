# Silver 5 - 1978. 소수 찾기 (https://www.acmicpc.net/problem/1978)

N = int(input())
arr = list(map(int, input().split(" ")))
for num in arr:
    if num == 1:
        N -= 1
        continue
    for i in range(1, num // 2 + 1):
            if i != 1 and num % i == 0:
                N -= 1
                break
print(N)
