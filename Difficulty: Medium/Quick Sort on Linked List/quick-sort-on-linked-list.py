#User function Template for python3

def quickSort(head):
    if head is None:
        return None

    #sorting linked list using quicksort algorithm

    h, t = mysort(head)
    t.next = None
    return h


def mysort(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    if head is None:
        return None, None

    #base cases
    #if head is the only node in the linked list
    if head and head.next is None:
        return head, head

    #partitioning the linked list based on head node
    left = None
    pleft = None
    right = None
    pright = None

    #keeping track of head node
    phead = head

    #setting p as the next node
    p = head.next

    #iterating over the linked list
    while p:
        if p.data < head.data:
            #if node value is less than head value, move it to the left partition
            if left is None:
                left = p
                pleft = p
                p = p.next
                pleft.next = None
            else:
                pleft.next = p
                pleft = p
                p = p.next
                pleft.next = None
        elif p.data > head.data:
            #if node value is greater than head value, move it to the right partition
            if right is None:
                right = p
                pright = p
                p = p.next
                pright.next = None
            else:
                pright.next = p
                pright = p
                p = p.next
                pright.next = None
        elif p.data == head.data:
            #if node value is equal to head value, move it to the end of the sorted list
            phead.next = p
            phead = p
            p = p.next
            phead.next = None

    #recursively sort the left and right partitions
    lhead, ltail = mysort(left)
    rhead, rtail = mysort(right)

    if lhead is None and rhead is None:
        #if both left and right partitions are empty, return head and phead as tail
        return head, phead
    if lhead is None and rhead is not None:
        #if left partition is empty and right partition is not empty, link phead to rhead
        phead.next = rhead
        return head, rtail
    elif lhead and rhead is None:
        #if left partition is not empty and right partition is empty, link ltail to head
        ltail.next = head
        return lhead, phead
    elif lhead and rhead:
        #if both left and right partitions are not empty, link ltail to head and phead to rhead
        ltail.next = head
        phead.next = rhead
        return lhead, rtail


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:

    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def nodeID(head, dic):
    while head:
        dic[head.data].append(id(head))
        head = head.next


def printList(head, dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Do'nt swap data, swap pointer/node")
            return
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        dic = defaultdict(list)  # dictonary to keep data and id of node
        nodeID(ll.head, dic)  # putting data and its id

        resHead = quickSort(ll.head)
        printList(resHead, dic)  #verifying and printing
        print()

        print("~")

# } Driver Code Ends