T = int(input())

for tc in range(1,T+1):
    N = int(input())
    dp = [0] * (N+1)
    dp[0] = 1

    for i in range(N+1):
        for d in range(1,4):
            if 0 <= i-d <= N:
                dp[i] += dp[i-d]

    print(dp[N])