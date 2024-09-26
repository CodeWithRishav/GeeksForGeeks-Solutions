#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        if not arr:  # Check for empty input
            return 0
        
        max_steps = 0
        current_steps = 0
        
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                current_steps += 1  # Count this step
            else:
                max_steps = max(max_steps, current_steps)
                current_steps = 0  # Reset for the next sequence
        
        # Final check to update max_steps
        max_steps = max(max_steps, current_steps)
        
        return max_steps


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends