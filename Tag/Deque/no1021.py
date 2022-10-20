# 실버3 - 1021. 회전하는 큐 (https://www.acmicpc.net/problem/1021)

from collections import deque

n, m = list(map(int, input().split(' ')))
targets = list(map(int, input().split(' ')))

deq = deque([i for i in range(1, n+1)])
cnt = 0

for t in targets:
    index = deq.index(t)

    if index <= len(deq) // 2 :
        for i in range(index):
            x = deq.popleft()
            deq.append(x)
            cnt += 1
    else:
        for i in range(len(deq) - index):
            x = deq.pop()
            deq.appendleft(x)
            cnt += 1
    deq.popleft()
    
print(cnt)
