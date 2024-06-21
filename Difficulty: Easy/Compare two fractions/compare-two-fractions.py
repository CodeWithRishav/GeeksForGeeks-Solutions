#User function Template for python3


class Solution:
    def compareFrac (self, s):
        
        s = s.replace(","," ").replace("/"," ")
        arr = s.split()
        
        a = (arr[0])
        b = (arr[1])
        c = (arr[2])
        d = (arr[3])
        
        if int(a)/int(b) == int(c) / int(d) :
            return "equal"
        elif int(a)/int(b) < int(c)/int(d):
            return c+"/"+d
        else:
            return a+"/"+b
        
        # code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends