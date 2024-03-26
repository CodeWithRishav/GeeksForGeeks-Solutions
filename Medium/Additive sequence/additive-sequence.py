#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# return 1 in case of True and 0 in case of False
class Solution:
    def isAdditiveSequence(self, num):
        def is_valid_sequence(num1, num2, remaining):
            if not remaining:  # If no remaining digits, return True
                return True
            sum_num = str(num1 + num2)  # Calculate the sum of num1 and num2
            if remaining.startswith(sum_num):  # Check if the sum is a prefix of remaining digits
                return is_valid_sequence(num2, int(sum_num), remaining[len(sum_num):])  # Recursively check the remaining digits
            return False

        length = len(num)
        for i in range(1, length):  # Try all possible splits for the first two numbers
            for j in range(i + 1, length):  # Try all possible splits for the second number
                num1 = int(num[:i])  # Extract the first number
                num2 = int(num[i:j])  # Extract the second number
                if is_valid_sequence(num1, num2, num[j:]):  # Check if it forms a valid sequence
                    return 1
        return 0
        #code here

#{ 
 # Driver Code Starts.
        
if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        s = input()
        print(sol.isAdditiveSequence(s))

# } Driver Code Ends