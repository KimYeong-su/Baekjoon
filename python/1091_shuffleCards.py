N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

check = {}
for idx, p in enumerate(P):
    if p in check:
        check[p] += [idx]
    else:
        check[p] = [idx]

if len(check[0]) == len(check[1]) == len(check[2]):
    pass
else:
    print(-1)
    exit()

cards = [x for x in range(N)]
case = [x for x in range(N)]
answer = 0

while True:
    for idx,card in enumerate(cards):
        if card not in check[idx%3]:
            break
    else:
        print(answer)
        break


    tmp = [0] * N
    for i in range(N):
        tmp[S[i]] = cards[i]

    if tmp == case:
        print(-1)
        break
    
    cards = tmp
    answer += 1