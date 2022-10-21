# 브론즈2 - 17389. 보너스 점수 (https://www.acmicpc.net/problem/17389)

N, S = input(), input()

score, bonus = 0, 0

for idx, OX in enumerate(S):
    if OX == 'O':
        score += idx + 1 + bonus
        bonus += 1
    else:
        bonus = 0
print(score)
