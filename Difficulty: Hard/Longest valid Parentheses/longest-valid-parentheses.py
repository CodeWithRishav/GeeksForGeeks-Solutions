# User function Template for Python3

class Solution:
    def maxLength(self, str):
        stack = [-1]
        count = 0
        for i, char in enumerate(str):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    count = max(count, i - stack[-1])
        
        return count


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))

# } Driver Code Ends