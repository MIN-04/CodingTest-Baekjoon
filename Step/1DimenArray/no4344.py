# Bronze 1 - 4344. 평균은 넘겠지 (https://www.acmicpc.net/problem/4344)

for _ in range(int(input())):
    scores = list(map(int, input().split(" ")))
    avgs = sum(scores[1:]) / scores[0]
    
    cnt = 0
    for score in scores[1:]:
        if score > avgs:
            cnt += 1
    
    rate = cnt / scores[0] * 100
    print(f'{rate:.3f}%')
