from sys import stdin

def dfs(idx, cnt):
    global answer
    if cnt >= K:
        word_cnt = 0
        for word in words:
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    break
            else:
                word_cnt += 1
        answer = max(answer, word_cnt)
        return
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt+1)
            learn[i] = False

N, K = map(int,stdin.readline().split())
words = [stdin.readline().rstrip() for _ in range(N)]

if K < 5 or K == 26:
    print(0 if K<5 else N)
    exit()

learn = [False] * 26

for c in ['a', 'c', 'i', 'n', 't']:
    learn[ord(c) - ord('a')] = True

answer = 0
dfs(0, 5)
print(answer)