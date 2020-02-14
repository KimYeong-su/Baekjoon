def insect(r,c):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    stack = [(r,c)]
    while stack:
        pr,pc = stack.pop()
        ground[pr][pc] = 0
        for k in range(4):
            nr = pr + dx[k]
            nc = pc + dy[k]
            if 0<=nr<N and 0<=nc<M:
                if ground[nr][nc]==1:
                    stack.append((nr,nc))
    # for row in ground:
    #     print(row)
    # print()
    return 1


T = int(input())

for tc in range(1,T+1):
    M, N, K = map(int,input().split())
    ground = [[0 for _ in range(M)]for _ in range(N)]
    start = []
    for _ in range(K):
        c,r = map(int,input().split())
        start.append((r,c))
        ground[r][c] = 1
    # for row in ground:
    #     print(row)
    # print()

    cnt = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                cnt += insect(i,j)
    print(cnt)
