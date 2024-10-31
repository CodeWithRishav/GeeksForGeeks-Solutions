#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        if head.data > x:
            new_node = Node(x)
            new_node.next = head
            return new_node
            
        temp = head
        
        while temp != None:
            if temp.next and temp.next.data > x:
                new_node = Node(x)
                curr_next = temp.next
                temp.next = new_node
                temp.next.next = curr_next
                break
            
            elif temp.next == None:
                temp.next = Node(x)
                break
            temp = temp.next
        
        
        return head

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends