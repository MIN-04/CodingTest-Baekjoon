# 브론즈2 - 10870. 피보나치 수 5 (https://www.acmicpc.net/problem/10870)

n = int(input())

def fibonacci(n) :
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1 :
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))
