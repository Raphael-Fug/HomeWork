n = int(input("Nhập n: "))
A = [0] * n  # Chỉ cần n phần tử cho hàng
cot = [1] * (n + 1)  # Bắt đầu với tất cả cột đều khả dụng
cheo1 = [1] * (2 * n)  # Chéo chính
cheo2 = [1] * (2 * n)  # Chéo phụ

def print_board(A, n):
    # Tạo bàn cờ để hiển thị trực quan
    board = [['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        board[i][A[i] - 1] = 'Q'  # -1 vì A[i] bắt đầu từ 1
    
    # In bàn cờ
    print("Giải pháp:")
    for row in board:
        print(' '.join(row))
    print()

def InKQ(A, n):
    for i in range(n):
        print(f"Con hậu ở hàng thứ {i + 1} cột {A[i]}")  # Thay đổi chỉ số cho dễ hiểu
    print_board(A, n)

def Try(i):
    if i == n:  # Khi đã đặt hết quân hậu
        InKQ(A, n)
        return
    for j in range(1, n + 1):
        if cot[j] == 1 and cheo1[i - j + n] == 1 and cheo2[i + j - 1] == 1:
            A[i] = j
            cot[j] = 0
            cheo1[i - j + n] = 0
            cheo2[i + j - 1] = 0
            Try(i + 1)
            # Backtrack
            cot[j] = 1
            cheo1[i - j + n] = 1
            cheo2[i + j - 1] = 1

Try(0)
