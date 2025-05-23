class Node:
    def __init__(self, data):
        self.data = data
        # Ban đầu chưa có liên kết
        self.next = None
class LinkedList:
    # Khởi tạo điểm đầu
    def __init__(self):
        self.head = None
    def Insert_at_begining(self, data):
        # Khởi tạo node mới
        new_node = Node(data)
        # self.head: Tham chiếu đến nút đầu tiên hiện tại của danh sách liên kết
        # Dòng này gán con trỏ next của nút mới để trỏ đến nút đầu tiên hiện tại
        # Nếu danh sách đang trống (self.head là None), thì new_node.next cũng sẽ là None
        new_node.next = self.head
        self.head = new_node
    def Insert_at_end(self, data):
        new_node = Node(data)
        # Nếu list đang rỗng
        if new_node.next == None:
            self.head = new_node
            return
        # Xác định last node
        current = self.head
        while (new_node.next != None):
            current = current.next
    def Delete_at_begining(self, data):
        return