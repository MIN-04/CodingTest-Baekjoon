# Bronze 3 - 2884. 알람시계 (https://www.acmicpc.net/problem/2884)

H, M = map(int, input().split(" "))

if M < 45:
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60

print(H, M - 45)
