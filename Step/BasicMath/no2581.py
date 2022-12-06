# Silver 5 - 2581. 소수 (https://www.acmicpc.net/problem/2581)

M = int(input())
N = int(input())
arr = []
for num in range(M, N + 1):
    flag = True
    if num != 1:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            arr.append(num)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
