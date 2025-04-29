'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):

        #creating three dummy nodes to point to beginning of three linked lists.
        zeroD = Node(0)
        oneD = Node(1)
        twoD = Node(2)

        #initializing current pointers for three lists.
        zero = zeroD
        one = oneD
        two = twoD

        curr_node = head
        #traversing over the list with a pointer.
        while curr_node:

            #we check data at current node and store the node in it's
            #respective list and update the link part of that list.
            if curr_node.data == 0:
                zero.next = curr_node
                zero = zero.next
            elif curr_node.data == 1:
                one.next = curr_node
                one = one.next
            else:
                two.next = curr_node
                two = two.next
            curr_node = curr_node.next

        #attaching the three lists containing 0s,1s and 2s respectively.
        if oneD.next:
            zero.next = oneD.next
        else:
            zero.next = twoD.next
        one.next = twoD.next
        two.next = None

        return zeroD.next
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))
        print("~")

# } Driver Code Ends