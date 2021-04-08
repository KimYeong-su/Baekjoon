'''
1026_보물
sol) 처음엔 재귀를 통해 하나씩 최소값을 찾기위해 확인해 나갔지만.. 
시간초과.. 혹시나 해서 재귀를 풀기전 생각했던 방식을 해봤더니.. 통과..
가끔은 그냥 쉽게 생각하는게 답이구나 싶습니다..
'''

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

result = 0
A = list(sorted(A))
B = list(sorted(B, reverse=True))
for i in range(N):
    result += A[i]*B[i]
print(result)