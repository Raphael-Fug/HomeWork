import sys

def tsp(graph, s):
    # Lưu tất cả các đỉnh trừ đỉnh đầu tiên
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)
    
    min_path = sys.maxsize
    min_path_order = []
    
    # Lưu tất cả các hoán vị của đường đi
    def permute(vertex, l, r):
        nonlocal min_path, min_path_order
        
        if l == r:
            current_path_weight = 0
            
            # Tính trọng số của đường đi hiện tại
            k = s  # bắt đầu từ đỉnh gốc
            path_order = [s]
            
            for i in range(len(vertex)):
                current_path_weight += graph[k][vertex[i]]
                k = vertex[i]
                path_order.append(k)
            
            # Thêm chi phí quay lại đỉnh gốc
            current_path_weight += graph[k][s]
            path_order.append(s)
            
            # Cập nhật đường đi ngắn nhất
            if current_path_weight < min_path:
                min_path = current_path_weight
                min_path_order = path_order.copy()
        else:
            for i in range(l, r + 1):
                # Swap
                vertex[l], vertex[i] = vertex[i], vertex[l]
                # Đệ quy
                permute(vertex, l + 1, r)
                # Backtrack
                vertex[l], vertex[i] = vertex[i], vertex[l]
    
    permute(vertex, 0, len(vertex) - 1)
    return min_path, min_path_order
# hang = int(input("Nhập số hàng: "))
# cot = int(input("Nhập số cột: "))
# A = []
# for i in range(hang):
#     for j in range(cot):
#         A[i][j] = int(input(f"Nhập số ở hàng {i} và cột {j}: "))