#{ 
 # Driver Code Starts
#Initial Template for Python 3
# 
# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def is_sum_tree(self, node):
        def check_sum_tree(node):
            
            # An empty tree is considered a Sum Tree
            if node is None:
                return 0
            
            # A leaf node is also considered a Sum Tree
            if node.left is None and node.right is None:
                return node.data
            
            # Recursively check the sum for the left and right subtrees
            left_sum = check_sum_tree(node.left)
            right_sum = check_sum_tree(node.right)
            
            # If any of the subtrees is not a Sum Tree, return -1 as a failure signal
            if left_sum == -1 or right_sum == -1:
                return -1
            
            # Check if the current node's data equals the sum of the left and right subtrees
            if node.data == left_sum + right_sum:
                # Return the sum of the current node's subtree (node.data + left_sum + right_sum)
                return node.data + left_sum + right_sum
            else:
                # If not, return -1 to indicate failure
                return -1
        
        # Start the check from the root node
        return check_sum_tree(node) != -1
        # code here

#{ 
 # Driver Code Starts.
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Utility function to create a new Tree Node
def new_node(val):
    return Node(val)


# Function to Build Tree
def build_tree(s):
    # Corner Case
    if not s or s[0] == 'N':
        return None

    # Creating list of strings from input string after splitting by space
    ip = s.split()

    # Create the root of the tree
    root = new_node(int(ip[0]))

    # Push the root to the queue
    queue = []
    queue.append(root)

    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        curr_node = queue.pop(0)

        # Get the current node's value from the string
        curr_val = ip[i]

        # If the left child is not null
        if curr_val != "N":
            # Create the left child for the current node
            curr_node.left = new_node(int(curr_val))

            # Push it to the queue
            queue.append(curr_node.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        curr_val = ip[i]

        # If the right child is not null
        if curr_val != "N":
            # Create the right child for the current node
            curr_node.right = new_node(int(curr_val))

            # Push it to the queue
            queue.append(curr_node.right)
        i += 1

    return root


# Driver code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = build_tree(s)
        ob = Solution()
        if ob.is_sum_tree(root):
            print("true")
        else:
            print("false")

# } Driver Code Ends