def climb_stairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1  # 1 cách để leo 1 bậc
    dp[2] = 2  # 2 cách để leo 2 bậc (1+1 hoặc 2)
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print(climb_stairs(9))  # 8
