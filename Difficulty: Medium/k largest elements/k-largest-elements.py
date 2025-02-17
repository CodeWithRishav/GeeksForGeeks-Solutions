import heapq


class Solution:
    #Function to find the k largest elements using a priority queue.
    def kLargest(self, arr, k):
        n = len(arr)
        pq = []  #initialize the priority queue

        #iterate through the array
        for num in arr:
            if len(pq) == k:  #if priority queue size is equal to k
                if pq[0] < num:  #if the smallest element in the priority queue is smaller than the current element
                    heapq.heappop(
                        pq
                    )  #remove the smallest element from the priority queue
                    heapq.heappush(
                        pq,
                        num)  #push the current element into the priority queue
            else:
                heapq.heappush(
                    pq, num
                )  #if priority queue size is less than k, push the current element into the priority queue

        ans = []  #initialize the result list
        while pq:  #while priority queue is not empty
            ans.append(
                heapq.heappop(pq)
            )  #pop the smallest element from the priority queue and append it to the result list

        return ans[::
                   -1]  #return the reversed result list to get the k largest elements in descending order


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kLargest(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends