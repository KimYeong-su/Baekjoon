N, M = map(int,input().split())
base = [list(map(int,input().split()))for _ in range(N)]
visit = [[0 for _ in range(N)]for _ in range(N)]
start = []
for i in range(N):
    for j in range(N):
        if base[i][j]==1:
            base[i][j]='-'
            visit[i][j]=1
        elif base[i][j]==2:
            base[i][j]='*'
            start += [(i,j)]

case = []
for i in range(1<<len(start)):
    temp = []
    for j in range(len(start)+1):
        if i & (1<<j):
            temp+=[start[j]]
    if len(temp)==M:
        case += [temp]

minimum = 10000
for a in range(len(case)):
    temp_max=0
    temp_point = []
    for i in range(N):
        for j in range(N):
            temp_d = 10000
            temp_d_point=[]
            if base[i][j]!='-' and base[i][j]!='*':
                for p,q in case[a]:
                    flag_row=0
                    flag_col=0
                    d = abs(i-p)+abs(j-q)
                    if p > i and q > j:
                        for a in range(i,p+1):
                            if 1 not in visit[a][j:q+1]:
                                flag_row = 1
                                break
                        for b in range(j,q+1):
                            for a in range(i,p+1):
                                if visit[a][b]==1:
                                    break
                                if a==p and visit[a][b]==0:
                                    flag_col=1
                            if flag_col == 1:
                                break
                    elif p > i and q <= j:
                        for a in range(i,p+1):
                            if 1 not in visit[a][q:j+1]:
                                flag_row = 1
                                break
                        for b in range(q,j+1):
                            for a in range(i,p+1):
                                if visit[a][b]==1:
                                    break
                                if a==p and visit[a][b]==0:
                                    flag_col=1
                            if flag_col == 1:
                                break
                    elif p <= i and q <= j:
                        for a in range(p,i+1):
                            if 1 not in visit[a][q:j+1]:
                                flag_row = 1
                                break
                        for b in range(q,j+1):
                            for a in range(p,i+1):
                                if visit[a][b]==1:
                                    break
                                if a==i and visit[a][b]==0:
                                    flag_col=1
                            if flag_col == 1:
                                break
                    elif p <= i and q > j:
                        for a in range(p,i+1):
                            if 1 not in visit[a][j:q+1]:
                                flag_row = 1
                                break
                        for b in range(j,q+1):
                            for a in range(p,i+1):
                                if visit[a][b]==1:
                                    break
                                if a==i and visit[a][b]==0:
                                    flag_col=1
                            if flag_col == 1:
                                break
                    if flag_row==1 and flag_col==1:
                        if temp_d>d:
                            temp_d = d

                            # if len(temp_d_point)==0:
                            #     temp_d_point.append((i,j))
                            # else:
                            #     temp_d_point[0] = (i,j)
                if temp_d != 10000:
                    if temp_max<temp_d:
                        temp_max = temp_d
                    # if len(temp_point)==0:
                    #     temp_point.append(temp_d_point[0])
                    # else:
                    #     temp_point[0] = temp_d_point[0]
    if temp_max!=0:
        if minimum>temp_max:
            minimum = temp_max

print(minimum)
