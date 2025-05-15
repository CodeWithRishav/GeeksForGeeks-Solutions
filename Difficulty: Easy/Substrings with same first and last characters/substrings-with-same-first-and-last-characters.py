class Solution:

    def countSubstring(self, s):
        n = len(s)

        # Create an array to store
        # frequency of characters
        freq = [0] * 26

        # Update frequency of each character
        for i in range(n):
            freq[ord(s[i]) - ord('a')] += 1

        count = 0

        # For each character, calculate number of substrings
        # that start and end with that character
        for i in range(26):

            # Number of substrings with same
            # first and last character is
            # nC2 + n = n*(n+1)/2
            count += (freq[i] * (freq[i] + 1)) // 2

        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends