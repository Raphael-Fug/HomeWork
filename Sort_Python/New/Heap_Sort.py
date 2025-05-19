def MaxHeapNode(A, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    max_index = i  # Đặt max_index là chỉ số của nút hiện tại

    # Kiểm tra xem nút trái có lớn hơn nút hiện tại không
    if left < n and A[left] > A[max_index]:
        max_index = left

    # Kiểm tra xem nút phải có lớn hơn nút hiện tại không
    if right < n and A[right] > A[max_index]:
        max_index = right

    # Nếu nút lớn nhất không phải là nút hiện tại, hoán đổi và tiếp tục heapify
    if max_index != i:
        A[i], A[max_index] = A[max_index], A[i]
        MaxHeapNode(A, n, max_index)

def MaxHeap(A, n):
    # Xây dựng heap tối đa từ giữa mảng trở về đầu
    for i in range(n // 2 - 1, -1, -1):
        MaxHeapNode(A, n, i)

def Sort(A, n):
    if n == 1:
        return
    else:
        MaxHeap(A, n)  # Xây dựng heap tối đa
        A[0], A[n - 1] = A[n - 1], A[0]  # Hoán đổi phần tử lớn nhất với phần tử cuối cùng
        Sort(A, n - 1)  # Gọi đệ quy với kích thước giảm
A = [12, 234, 11, 5, 50, 200]
n = len(A)
Sort(A, n)
print(A)