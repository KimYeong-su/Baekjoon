import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
crime_index = []
for idx, num in enumerate(list(map(int, input().rstrip('\n').split()))):
    crime_index.append([-num, idx])
base = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
mafia_idx = int(input().rstrip('\n'))
visit = [False] * N
if N == 1:
    print(0)
    exit()
answer = 0
def game(remain, result):
    global answer
    if remain == 1 or visit[mafia_idx]:
        if answer < result:
            answer = result
        return
    if remain%2: # 낮
        now = [-1,-1]
        for num, idx in crime_index:
            if visit[idx]: continue
            if now == [-1,-1]:
                now = [num,idx]
            else:
                if num < now[0]:
                    now = [num,idx]
                elif num == now[0]:
                    if idx < now[1]:
                        now = [num, idx]
        visit[now[1]] = True
        game(remain-1, result)
        visit[now[1]] = False
        return
    else: # 밤
        for i in range(N):
            if visit[i]: continue
            for j in range(N):
                if visit[j]: continue
                crime_index[j][0] -= base[i][j]
            visit[i] = True
            game(remain-1, result+1)
            visit[i] = False
            for j in range(N):
                if visit[j]: continue
                crime_index[j][0] += base[i][j]
        return
game(N, 0)
print(answer)