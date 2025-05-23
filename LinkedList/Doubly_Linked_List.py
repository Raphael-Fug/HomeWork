# class Node:
#     def __init__(self, data):
#         self.data = data    # Dữ liệu của node
#         self.prev = None    # Con trỏ đến node trước đó
#         self.next = None    # Con trỏ đến node tiếp theo

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None    # Con trỏ đến node đầu tiên
#         self.tail = None    # Con trỏ đến node cuối cùng
    
#     # Thêm node vào đầu danh sách
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
        
#         # Nếu danh sách rỗng
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
        
#         # Liên kết node mới với node đầu tiên hiện tại
#         new_node.next = self.head
#         self.head.prev = new_node
        
#         # Cập nhật head
#         self.head = new_node
    
#     # Thêm node vào cuối danh sách
#     def insert_at_end(self, data):
#         new_node = Node(data)
        
#         # Nếu danh sách rỗng
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
        
#         # Liên kết node mới với node cuối cùng hiện tại
#         self.tail.next = new_node
#         new_node.prev = self.tail
        
#         # Cập nhật tail
#         self.tail = new_node
    
#     # Thêm node sau một node cụ thể
#     def insert_after(self, prev_node, data):
#         # Kiểm tra node trước có tồn tại không
#         if prev_node is None:
#             print("Node trước không tồn tại trong danh sách")
#             return
        
#         # Tạo node mới
#         new_node = Node(data)
        
#         # Liên kết node mới với node tiếp theo của prev_node
#         new_node.next = prev_node.next
        
#         # Liên kết node mới với prev_node
#         new_node.prev = prev_node
#         prev_node.next = new_node
        
#         # Nếu node mới không phải là node cuối cùng
#         if new_node.next:
#             new_node.next.prev = new_node
#         else:
#             # Nếu node mới là node cuối cùng, cập nhật tail
#             self.tail = new_node
    
#     # Xóa node theo giá trị
#     def delete_node(self, key):
#         # Nếu danh sách rỗng
#         if self.head is None:
#             print("Danh sách rỗng")
#             return
        
#         # Nếu node đầu tiên chứa giá trị cần xóa
#         if self.head.data == key:
#             # Cập nhật head
#             self.head = self.head.next
            
#             # Nếu danh sách không rỗng sau khi xóa
#             if self.head:
#                 self.head.prev = None
#             else:
#                 # Nếu danh sách rỗng sau khi xóa
#                 self.tail = None
#             return
        
#         # Nếu node cuối cùng chứa giá trị cần xóa
#         if self.tail.data == key:
#             # Cập nhật tail
#             self.tail = self.tail.prev
#             self.tail.next = None
#             return
        
#         # Tìm node cần xóa
#         current = self.head
#         while current and current.data != key:
#             current = current.next
        
#         # Nếu không tìm thấy node
#         if current is None:
#             print(f"Không tìm thấy node có giá trị {key}")
#             return
        
#         # Xóa node bằng cách cập nhật các liên kết
#         current.prev.next = current.next
#         if current.next:
#             current.next.prev = current.prev
    
#     # In danh sách từ đầu đến cuối
#     def print_forward(self):
#         if self.head is None:
#             print("Danh sách rỗng")
#             return
        
#         current = self.head
#         print("Từ đầu đến cuối: ", end="")
#         while current:
#             print(current.data, end=" <-> " if current.next else " -> None")
#             current = current.next
#         print()
    
#     # In danh sách từ cuối đến đầu
#     def print_backward(self):
#         if self.tail is None:
#             print("Danh sách rỗng")
#             return
        
#         current = self.tail
#         print("Từ cuối đến đầu: ", end="")
#         while current:
#             print(current.data, end=" <-> " if current.prev else " -> None")
#             current = current.prev
#         print()
# # Tạo một danh sách liên kết đôi mới
# dll = DoublyLinkedList()

# # Thêm các phần tử
# dll.insert_at_beginning(10)  # 10
# dll.insert_at_beginning(5)   # 5 <-> 10
# dll.insert_at_end(15)        # 5 <-> 10 <-> 15
# dll.insert_at_end(20)        # 5 <-> 10 <-> 15 <-> 20

# # In danh sách theo cả hai hướng
# dll.print_forward()          # Từ đầu đến cuối: 5 <-> 10 <-> 15 <-> 20 -> None
# dll.print_backward()         # Từ cuối đến đầu: 20 <-> 15 <-> 10 <-> 5 -> None

# # Thêm phần tử sau một node cụ thể (sau node có giá trị 10)
# current = dll.head
# while current and current.data != 10:
#     current = current.next

# if current:
#     dll.insert_after(current, 12)  # 5 <-> 10 <-> 12 <-> 15 <-> 20

# dll.print_forward()  # Từ đầu đến cuối: 5 <-> 10 <-> 12 <-> 15 <-> 20 -> None

# # Xóa node có giá trị 15
# dll.delete_node(15)  # 5 <-> 10 <-> 12 <-> 20

# dll.print_forward()  # Từ đầu đến cuối: 5 <-> 10 <-> 12 <-> 20 -> None
