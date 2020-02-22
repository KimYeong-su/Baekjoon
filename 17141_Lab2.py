# 재귀함수를 이용한 조합 만들기 https://jebae.github.io/2018/11/13/combination-using-recursion/
def recursion(l1,l2,arr):
    arr.append(l1)
    for i, x in enumerate(l2):
        recursion(l1+[x], l2[i+1:],arr)

def combination(l):
    result = []
    recursion([],l,result)
    return result[1:]

N, M = map(int, input().split())

base = [list(map(int,input().split()))for _ in range(N)]

s_point = []
for i in range(N):
    for j in range(N):
        if base[i][j]==2:
            s_point.append((i,j))
        elif base[i][j]==1:
            base[i][j] = '-'

# result = list(combination(s_point,M))
# print(result)
case = []
for i in combination(s_point):
    if len(i)==M:
        case.append(i)
print(case)
