# Cho một mảng số nguyên và một số mục tiêu. 
# Hãy tìm hai số trong mảng có tổng bằng số mục tiêu.
def Sum(A, x):
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            if (x == A[i] + A[j]):
                print(f"[{i}, {j}]")
A = []
n = int(input("Nhập số lượng phần tử của mảng: "))
for i in range(0, n):
    i = int(input(f"Nhập phần tử thứ {i} của mảng: "))
    A.append(i)
x = int(input("Nhập mục tiêu: "))
Sum(A, x)

