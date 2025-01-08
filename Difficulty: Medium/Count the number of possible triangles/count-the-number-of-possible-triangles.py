#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        n = len(arr)
        #Sorting the input array.
        arr.sort()
        count = 0

        #Traversing the array.
        for i in range(n - 2):
            #Storing the third index starting from ith index in k.
            k = i + 2
            #Traversing all the elements after ith index.
            for j in range(i + 1, n):

                #Traversing all the elements after jth index to check if there
                #exists any element which can satisfy the condition of triangle
                #with the elements at ith, jth and kth index.
                while (k < n and arr[i] + arr[j] > arr[k]):
                    k += 1

                #Incrementing the count of triangles.
                if k > j:
                    count += k - j - 1

        #returning the count of triangles.
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends