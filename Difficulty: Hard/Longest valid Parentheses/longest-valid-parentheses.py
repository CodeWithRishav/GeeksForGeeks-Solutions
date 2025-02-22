
class Solution:

    def maxLength(self, s):
        stack = []

        # Push -1 as the initial index to
        # handle the edge case
        stack.append(-1)
        maxLen = 0

        # Traverse the string
        for i in range(len(s)):

            # If we encounter an opening parenthesis,
            # push its index
            if s[i] == '(':
                stack.append(i)
            else:

                # If we encounter a closing parenthesis,
                # pop the stack
                stack.pop()

                # If stack is empty, push the current index
                # as a base for the next valid substring
                if not stack:
                    stack.append(i)
                else:

                    # Update maxLength with the current length
                    # of the valid parentheses substring
                    maxLen = max(maxLen, i - stack[-1])

        return maxLen


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends