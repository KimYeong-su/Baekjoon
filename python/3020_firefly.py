import sys

N, H = map(int, sys.stdin.readline().split())
up = [0] * H
down = [0] * H
for i in range(N):
    if i % 2:
        down[H-int(sys.stdin.readline())] += 1
    else:
        up[int(sys.stdin.readline())-1] += 1

for i in range(1,H):
    down[i] += down[i-1]
for i in range(H-1,0,-1):
    up[i-1] += up[i]

for i in range(H):
    up[i] += down[i]

answer = min(up)
print(f'{answer} {up.count(answer)}')