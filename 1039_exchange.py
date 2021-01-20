N,K = map(int, input().split(' '))
N = str(N)
maximum = sorted(N, reverse=True)
queue = [(N, 0, i) for i in range(len(N)-1)]
answer = -1
while queue:
    tmp, cnt, idx = queue.pop(0)
    if cnt == K:
        result = int(tmp)
        if answer < result:
            answer = result
        continue
    if idx == len(tmp):
        continue
    if list(tmp) == maximum:
        break
    for i in range(idx+1, len(tmp)):
        if tmp[idx] < tmp[i]:
            a = tmp[:idx] + tmp[i] + tmp[idx+1:i] + tmp[idx] + tmp[i+1:]
            queue.append((a, cnt+1, idx+1))

if (K - cnt) % 2:
    answer = tmp[:len(tmp)-2] + tmp[-1] + tmp[-2]
print(int(answer))