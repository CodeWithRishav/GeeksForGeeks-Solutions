class Solution:
    #Function to find the maximum length of subarray with equal number
    #of 0s and 1s.
    def maxLen(self, arr):
        n = len(arr)
        #creating an array to store the sum of elements in arr.
        s = [0] * len(arr)

        #setting the first element of s based on the first element of arr.
        if (arr[0] == 0):
            s[0] = -1
        else:
            s[0] = 1

        #iterating over the rest of the elements in arr.
        for i in range(1, len(s)):

            #updating the sum based on the current element in arr.
            if (arr[i] == 0):
                s[i] = s[i - 1] - 1
            else:
                s[i] = s[i - 1] + 1

        #creating a dictionary to store the sum as the key and the index
        #as the value.
        d = dict()

        #variable to keep track of the maximum length of the subarray
        mx_len = 0

        #variable to keep track of the current index.
        i = 0

        #iterating over the elements in s.
        for j in s:

            #if the sum is 0, it means we have equal number of 0s and 1s
            #so we update the maximum length.
            if (j == 0):
                mx_len = max(mx_len, i + 1)

            #if the sum is already present in the dictionary, it means we
            #have a subarray with equal number of 0s and 1s, so we update
            #the maximum length.
            if (d.get(j) != None):
                mx_len = max(mx_len, i - d[j])

            #if the sum is not present in the dictionary, we add it with
            #the current index.
            else:
                d[j] = i

            #incrementing the index.
            i = i + 1

        #returning the maximum length.
        return mx_len


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends