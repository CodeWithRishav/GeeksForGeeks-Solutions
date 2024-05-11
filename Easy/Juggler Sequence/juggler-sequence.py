#User function Template for python3

class Solution:
    def jugglerSequence(self, n):
        l = [n]
        val = n
        while True:
            if val == 1:
                return l
            if val%2==0:
                val = int(val**0.5)
            else:
                val = int(val**1.5)
            l.append(val)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends