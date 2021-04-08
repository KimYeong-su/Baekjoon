N,M,G,R = map(int,input().split())
base = [list(map(int,input().split()))for _ in range(N)]
visit = [[0 for i in range(M)]for j in range(N)]

# 시작가능 좌표 찾기 & 호수는 visit=-1 처리
s_p = []
for i in range(N):
    for j in range(M):
        if base[i][j]==2:
            s_p.append((i,j))
        elif base[i][j]==0:
            visit[i][j]=-1
l = len(s_p)
way_g=[]
way_r=[]
for i in range(1<<l):
    temp = []
    temp2 = []
    for j in range(l+1):
        if i & (1<<j):
            temp.append(j)
        else:
            if j!=l:
                temp2.append(j)
    if len(temp)==G:
        way_g.append(temp)
        temp4 = []
        for a in range(1<<len(temp2)):
            temp3 = []
            for b in range(len(temp2)+1):
                if a & (1<<b):
                    temp3.append(temp2[b])
            if len(temp3)==R:
                temp4.append(temp3)
        way_r.append(temp4)
for i in range(len(way_r)):
    print(way_g[i])
    print(way_r[i],len(way_r[i]))
