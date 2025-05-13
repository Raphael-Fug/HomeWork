# Cho một mảng số nguyên, hãy tìm số lớn nhất và nhỏ nhất trong mảng.
def Max(A):
    max = -10000
    for i in range(len(A)):
        if(A[i] > max):
            max = A[i]
    return max
def Min(A):
    min = 100000
    for i in range(len(A)):
        if(A[i] < min):
            min = A[i]
    return min
A = []
n = int(input("Nhập số lượng phần tử của mảng: "))
for i in range(0, n):
    i = int(input(f"Nhập phần tử thứ {i} của mảng: "))
    A.append(i)
print(f"Max: {Max(A)}, Min: {Min(A)}")