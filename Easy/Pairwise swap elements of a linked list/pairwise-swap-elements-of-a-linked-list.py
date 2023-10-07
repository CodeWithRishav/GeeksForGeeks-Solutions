class Solution:    
    def pairWiseSwap(self, head):
        a = head
        b, c, prev = None, None, None
        
        while a and a.next:
            b = a.next     # b is second node
            c = b.next     # c is third node (c might be null)
                           # current order : prev - a - b - c
            
            if a == head:
                # b will be new head
                head = b
            else:
                # else, linking second node i.e. b, to a's ancestor
                prev.next = b
            
            b.next = a     # a should now come after b
            a.next = c     # connecting a to list ahead
            
            # now we have to update a and prev for next pair
            prev = a
            a = c
            
        return head

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
            
        dict1 = {}
        temp = lis.head
        while temp:
            dict1[temp] = temp.data
            temp = temp.next
        
        failure = LinkedList()
        failure.insert(-1)
        
        head = Solution().pairWiseSwap(lis.head)
        
        temp = head
        f = 0
        while temp:
            if dict1[temp] != temp.data:
                f = 1;
            temp = temp.next
        
        if f:
            printList(failure)
        else:
            printList(head)

# } Driver Code Ends