import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
base = [[float('inf') for _ in range(n)]for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    base[a-1][b-1] = min(c, base[a-1][b-1])


for k in range(n):
    base[k][k] = 0
    for i in range(n):
        for j in range(n):
            base[i][j] = min(base[i][j], base[i][k] + base[k][j])

for i in base:
    for j in range(n):
        if i[j] == float('inf'):
            i[j] = 0
    print(' '.join(map(str,i)))