#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends


class Solution:

    def evaluate(self, arr):
        stack = []
        for token in arr:
            if token[-1].isdigit():  # Check if the token is a number
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    stack.append(int(num1 / num2))  # Perform integer division
        return stack[-1]


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        solution = Solution()
        print(solution.evaluate(arr))
        print("~")

# } Driver Code Ends