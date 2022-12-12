# Silver 3 - 2108. 통계학 (https://www.acmicpc.net/problem/2108)

import sys
import collections

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

# 산술평균
print(round(sum(arr) / N))

# 중앙값
arr.sort()
print(arr[N // 2])

# 최빈값
fre = collections.Counter(arr).most_common()
if len(fre) > 1 and fre[0][1] == fre[1][1]:
    print(fre[1][0])
else:
    print(fre[0][0])

# 범위
print(max(arr) - min(arr))
