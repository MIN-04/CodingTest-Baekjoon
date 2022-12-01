# Bronze 1 - 1546. 평균 (https://www.acmicpc.net/problem/1546)

N = int(input())
score = list(map(int, input().split(" ")))
Max = max(score)
for i in range(len(score)):
    score[i] = score[i] / Max * 100
print(sum(score) / N)
