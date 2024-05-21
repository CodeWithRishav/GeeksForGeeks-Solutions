#User function Template for python3

import heapq
class Solution:
    def printKClosest(self, arr, n, k, x):
        # code here
        pq1 = []
        pq2 = []
    
        for i in range(n):
            if x == arr[i]: continue
            if x < arr[i]:
                heapq.heappush(pq1, (abs(x-arr[i]), i))
            else:
                heapq.heappush(pq2, (abs(x-arr[i]),i))
    
        heapq.heappush(pq1, (1000000007,-1))
        heapq.heappush(pq2, (1000000007,-1))
    
        ans = []
    
        while len(ans) < k:
            dif1 = pq1[0][0]
            dif2 = pq2[0][0]
    
            if dif1 <= dif2:
                ans.append(arr[pq1[0][1]])
                heapq.heappop(pq1)
            else:
                ans.append(arr[pq2[0][1]])
                heapq.heappop(pq2)
    
        return ans
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends