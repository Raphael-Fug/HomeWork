n = int(input("Nhập n: "))
k = int(input("Tổ hợp chập k: "))
A = [0]*k
ed = k
def InKQ():
    for item in range(ed):
        print(A[item], end = " ")
    print()
def Try(k, start):
    if k == ed:
        InKQ()
    else: 
        for i in range(start, n+1):
            A[k] = i
            Try(k+1, i +1) # Tăng chỉ số bắt đầu để tránh lặp lại
Try(0, 1)