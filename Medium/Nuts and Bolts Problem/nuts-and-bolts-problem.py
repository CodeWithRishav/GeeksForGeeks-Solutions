#User function Template for python3
class Solution:

    def matchPairs(self, n, nuts, bolts):
        l=[0]*9
        dic={'!':0,'#':1,'$':2,'%':3,'&':4,'*':5,'?':6,'@':7,'^':8 }
        for i in nuts:
            if i in dic:
                temp=dic[i]
                l[temp]=i
        
        j=0
        for i in l:
            if i!=0:
                nuts[j]=i
                bolts[j]=i
                j+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends