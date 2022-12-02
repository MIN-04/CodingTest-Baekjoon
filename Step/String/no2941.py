# Silver 5 - 2941. 크로아티아 알파벳 (https://www.acmicpc.net/problem/2941)

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in cro:
    if word.find(i) != -1:
        word = word.replace(i, '*')
print(len(word))
