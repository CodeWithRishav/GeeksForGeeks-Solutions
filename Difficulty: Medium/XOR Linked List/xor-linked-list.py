#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def insert(head, data):
    # create a new node with the given data
    new_node = Node(data)
    # make the new node's npx point to the current head
    new_node.npx = head
    # return the new node as the new head
    return new_node


def getList(head):
    result = []
    current = head
    while current is not None:
        # add the data of the current node to the list
        result.append(current.data)
        # move to the next node
        current = current.npx
    # return the list containing the values of the nodes in the list
    return result
    
    
    
    

#{ 
 # Driver Code Starts.
#Back-end complete function Template for Python 3
class Node:
    def __init__(self, x):
        self.data = x
        self.npx = None

def XOR(a, b):
    return id(a) ^ id(b)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        head = None
        data_list = list(map(int, input().split()))
        for data in data_list:
            head = insert(head, data)
        
        vec = getList(head)
        print(*vec)
        print(*reversed(vec))

# } Driver Code Ends