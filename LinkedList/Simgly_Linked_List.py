class Node:
    def __init__(self, value):
        self.value = value
        # Giá trị tại vị trí next hoặc con trỏ ở vị trí tiếp
        self.next = None
class Singly_Linked_List:
    def __init__(self):
        self.head = None
    def Insert_at_beginning(self, value):
        new_node = Node(value) # Khởi tạo Node mới
        new_node.next = self.head # Chỏ đến node tiếp theo, head ban đầu thành next 
        self.head = new_node # Gán node ban đầu
    def Insert_at_end(self, value):
        new_node = Node(value)
        if self.head == None: # Trường hợp list không có phần tử nào
            self.head = new_node
            return
        else:
            current = self.head # Xác đinh phần tử đầu tiên 
            while (current.next != None):
                current = current.next
            current.next = new_node
    def Delete_Value(self, dl_value):
        temp = self.head
        if (temp == dl_value):
            self.head = temp.next
            return
        # Tìm node cần xóa
        while temp != None and temp.next != None: # Kiểm tra temp và node kế tiếp có tồn tại không
            if temp.next.value == dl_value:
                temp.next = temp.next.next # Cho node hiện tại trỏ đến node sau node cần xóa (bỏ qua node cần xóa)
                return
            temp = temp.next # Nếu không tìm thấy, tiếp tục duyệt với temp = temp.next
    def Print_List(self):
        current = self.head
        while current != None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
# Tạo danh sách mới
linked_list = Singly_Linked_List()

# Thêm các node
linked_list.Insert_at_beginning(3)  # 3 -> None
linked_list.Insert_at_beginning(2)  # 2 -> 3 -> None
linked_list.Insert_at_beginning(1)  # 1 -> 2 -> 3 -> None
linked_list.Insert_at_end(4)        # 1 -> 2 -> 3 -> 4 -> None

# In danh sách
linked_list.Print_List()            # Output: 1 -> 2 -> 3 -> 4 -> None

# Xóa node có giá trị 2
linked_list.Delete_Value(2)          # 1 -> 3 -> 4 -> None

# In danh sách sau khi xóa
linked_list.Print_List()            # Output: 1 -> 3 -> 4 -> None
