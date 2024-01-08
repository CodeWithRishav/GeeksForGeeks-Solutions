class Solution:
    
    def mergeResult(self, h1, h2):
        #return head of merged list
        
        h1 = self.reverse(h1)
        h2 = self.reverse(h2)
        
        temp = Node(0)
        res = temp
        
        while h1 and h2:
            if h1.data > h2.data:
                res.next = h1
                h1 = h1.next
            else:
                res.next = h2
                h2 = h2.next
            res = res.next
        while h1:
            res.next = h1
            h1 = h1.next
            res = res.next
        while h2:
            res.next = h2
            h2 = h2.next
            res = res.next
        return temp.next

    def reverse(self, head):
        curr = head
        pre = None
        while(curr != None):
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1,n2=[int(x) for x in input().split()]
        
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        arr2=[int(x) for x in input().split()]
        ll2=Llist()
        tail=None
        for nodeData in arr2:
            tail=ll2.insert(nodeData,tail)
        
        
        ob = Solution()
        resHead=ob.mergeResult(ll1.head,ll2.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends