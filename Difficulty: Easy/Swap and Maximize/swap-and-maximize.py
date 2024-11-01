#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        l = []
        for i in range(len(arr)):
            if i%2==0:
                l.append(arr.pop(0))
            else:
                l.append(arr.pop())
        c = 0
        for i in range(1,len(l)):
            c += abs(l[i]-l[i-1])
        c += abs(l[-1]-l[0])
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends