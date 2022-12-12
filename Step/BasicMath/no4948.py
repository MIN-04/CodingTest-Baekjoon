# Silver 2 - 4948. 베르트랑 공준 (https://www.acmicpc.net/problem/4948)

prime = []

for num in range(1, 246913):
    if num != 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            prime.append(num) 

while True:
    n = int(input())
    if n == 0:
        break
    
    cnt = 0
    for num in prime:
        if n < num and num <= 2*n:
            cnt += 1
    print(cnt)
    
