class Solution:
    def search(self, pat, txt):
        l = 0
        indexs = []

        while l < len(txt):
            if txt[l] == pat[0] and txt[l:l+len(pat)] == pat:
                    indexs.append(l + 1)
            l += 1

        if indexs:
            return indexs
        else:
            return [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends