# Liệt kê xâu nhị phân độ dài n
n = int(input("Nhập n: "))
m = int(input("Nhập phần tử:"))
A = [0] * (n + 1)  # Khởi tạo danh sách A với n+1 phần tử

def GhiNhan():
    for i in range(1, m+1):
        print(A[i], end=' ')  # In cùng trên một dòng
    print() 
# def Try(k):
#     for i in range(0, 2):
#         A[k] = i
#         if (k == n):
#             GhiNhan()
#         else: 
#             Try(k+1)
# Try(0)
def Try(k, start):
    for i in range(start, n + 1):
        A[k] = i
        if k == m:
            GhiNhan()
        else:
            Try(k + 1, i + 1)
Try(1,1)