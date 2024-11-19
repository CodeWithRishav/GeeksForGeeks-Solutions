#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        flag=0
        for i in range(len(arr)-2,-1,-1):
            if arr[i]<arr[i+1]:
                flag=1
                break
        if flag:
            cur=[float('inf'),0]
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i] and arr[j]<cur[0]:
                    cur=[arr[j],j]
            if cur[0]!=float('inf'):
                arr[i],arr[cur[1]]=arr[cur[1]],arr[i]
        if i==0 and not flag:
            i-=1
        temp=sorted(arr[i+1:])
        res=arr[:i+1]+temp
        arr.clear()
        arr.extend(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends