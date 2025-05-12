import math
# Đệ quy tổ hợp
def ToHop(n, k):
    if (k == 0 or k == n):
        return 1
    else:
        return ToHop(n-1, k-1) + ToHop(n-1, k)
def ToHop_conho(n, k):
    # Kiểm tra điều kiện đầu vào
    if k > n:
        return 0
    if (k == 0 or k == n):
        return 1
    if n >= len(D) or k >= len(D[0]):
        return ToHop_conho(n-1, k-1) + ToHop_conho(n-1, k)
    if(D[n][k] != -1): 
        return D[n][k]
    else:
        D[n][k] = ToHop_conho(n-1, k-1) + ToHop_conho(n-1, k)
        return D[n][k]

# Kích thước mảng D
n = 30
k = 20
# Khởi tạo mảng D
D = [[-1 for j in range(k)] for i in range(n)]
print(ToHop_conho(5, 2))
# print(ToHop(5, 3))

# Đệ quy tháp Hà Nội
def HanoiTower(n, a, c, b):
    if (n == 1): 
        print(f" Chuyển từ cọc {a} sang cọc {c}")
    else:
        HanoiTower(n-1, a, b, c)
        HanoiTower(1, a, c, b)
        HanoiTower(n-1, b, c, a)
# a = "a"
# b = "b"
# c = "c"
# HanoiTower(5, a, c, b)

def Palindrome(str, start, end):
    if(start >= end): return True
    else:
        if(str[start] == str[end]): return Palindrome(str, start+1, end-1)
        else: return False
str = "abcbag"
print(Palindrome(str, 0, len(str)-1 ))
