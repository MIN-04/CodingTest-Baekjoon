# Bronze 2 - 8958. OX퀴즈 (https://www.acmicpc.net/problem/8958)

test = [input() for _ in range(int(input()))]
for result in test:
    score = 0
    sum = 0
    for i in range(len(result)):
        if result[i] == "O":
            sum += 1
        else:
            sum = 0
        score += sum
    print(score)
