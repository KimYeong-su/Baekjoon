N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

check = {}
for idx, p in enumerate(P):
    if p in check:
        check[p] += [idx]
    else:
        check[p] = [idx]

print(check)

# answer = 0
# tmp = []
# for s in S:
#     tmp.append(s)

# case = []

# while True:

#     for idx, t in enumerate(tmp):
#         if t not in check[idx]:
#             break
#     else:
#         print(answer)
#         exit()
#     if tmp in case:
#         print(-1)
#         exit()
#     else:
#         case.append(tmp)
    
#     tmp1 = [0] * N
#     for t in tmp:
#         tmp1[t] = t

#     tmp = tmp1
#     answer += 1    