# 실버3 - 16165. 걸그룹 마스터 준석이 (https://www.acmicpc.net/problem/16165)

# 걸그룹 수 N, 맞춰야 할 문제 수 M
N, M = map(int, input().split())

team_mem, mem_team = {}, {}

for i in range(N) :
    team_name, team_num = input(), int(input())
    team_mem[team_name] = []
    for j in range(team_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M) :
    data, case = input(), int(input())
    if case:
        print(mem_team[data])
    elif case == 0:
        for name in sorted(team_mem[data]):
            print(name)

