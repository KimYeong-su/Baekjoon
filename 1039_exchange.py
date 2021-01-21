N,K = map(int, input().split())
N = str(N)
maximum = sorted(N, reverse=True)
queue = [(N, 0)]
visit = [[False for _ in range(11)] for _ in range(1000001)]
visit[int(N)][0] = True
answer = -1
while queue:
    tmp, cnt = queue.pop(0)
    if cnt == K:
        answer = max(answer, int(tmp))
    else:
        for idx in range(len(tmp)-1):
            for i in range(idx+1, len(tmp)):
                if idx==0 and tmp[i] == '0': continue
                a = tmp[:idx] + tmp[i] + tmp[idx+1:i] + tmp[idx] + tmp[i+1:]
                if not visit[int(a)][cnt+1]:
                    visit[int(a)][cnt+1] = True
                    queue.append((a, cnt+1))
print(answer)