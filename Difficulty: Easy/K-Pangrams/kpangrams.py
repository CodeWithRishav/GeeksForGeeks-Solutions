#User function Template for python3
class Solution:
    def kPangram(self, string, k):
        # Create a set to store unique alphabetic characters in the string
        unique_chars = set()
        
        # Traverse the string and add each character to the set
        for char in string:
            if char.isalpha():  # We only consider alphabetic characters
                unique_chars.add(char)
        
        # Count the number of unique characters
        unique_count = len(unique_chars)
        
        # Calculate the number of missing characters to make it a pangram
        missing_chars = 26 - unique_count
        
        # If the number of missing characters is less than or equal to k, and the string has at least 26 characters
        if missing_chars <= k and len([c for c in string if c.isalpha()]) >= 26:
            return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends