#User function Template for python3

class Node:

    def __init__(self):
        self.one = None
        self.zero = None


class Trie:

    def __init__(self):
        self.root = Node()

    # Function to insert in Trie
    def insert(self, n):
        curr = self.root
        for i in range(31, -1, -1):
            bit = (n >> i) & 1

            # Check if the bit is 0
            if bit == 0:
                if not curr.zero:
                    curr.zero = Node()
                curr = curr.zero

            # Else if bit is 1
            else:
                if not curr.one:
                    curr.one = Node()
                curr = curr.one

    # Function to find element having
    # the maximum XOR with value n
    def findXOR(self, n):
        curr = self.root
        res = 0

        for i in range(31, -1, -1):
            bit = (n >> i) & 1

            # if the bit is 0
            if bit == 0:

                # if set bit is present
                if curr.one:
                    curr = curr.one
                    res += (1 << i)
                else:
                    curr = curr.zero

            # Else if bit is 1
            else:

                # if unset bit is present
                if curr.zero:
                    curr = curr.zero
                    res += (1 << i)
                else:
                    curr = curr.one
        return res


class Solution:

    def maxXor(self, arr):
        res = 0
        t = Trie()

        # insert the first element in trie
        t.insert(arr[0])

        for i in range(1, len(arr)):
            res = max(t.findXOR(arr[i]), res)
            t.insert(arr[i])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxXor(arr))
        print("~")

# } Driver Code Ends