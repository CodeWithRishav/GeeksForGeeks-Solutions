#User function Template for python3
class Solution:

    #Function to check if element x is present in the matrix.
    def matSearch(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        i = 0
        j = m - 1

        #iterating through the matrix
        while i < n and j >= 0:

            #if the current element is equal to x, return true
            if mat[i][j] == x:
                return True

            #if the current element is greater than x, move left
            if mat[i][j] > x:
                j -= 1

            #if the current element is less than x, move down
            else:
                i += 1

        #if x is not found in the matrix, return false
        return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.matSearch(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends