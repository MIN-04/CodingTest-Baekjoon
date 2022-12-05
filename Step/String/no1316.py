# Silver 5 - 1316. 그룹 단어 체커 (https://www.acmicpc.net/problem/1316)

N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    arr = [word[0]]
    flag = True
    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            if word[i] in arr:
                flag = False
                break
            else:
                arr.append(word[i])
    if flag:
        cnt += 1
print(cnt)
