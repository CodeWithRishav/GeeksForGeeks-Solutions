'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
   '''     
        
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def sortedInsert(self, head, data):
        new_node = Node(data)

        # If linked list is empty
        if head is None:
            new_node.next = new_node
            return new_node

        curr = head
        next_to_curr = head.next

        # Insert at the beginning if data is less
        # than or equal to head's data
        if data <= head.data:
            last_node = head
            while last_node.next != head:
                last_node = last_node.next
            new_node.next = head
            last_node.next = new_node
            return new_node

        # Insert in the middle of the list
        while curr.next != head:
            if curr.data < data and next_to_curr.data >= data:
                new_node.next = curr.next
                curr.next = new_node
                return head
            else:
                curr = curr.next
                next_to_curr = next_to_curr.next

        # Insert at the end of the list
        new_node.next = head
        curr.next = new_node
        return head