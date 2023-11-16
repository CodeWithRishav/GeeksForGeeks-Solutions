class Solution:
    
    # Function to perform depth-first search and find the string
    def dfs(self, ans, d, tot, N, K):
        global res
        if len(d)==tot: # if all combinations have been tried
            res = ans
            return True
        tmp = ""
        if N>1:
            tmp = ans[len(ans)-N+1:] # get the last N-1 characters of the current string
        
        for i in range(K): # iterate through all possible characters
            tmp += chr(48+i) # add the character to the current string
            if tmp not in d: # check if the current string is unique
                ans += chr(48+i) # add the character to the final answer
                d[tmp] = 1 # mark the current string as used
                
                # recursively call dfs with the updated answer and dictionary
                if self.dfs(ans,d,tot,N,K):
                    return True
                
                d.pop(tmp) # remove the current string from the dictionary
                ans = ans[0:len(ans)-1] # remove the character from the final answer
            tmp = tmp[0:len(tmp)-1] # remove the last character from the current string
        
        return False
    
    # Function to find the string of length N with K possible characters
    def findString(self, N, K):
        if N==1: # if N is 1, return a string of all possible characters
            r = ""
            for i in range(K):
                r += chr(i+48)
            return r
        tot = pow(K,N) # total number of possible combinations
        ans = '0'*(N) # initialize the answer with N '0' characters
        d = dict() # dictionary to store used strings
        d[ans] = 1 # mark the initial string as used
        self.dfs(ans,d,tot,N,K) # call dfs to find the string
        return res # return the result string


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())

        ob = Solution()
        ans = ob.findString(N,K)
        ok = 1
        for i in ans:
            if ord(i)<48 or ord(i)>K-1+48:
                ok = 0
        if not ok:
            print(-1)
            continue
        d = dict()
        i = 0
        while i+N-1<len(ans):
            d[ans[i:i+N]] = 1
            i += 1
        tot = pow(K,N)
        if len(d)==tot:
            print(len(ans))
        else:
            print(-1)
# } Driver Code Ends