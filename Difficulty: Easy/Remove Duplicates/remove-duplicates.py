#User function Template for python3
class Solution:
    def removeDups(self, str):
        str1= '';
        for i in str:
            if i not in str1:
                str1+=i;
        return str1 ;


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends