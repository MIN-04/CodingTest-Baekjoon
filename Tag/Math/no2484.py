# 브론즈2 - 2484. 주사위 네개 (https://www.acmicpc.net/problem/2484)

def money() :
    arr = sorted(list(map(int, input().split())))

    if len(set(arr)) == 1:
        return 50000 + arr[-1] * 5000

    if len(set(arr)) == 2:
        if arr[1] == arr[2]:
            return 10000 + arr[2] * 1000
        else:
            return 2000 + arr[1] * 500 + arr[2] * 500

    for i in range(3):
        if arr[i] == arr[i+1]:
            return 1000 + arr[i] * 100

    return arr[-1] * 100

N = int(input())

print(max(money() for i in range(N)))
