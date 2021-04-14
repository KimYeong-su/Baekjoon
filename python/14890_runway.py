import sys
input = sys.stdin.readline

N, L = map(int, input().rstrip('\n').split())
base = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]

answer = 0
def check(base, result):
    for r in range(N):
        if len(set(base[r])) == 1:
            result += 1
            continue
        now = base[r][0]
        count = 1
        visit = [False] * N
        for c in range(N-1):
            diff = abs(base[r][c]-base[r][c+1])
            if diff > 1: break
            elif diff == 0 : continue
            else:
                if base[r][c]>base[r][c+1] and c<N-L and True not in visit[c+1:c+L+1] and len(set(base[r][c+1:c+L+1]))==1:
                    visit[c+1:c+L+1] = [True] * L
                elif base[r][c]<base[r][c+1] and c+1>=L and True not in visit[c+1-L:c+1] and len(set(base[r][c+1-L:c+1]))==1:
                    visit[c+1-L:c+1] = [True] * L
                else:
                    break
        else:
            result += 1
    return result

answer += check(base, 0)
answer += check(list(zip(*base)),0)
print(answer)