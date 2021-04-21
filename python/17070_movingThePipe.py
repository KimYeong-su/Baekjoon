import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
maps = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
table = [[[0 for _ in range(N)]for _ in range(N)]for _ in range(3)] # 가로 : 0, 세로 : 1, 대각선 : 2

Horize = 0
Vertical = 1
Cross = 2

dr = [0,1,1]
dc = [1,0,1]

def check(to, row, col):
    if 0<=row<N and 0<=col<N:
        if to == Cross:
            if maps[row][col]==0 and maps[row-1][col]==0 and maps[row][col-1]==0: return True
        else:
            if maps[row][col]==0: return True
    return False

def solution(to, row, col):
    global table
    if row == N-1 and col == N-1: return 1
    if table[to][row][col]: return table[to][row][col]
    for i in range(3):
        nr = row + dr[i]
        nc = col + dc[i]
        flag = False
        if to == Horize and i != Vertical: flag = check(i,nr,nc)
        elif to == Vertical and i != Horize: flag = check(i,nr,nc)
        elif to == Cross: flag = check(i,nr,nc)
        if flag:
            table[to][row][col] += solution(i,nr,nc)
    return table[to][row][col]

print(0) if maps[-1][-1] == 1 else print(solution(Horize, 0, 1))