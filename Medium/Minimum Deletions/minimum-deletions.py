class Solution:
    # Returns the length of 
    # the longest palindromic 
    # subsequence in 'str'
    def lps(self, str):
        n = len(str)
     
        # Create a table to store
        # results of subproblems
        L = [[0 for x in range(n)]for y in range(n)]
     
        # Strings of length 1
        # are palindrome of length 1
        for i in range(n):
            L[i][i] = 1
     
        # Build the table. Note that 
        # the lower diagonal values 
        # of table are useless and 
        # not filled in the process. 
        # c1 is length of substring
        for cl in range( 2, n+1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if (str[i] == str[j] and cl == 2):
                    L[i][j] = 2
                elif (str[i] == str[j]):
                    L[i][j] = L[i + 1][j - 1] + 2
                else:
                    L[i][j] = max(L[i][j - 1],L[i + 1][j])
     
        # length of longest
        # palindromic subseq
        return L[0][n - 1]
        
    def minimumNumberOfDeletions(self, S):
        n = len(S)
 
        # Find longest palindromic 
        # subsequence
        l = self.lps(S)
     
        # After removing characters 
        # other than the lps, we 
        # get palindrome.
        return (n - l)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends