import sys
from copy import deepcopy
input = sys.stdin.readline

R,C,M = map(int, input().rstrip('\n').split())
maps = [[0]*C for _ in range(R)]
queue = []
for _ in range(M): # 1:위, 2: 아래, 3: 오른쪽, 4: 왼쪽
    r,c,s,d,z = map(int, input().rstrip('\n').split())
    if r-1==0 and d==1:
        maps[r-1][c-1] = (s,2,z)
    elif r-1==R-1 and d==2:
        maps[r-1][c-1] = (s,1,z)
    elif c-1==0 and d==4:
        maps[r-1][c-1] = (s,3,z)
    elif c-1==C-1 and d==3:
        maps[r-1][c-1] = (s,4,z)
    else:
        maps[r-1][c-1] = (s,d,z)
    queue.append((r-1,c-1))

def next_position(r,c,s,d):
    if d==3 or d==4:
        remain = s%(C*2-2)
        while remain:
            if d==3:
                c += 1
                remain -= 1
                if c==C-1:
                    d=4
            else:
                c -= 1
                remain -= 1
                if c==0:
                    d=3
    else:
        remain = s%(R*2-2)
        while remain:
            if d == 1:
                r -= 1
                remain -= 1
                if r == 0:
                    d=2
            else:
                r += 1
                remain -= 1
                if r == R-1:
                    d=1
    return r, c, s, d

fishing = 0
answer = 0
while fishing<C:
    for i in range(R):
        if maps[i][fishing]:
            answer += maps[i][fishing][2]
            maps[i][fishing] = 0
            queue.remove((i,fishing))
            break
    if len(queue) == 0:
        break
    tmp = [[0]*C for _ in range(R)]
    tmp_q = set()
    for r,c in queue:
        s,d,z = maps[r][c]
        if s == 0:
            nr,nc,ns,nd = r,c,s,d
        else:
            nr,nc,ns,nd = next_position(r,c,s,d)
        tmp_q.add((nr,nc))
        if tmp[nr][nc] == 0:
            tmp[nr][nc] = (ns, nd, z)
        else:
            if z > tmp[nr][nc][2]:
                tmp[nr][nc] = (ns, nd, z)
    
    fishing += 1
    maps = deepcopy(tmp)
    queue = list(tmp_q)

print(answer)