#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.prev=self.head
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.prev = self.head
        else:
            self.prev.next = new_node
            self.prev = self.prev.next

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


# } Driver Code Ends
#User function Template for python3

class Solution:
    def sortedInsert(self,head,key):
        new_node = Node(key)
        
        if head is None or head.data>=key:
            # if new node is needed at the start of list
            new_node.next = head
            return new_node
        
        current = head
        
        while (current.next is not None) and current.next.data<key:
            current = current.next;
            # finding a node which has lesser value than new_node
            # but its successor should have greater (or equal) value
        
        # inserting new_node after current node
        new_node.next = current.next;
        current.next = new_node;
        
        return head


#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        
        key=int(input())
        h=Solution().sortedInsert(a.head,key)
        printList(h)

# } Driver Code Ends