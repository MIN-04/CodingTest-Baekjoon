
# Gold 5 - 2447. 별 찍기 - 10 (https://www.acmicpc.net/problem/2447)

def make_stars(n):
    if n == 1:
        return ['*']
    
    stars = make_stars(n // 3)
    L = []
    
    for star in stars:
        L.append(star * 3)
    for star in stars:
        L.append(star + ' ' * (n//3) + star)
    for star in stars:
        L.append(star * 3)
    return L

N = int(input())
print('\n'.join(make_stars(N)))
