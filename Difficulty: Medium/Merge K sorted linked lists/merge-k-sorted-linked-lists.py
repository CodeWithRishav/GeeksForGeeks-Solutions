#User function Template for python3
'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
class Solution:

    def mergeKLists(self, arr):
        pq = []

        # Insert the head nodes of k lists
        for i in range(0, len(arr)):
            head = arr[i]
            if head is not None:
                heapq.heappush(pq, (head.data, i, head))

        # Initialize a dummy head
        dummy = Node(-1)
        tail = dummy

        while pq:

            # Pop the min node
            _, index, top = heapq.heappop(pq)

            # Append the node into list
            tail.next = top
            tail = top

            # If top node has next node,
            # add it to the heap.
            if top.next is not None:
                heapq.heappush(pq, (top.next.data, index, top.next))

        return dummy.next


#{ 
 # Driver Code Starts
import heapq


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

    # To compare nodes in the heap
    def __lt__(self, other):
        return self.data < other.data


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lists = []
        for _ in range(n):
            values = list(map(int, input().split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.next = newNode
                    temp = temp.next
            lists.append(head)

        sol = Solution()
        head = sol.mergeKLists(lists)
        printList(head)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends