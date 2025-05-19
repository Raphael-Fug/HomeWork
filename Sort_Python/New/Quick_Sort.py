def Partition(A, left, right):
    # Điểm chốt (Chọn điểm cuối)
    pivot = A[right]
    i = left - 1
    for j in range(left, right):
        # Nếu A tại vị trí nhỏ hơn điểm chốt thì tăng i lên 1 và đảo vị trí với j
        if(A[j] <= pivot):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    # Trả về điểm chốt hiện tại
    return i + 1
def Sort(A, left, right):
    if left < right:
        # Vừa trả về điểm chốt vừa phân vùng
        pivot = Partition(A, left, right)
        Sort(A, left, pivot - 1)
        Sort(A, pivot + 1, right)
A = [12, 234, 11, 5, 50, 200]
n = len(A)
Sort(A, 0, n - 1)
print(A)