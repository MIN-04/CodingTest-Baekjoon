# 실버5 - 11866. 요세푸스 문제 0 (https://www.acmicpc.net/problem/11866)

from collections import deque


n, k = list(map(int, input().split(' ')))
deq = deque([i for i in range(1, n+1)])

result = []

for i in range(n) :
    for j in range(k-1):
        deq.append(deq.popleft())
    result.append(deq.popleft())

print('<', end='')
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=', ')
    else: 
        print(result[i], end='')
print('>')
