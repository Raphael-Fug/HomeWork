def Sum(n):
    if(n < 10): return n
    return n%10 + Sum(n//10)
n = int(input("Nhập n: "))
print(Sum(n))