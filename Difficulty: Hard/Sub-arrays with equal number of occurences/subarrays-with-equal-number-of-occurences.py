#User function Template for python3

class Solution:
    def sameOccurrence(self, arr, x, y):
        # Initialize a hash map to store count of differences and number of occurrences
        diff_map = {0: 1}  # Starting with 0 difference at the beginning
        count = 0  # This will track the difference between occurrences of x and y
        result = 0  # This will store the total number of valid subarrays
        
        for num in arr:
            if num == x:
                count += 1
            elif num == y:
                count -= 1
            
            # Check if this count has been seen before
            if count in diff_map:
                result += diff_map[count]
            
            # Add/update the count in the map
            if count in diff_map:
                diff_map[count] += 1
            else:
                diff_map[count] = 1
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends