import sys
from copy import deepcopy
input = sys.stdin.readline

R,C,M = map(int, input().rstrip('\n').split())
maps = [[0]*C for _ in range(R)]
queue = []
for _ in range(M): # 1:위, 2: 아래, 3: 오른쪽, 4: 왼쪽
    r,c,s,d,z = map(int, input().rstrip('\n').split())
    maps[r-1][c-1] = (s,d,z)
    queue.append((r-1,c-1))

def next_position(r,c,s,d):
    if d == 1:
        
    elif d == 2:
        
    elif d == 3:
        
    elif d == 4:
        
            
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