'''
# 나는 위에서 아래로 찾아왔지만 아래 코드는 아래에서 n을 만들어 나갔다.
# -1을 일일히 하지 않아도 되서 내 코드보다 아래의 코드가 훨 빠르다.
# 내 코드도 좀만 다듬으면 할 수 있을거 같긴하다..

def dp(n):
    if n in memo:
        return memo[n]
    m = 1 + min(dp(n//2) + n % 2, dp(n//3) + n % 3) 
    # 2로 나누어 떨어지면 1만 증가하면 되지만 그렇지 않으면 나머지를 더하여 일일히 더해간다
    # 3도 마찬가지이다.
    memo[n] = m
    return m

memo = {1:0, 2:1}
n = int(input())
print(dp(n))
'''
N = int(input())
dp = [float('inf')] * (N+1)
dp[N] = 0
for i in range(N,0,-1):
    if not i % 3:
        dp[i//3] = min(dp[i//3], dp[i] + 1)
    if not i % 2:
        dp[i//2] = min(dp[i//2], dp[i] + 1)
    if i > 1:
        dp[i-1] = min(dp[i-1], dp[i] + 1)

print(dp[1])