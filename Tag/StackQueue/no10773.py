# 실버4 - 10773. 제로 (https://www.acmicpc.net/problem/10773)

k = int(input())
stack = []

for _ in range(k):
    data = int(input())

    if data == 0:
        if stack:
            stack.pop()
        else:
            stack.append(data)
    else:
        stack.append(data)
print(sum(stack))
