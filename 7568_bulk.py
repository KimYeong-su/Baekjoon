from sys import stdin

N = int(stdin.readline())
base = [tuple(map(int,stdin.readline().split())) for _ in range(N)]
answer = [1] * N
for i in range(N-1):
    aw, ah = base[i]
    for j in range(i+1,N):
        bw, bh = base[j]
        if aw > bw and ah > bh:
            answer[j] += 1
        elif aw < bw and ah < bh:
            answer[i] += 1
print(' '.join(map(str,answer)))