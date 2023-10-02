class Solution:
    def distinctSubsequences(self, S):
        # create an array to store index of last
        last = [-1]*26
        
        mod = 10**9+7
        
        # length of input string
        n = len(S)
        
        # dp[i] is going to store count of
        # discount subsequence of length of i
        dp = [-2 for i in range(n + 1)]
        
        # empty substring has only
        # one subseqence
        dp[0] = 1
        
        # Traverse through all lengths
        # from 1 to n
        for i in range(1, n + 1):
        
            # number of subseqence with
            # substring str[0...i-1]
            dp[i] = 2 * dp[i - 1]
            dp[i] %= mod
            
            # if current character has appeared
            # before, then remove all subseqences
            # ending with previous occurrence.
            if last[ord(S[i - 1])-97] != -1:
                dp[i] = dp[i] - dp[last[ord(S[i - 1])-97]]
                dp[i] %= mod
            last[ord(S[i - 1])-97] = i - 1
        
        return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends