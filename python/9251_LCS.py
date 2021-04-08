'''
# https://suri78.tistory.com/11
'''
A = list(input())
B = list(input())
dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
for i in range(1,len(A)+1):
    a = A[i-1]
    for j in range(1,len(B)+1):
        b = B[j-1]
        if a == b:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])