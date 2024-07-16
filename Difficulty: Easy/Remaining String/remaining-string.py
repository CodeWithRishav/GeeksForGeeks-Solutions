#User function Template for python3
class Solution:
    def printString(self, s, ch, count):
        occurrence = 0  # Initialize the occurrence count
        
        for i in range(len(s)):
            if s[i] == ch:
                occurrence += 1  # Increment the count when the character is found
            if occurrence == count:
                return s[i + 1:]  # Return the substring after the nth occurrence of the character
        
        return ""


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends