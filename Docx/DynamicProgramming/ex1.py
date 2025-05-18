n = int(input("Nhập n: "))
memmory = [0]*(n+1)
def Fibonanci(n):
    if n <= 1: return 1
    if memmory[n] != 0: return memmory[n]
    result = Fibonanci(n-1) + Fibonanci(n-2)
    memmory[n] = result
    return result
print(Fibonanci(n))