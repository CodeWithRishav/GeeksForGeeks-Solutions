#User function Template for python3

class Solution:
    # Function to return the count of number of elements in the union of two arrays.
    def findUnion(self, a, b):

        # Using set to store the elements.
        hs = set()

        # Insert all the elements of the first array into the set.
        for x in a:
            hs.add(x)

        # Insert all the elements of the second array into the set.
        # Set does not contain duplicates.
        for y in b:
            hs.add(y)

        # Returning the size of the set which is the total number of elements in the set.
        return len(hs)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.findUnion(a, b))
        print("~")

# } Driver Code Ends