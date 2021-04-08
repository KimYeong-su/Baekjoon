'''
# dfs와 백트래킹을 적절히 사용해야 한다.

1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

answer = 5
'''

import sys
input = sys.stdin.readline

base = [list(map(int,input().split())) for _ in range(10)]
count = {x:0 for x in range(1,6)}
answer = 26

def check(row, col, cnt):
    global answer
    if col >= 10:
        answer = min(answer,cnt)
        return
    if row >= 10:
        check(0,col+1,cnt)
        return
    if cnt >= answer:
        return
    if base[row][col]:
        for size in range(5,0,-1):
            if count[size] == 5: continue
            if row + size >10 or col + size >10: continue
            for i in range(row, row+size):
                if 0 in base[i][col:col+size]:
                    break
            else:
                for i in range(row, row+size):
                    base[i][col:col+size] = [0] * size
                count[size] += 1
                check(row+size, col, cnt+1)
                count[size] -= 1
                for i in range(row, row+size):
                    base[i][col:col+size] = [1] * size
    else:
        check(row+1,col,cnt)


check(0,0,0)
if answer == 26:
    print(-1)
else:
    print(answer)