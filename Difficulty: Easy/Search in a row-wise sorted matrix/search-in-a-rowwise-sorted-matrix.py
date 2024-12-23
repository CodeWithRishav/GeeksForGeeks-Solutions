
#User function Template for python3

class Solution:
    # Function to search a given number in a row-wise sorted matrix.
    def searchRowMatrix(self, mat, x):
        n = len(mat)  # Number of rows

        for row in mat:
            left, right = 0, len(row) - 1

            # Perform binary search in the current row
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] == x:
                    return 1  # Found the target
                elif row[mid] < x:
                    left = mid + 1  # Search in the right half of the row
                else:
                    right = mid - 1  # Search in the left half of the row
        return 0  # Element not found in any row
    	



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
        if ob.searchRowMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends