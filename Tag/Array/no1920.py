# 실버4 - 1920. 수 찾기 (https://www.acmicpc.net/problem/1920)

n = int(input())
a = set(map(int, input().split(' ')))
m = int(input())
data = list(map(int, input().split(' ')))

for i in data:
    if i not in a:
        print(0)
    else:
        print(1)
