# Silver 5 - 2563. 색종이 (https://www.acmicpc.net/problem/2563)

white = [[0] * 100 for _ in range (100)]

T = int(input())

for _ in range(T):
    row, col = map(int, input().split(" "))
    for i in range(row, row + 10):
        for j in range(col, col + 10):
            white[i][j] = 1

sum = 0
for i in range(100):
    for j in range(100):
        if white[i][j]:
            sum += 1
print(sum)
    
