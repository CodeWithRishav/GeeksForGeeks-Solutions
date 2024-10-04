#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        if head is None or head.next == head:
            return head

        prev = None
        current = head
        init = head

        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == init:
                break

        head.next = prev
        return prev

    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        if head is None:
            return head

        current = head
        prev = None

        # If head is to be deleted
        if current.data == key:
            if head.next == head:
                return None
            while current.next != head:
                current = current.next
            current.next = head.next
            return current.next

        # If node to be deleted is not the head node
        while current.next != head and current.data != key:
            prev = current
            current = current.next

        if current.data == key:
            prev.next = current.next

        return head
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends