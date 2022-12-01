# Bronze 2 - 3052. 나머지 (https://www.acmicpc.net/problem/3052)

mod = []

for _ in range(10):
    mod.append(int(input()) % 42)

print(len(set(mod)))
