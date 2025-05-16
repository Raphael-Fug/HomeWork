def Count(n):
    if (n < 10): return 1
    return 1 + Count(n // 10)

n = int(input("Nhập n: "))
print (Count(n))