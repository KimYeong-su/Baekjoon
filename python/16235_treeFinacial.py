import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip('\n').split())
A = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
base = [[5]*N for _ in range(N)]
trees = {(i,j):[] for i in range(N) for j in range(N)}

answer = 0
for _ in range(M):
    x,y,z = map(int, input().rstrip('\n').split())
    trees[(x-1,y-1)] += [z]
    answer += 1

while K:
    if answer == 0:
        break
    tmp = {(i,j):[] for i in range(N) for j in range(N)}
    for x in range(N):
        for y in range(N):
            if not trees[(x,y)]:
                base[x][y] += A[x][y]
                continue
            else:
                if len(trees[(x,y)])>1:
                    trees[(x,y)].sort()
                add_nut = A[x][y]
                for z in trees[(x,y)]:
                    if z > base[x][y]:
                        add_nut += z//2
                        answer -= 1
                    else:
                        base[x][y] -= z
                        tmp[(x,y)] += [z+1]
                        if (z+1)%5==0:
                            for i in range(-1,2):
                                for j in  range(-1,2):
                                    if i==0 and j==0: continue
                                    if 0<=x+i<N and 0<=y+j<N:
                                        tmp[(x+i,y+j)] += [1]
                                        answer += 1
                base[x][y] += add_nut
    trees = tmp                     
    K-=1
print(answer)