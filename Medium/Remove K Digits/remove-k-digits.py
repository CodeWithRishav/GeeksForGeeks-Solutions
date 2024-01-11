class Solution:

    def removeKdigits(self, s, k):
        ans =[]
        for i in range(len(s)):
            while( ans and ans[-1]>s[i] and k):
                ans.pop()
                k-=1
            if len(ans)>0 or s[i]!="0":
                ans.append(s[i])
        while(ans and k):
            ans.pop()
            k-=1
        if not ans: return "0"
        return "".join(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends