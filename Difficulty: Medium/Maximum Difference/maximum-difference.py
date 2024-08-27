class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        
        # Initialize arrays for left and right smaller elements
        left_smaller = [0] * n
        right_smaller = [0] * n
        
        # Stack for left smaller elements
        stack = []
        
        # Find the nearest left smaller element for each element
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                left_smaller[i] = stack[-1]
            else:
                left_smaller[i] = 0
            stack.append(arr[i])
        
        # Clear the stack to reuse it for right smaller elements
        stack = []
        
        # Find the nearest right smaller element for each element
        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                right_smaller[i] = stack[-1]
            else:
                right_smaller[i] = 0
            stack.append(arr[i])
        
        # Find the maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(left_smaller[i] - right_smaller[i]))
        
        return max_diff


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends