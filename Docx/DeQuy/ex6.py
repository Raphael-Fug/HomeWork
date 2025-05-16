def Reverse(str):
    n = len(str)
    if (n == 0): return str
    return str[n-1] + Reverse(str[:n-1])
str = input("Nhập chuỗi: ")
print(Reverse(str))