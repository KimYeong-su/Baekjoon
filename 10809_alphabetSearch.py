import sys
input = sys.stdin.readline

string = list(input())[:-1]
check = {97+x:-1 for x in range(26)}
for idx, s in enumerate(string):
    if check[ord(s)] == -1:
        check[ord(s)] = idx
answer = ' '.join(map(str,check.values()))
print(answer)