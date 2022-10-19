# 실버4 - 10828. 스택 (https://www.acmicpc.net/problem/10828)

n = int(input())
stack = []
result = []

for _ in range(n):
    command = input().split(' ')
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack:
            result.append(stack.pop())
        else:
            result.append('-1')
    elif command[0] == 'size':
        result.append(str(len(stack)))
    elif command[0] == 'empty':
        if stack:
            result.append('0')
        else: 
            result.append('1')
    elif command[0] == 'top':
        if stack:
            result.append(stack[-1])
        else:
            result.append('-1')
print('\n'.join(result))
