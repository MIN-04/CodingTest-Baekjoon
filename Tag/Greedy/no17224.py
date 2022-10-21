# 브론즈1 - 17224. https://www.acmicpc.net/problem/17224

# 문제 개수 N, 역량 L , 맞출 수 있는 문제 수 K

N, L, K = map(int, input().split())

score = 0
hard, easy = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

# 어려운 문제 점수
score += min(hard, K) * 140 

# 쉬운 문제 점수
if hard < K:
    score += min(K-hard, easy) * 100

print(score)
