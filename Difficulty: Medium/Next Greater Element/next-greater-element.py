# User function Template for python3

from collections import deque


class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        n = len(arr)  # Define the length of the array
        s = deque()
        res = [0] * n  # Initialize the result list with size n

        # Traversing the array from the last element in backward direction.
        for i in range(n - 1, -1, -1):
            # While element at the top of the stack is less than or equal to
            # current array element, pop elements from the stack.
            while len(s) and s[-1] <= arr[i]:
                s.pop()

            # If stack becomes empty, store -1 in the result list
            # else store the top element of the stack.
            res[i] = -1 if not len(s) else s[-1]

            # Push the current array element into the stack.
            s.append(arr[i])

        # Returning the result list.
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends