#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function which returns a pair such that first of the pair indicates maximum
    #sum when data of a node is included and the second when it is not included.
    def maxSumHelper(self, root):

        #if root is null, we return two zeroes in pair.
        if (root == None):
            sum = [0, 0]
            return sum

        #calling function recursively for left and right subtrees.
        sum1 = self.maxSumHelper(root.left)
        sum2 = self.maxSumHelper(root.right)
        sum = [0, 0]

        #current node is included (Left and right children are not included).
        sum[0] = sum1[1] + sum2[1] + root.data

        #current node is excluded (Either left or right child is included).
        sum[1] = (max(sum1[0], sum1[1]) + max(sum2[0], sum2[1]))
        return sum

    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self, root):

        res = self.maxSumHelper(root)
        #returning the maximum between the elements in pair(res).
        return max(res[0], res[1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10**6)


class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        print(ob.getMaxSum(root))

        print("~")

# } Driver Code Ends