#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    # Function to calculate the span of stock's price for all n days.
    def calculateSpan(self, arr):
        n = len(arr)
        s = []
        s.append(0)
        S = [0] * n

        # Span value of first day is always 1.
        S[0] = 1

        for i in range(1, n):
            # We pop elements from the stack till price at top of stack
            # is less than or equal to current price.
            while s and arr[s[-1]] <= arr[i]:
                s.pop()

            # If stack becomes empty, then price[i] is greater than all
            # elements on left of it in list so span is i+1.
            # Else price[i] is greater than elements after value at top of stack.
            span = (i + 1) if not s else (i - s[-1])
            S[i] = span

            # Pushing this element to stack.
            s.append(i)
        # Returning the list.
        return S
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends