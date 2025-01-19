# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:

    #Function to rotate a linked list.
    def rotate(self, head, k):
        # If the linked list is empty or no rotations are needed,
        # return the original linked list
        if k == 0 or head is None:
            return head

        curr = head
        length = 1

        # Find the length of the linked list
        while curr.next is not None:
            curr = curr.next
            length += 1

        # Modulo k with length of linked list to handle
        # large values of k
        k %= length

        if k == 0:
            curr.next = None
            return head

        # Make the linked list circular
        curr.next = head

        # Traverse the linked list to find the kth node
        curr = head
        for _ in range(1, k):
            curr = curr.next

        # Update the (k + 1)th node as the new head
        newHead = curr.next

        # Break the loop by updating the next pointer
        # of kth node
        curr.next = None
        return newHead


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        k = int(data[idx + 1].strip())
        idx += 2
        head = Solution().rotate(head, k)
        printList(head)
        print("~")
        t -= 1

# } Driver Code Ends