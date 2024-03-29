# 실버3 - 1966. 프린터 큐 (https://www.acmicpc.net/problem/1966)

testCase = int(input())

for _ in range(testCase):

    n, m = list(map(int, input().split(' ')))

    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
