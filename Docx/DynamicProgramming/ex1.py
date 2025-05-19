n = int(input("Nhập n: "))
memmory = [0]*(n+1)
# Cách Top-down
def Fibonanci(n):
    if n <= 1: return 1
    if memmory[n] != 0: return memmory[n]
    result = Fibonanci(n-1) + Fibonanci(n-2)
    memmory[n] = result
    return result
print(Fibonanci(n))

# Cách Bottom-up
def fibonacci(n):
    # Khởi tạo bảng DP
    dp = [0] * (n + 1)
    
    # Điền giá trị cơ sở
    dp[0] = 0
    dp[1] = 1
    
    # Tính các giá trị tiếp theo
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
