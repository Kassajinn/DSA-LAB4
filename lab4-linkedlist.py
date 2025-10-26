class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # def insert_at_beginning(self, data):
    #     new_node = Node(data)
    #     if self.head:
    #         new_node.next = self.head
    #         self.head = new_node
    #     else:
    #         self.tail = new_node
    #         self.head = new_node

    # def insert_at_end(self,data):
    #     new_node = Node(data)
    #     if self.head:
    #         self.tail.next = new_node
    #         self.tail = new_node
    #     else:
    #         self.head = new_node
    #         self.tail = new_node

    # def view_nodes(self):
    #     current_node = self.head
    #     while current_node:
    #         print(current_node.data)
    #         current_node = current_node.next

    # def search(self, data):
    #     current_node = self.head
    #     while current_node:
    #         if current_node.data == data:
    #             return True    
    #         current_node = current_node.next
    #         return False

    def remove_at_beginning(self):
        current_node = self.head
        if self.head:
            new_head = current_node.next
            self.head = new_head

    def remove_at_end(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None


    def remove_at(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next and current_node.next.data == data:
            current_node.next = current_node.next.next


# link = LinkedList()

# fruit_1 = link.insert_at_beginning("apple")
# fruit_2 = link.insert_at_beginning("orange")
# fruit_2 = link.insert_at_beginning("banana")
# fruit_2 = link.insert_at_beginning("grapes")

# link.view_nodes()

# print("===========================")
# link.remove_at("banana")

# link.view_nodes()
