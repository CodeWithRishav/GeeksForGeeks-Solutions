#User function Template for python3

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
class Solution:

    def findFirstNode(self, head):
        # Initialize two pointers, slow and fast
        slow = head
        fast = head

        # Traverse the list
        while fast and fast.next:

            # Move slow pointer by one step
            slow = slow.next

            # Move fast pointer by two steps
            fast = fast.next.next

            # Detect loop
            if slow == fast:

                # Move slow to head, keep
                # fast at meeting point
                slow = head

                # Move both one step at a time until
                # they meet
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                # Return the meeting node, which is the
                # start of the loop
                return slow

        # No loop found
        return None

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


def loop_here(head, tail, position):
    if position == 0:
        return

    walk = head
    for _ in range(1, position):
        walk = walk.next
    tail.next = walk


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        k = int(input())
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        loop_here(head, tail, k)

        ob = Solution()
        ans = ob.findFirstNode(head)
        if (ans == None):
            print(-1)
        else:
            print(ans.data)
        print("~")

# } Driver Code Ends