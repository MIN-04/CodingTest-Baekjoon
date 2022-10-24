# 브론즈2 - 16675. 두 개의 손 (https://www.acmicpc.net/problem/16675)

# 가위:0 바위:1 보:2
ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())

if ML == MR and (ML+2) % 3 in [TL, TR]:
    print('TK')
elif TL == TR and (TL+2) % 3 in [ML, MR]:
    print('MS')
else:
    print('?')
