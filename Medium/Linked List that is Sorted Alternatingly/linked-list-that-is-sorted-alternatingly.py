#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def sort(self, h1):
        #return head
        arr=[]
        while h1:
            arr.append(h1.data)
            h1 = h1.next 
            
        #print(arr)
        e=[]
        o=[]
        for i in  range(len(arr)):
            if i%2==0 :
                e.append(arr[i])
            else : 
                o.append(arr[i])
            
        o=o[::-1]
        e.extend(o)
        #print(o)
        for i in range(len(e)):
            print(e[i], end=" ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends