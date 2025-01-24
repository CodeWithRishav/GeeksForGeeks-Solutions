#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
# Return boolean value True or False

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):

        #using two pointers and moving one pointer(slow) by one node and
        #another pointer(fast) by two nodes in each iteration.
        slow = head
        fast = head

        #using a loop to move the pointers which stops when any of the pointers
        #or the pointer next to fast becomes null.
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            #if both the pointers fast and slow point to same node which
            #shows the presence of loop so we return true.
            if slow == fast:
                return True

        #if we reach here it means both the pointers fast and slow never
        #point to same node so we return false.
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    #connects last node to node at position pos from begining.
    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))
        res = Solution().detectLoop(LL.head)
        if (res):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends