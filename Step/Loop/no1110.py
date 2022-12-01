# Bronze 1 - 1110. 더하기 사이클 (https://www.acmicpc.net/problem/1110)

N = int(input())
cnt = 0
origin = N
while True:
    ten = N // 10
    unit = N % 10
    N = unit * 10 + (ten + unit) % 10
    cnt += 1
    
    if N == origin:
        break

print(cnt)
