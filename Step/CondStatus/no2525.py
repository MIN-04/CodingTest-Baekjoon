# Bronze 3 - 2525. 오븐 시계 (https://www.acmicpc.net/problem/2525)

A, B = map(int, input().split(" "))
C = int(input())

M = B + C
if A + (M // 60) >= 24:
    A -= 24

print(A + M // 60, M % 60)
