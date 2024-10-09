#User function Template for python3

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def constructLinkedMatrix(self, mat):
        n = len(mat)
        # Create a list of lists to store nodes
        nodes = [[None for _ in range(n)] for _ in range(n)]

        # Step 1: Initialize all nodes
        for i in range(n):
            for j in range(n):
                nodes[i][j] = Node(mat[i][j])

        # Step 2: Set the right and down pointers
        for i in range(n):
            for j in range(n):
                if j + 1 < n:  # if not the last column, set right pointer
                    nodes[i][j].right = nodes[i][j + 1]
                if i + 1 < n:  # if not the last row, set down pointer
                    nodes[i][j].down = nodes[i + 1][j]

        # Return the head of the linked matrix (top-left node)
        return nodes[0][0]

#{ 
 # Driver Code Starts
class Node():

    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None


def display(head):
    Dp = head
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            if Rp.right:
                print(Rp.right.data, end=" ")
            else:
                print("null", end=" ")
            if Rp.down:
                print(Rp.down.data, end=" ")
            else:
                print("null", end=" ")
            Rp = Rp.right
        Dp = Dp.down


if __name__ == "__main__":
    for _ in range(int(input())):
        # First row input
        a = list(map(int, input().strip().split()))
        n = len(a)

        # Input the matrix
        mat = [a]
        for i in range(1, n):
            row = list(map(int, input().strip().split()))
            mat.append(row)

        # Create a Solution object and construct the linked matrix
        obj = Solution()
        head = obj.constructLinkedMatrix(mat)
        if head is None:
            print(-1)
            continue
        display(head)
        print()

# } Driver Code Ends