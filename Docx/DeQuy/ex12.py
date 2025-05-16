def generate_subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])  # Thêm bản sao của current vào kết quả
        for i in range(start, len(nums)):
            current.append(nums[i])  # Thêm phần tử vào current
            backtrack(i + 1, current)  # Gọi đệ quy để thêm phần tử tiếp theo
            current.pop()  # Xóa phần tử cuối cùng để quay lại trạng thái trước

    backtrack(0, [])
    return result

# Ví dụ sử dụng
input_set = [1, 2, 3]
subsets = generate_subsets(input_set)
print(subsets)
