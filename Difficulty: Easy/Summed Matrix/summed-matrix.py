#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        if q == 0:
            return -1
        if q > n*2 or q < 2:
            return 0
        dist_frm_strt = q-1
        dist_frm_end = n*2 - (q-1)
        if dist_frm_strt == dist_frm_end:
            return n
        else:
            val = min([dist_frm_strt, dist_frm_end])
            return val


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends