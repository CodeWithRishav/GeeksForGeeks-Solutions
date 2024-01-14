class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        seen_rows = {}  # Dictionary to store unique rows and their first occurrence indices
        duplicate_rows = []

        for i in range(m):
            row_str = "".join(map(str, arr[i]))  # Convert row to string for efficient comparison
            if row_str in seen_rows:
                duplicate_rows.append(i)  # Add to duplicate list if already seen
            else:
                seen_rows[row_str] = i  # Store first occurrence index

        return duplicate_rows
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        arr = []
        for i in range(n):
            nums = list(map(int, input().strip().split()))
            arr.append(nums)
        ob = Solution()
        ans = ob.repeatedRows(arr, n, m)
        
        for x in ans:
            print(x, end=" ")
            
        print()
        tc -= 1

# } Driver Code Ends