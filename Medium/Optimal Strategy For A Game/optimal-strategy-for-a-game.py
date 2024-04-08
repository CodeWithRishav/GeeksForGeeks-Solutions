#User function Template for python3


#Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self, n, arr):
        self.memorize = [[-1 for _ in range(n)] for _ in range(n)]
        return self.maximumAmountHelper(arr, 0, n - 1)
        
        
    def maximumAmountHelper(self, arr, left_i, right_i):
        
        if left_i > right_i:
            return 0
        if left_i == right_i:
            return arr[left_i]

        if self.memorize[left_i][right_i] != -1:
            return self.memorize[left_i][right_i]

            
        # Else usual case
        take_left = arr[left_i] + min( self.maximumAmountHelper(arr, left_i+2, right_i), \
                                        self.maximumAmountHelper(arr, left_i+1, right_i-1) )
                                        
        take_right = arr[right_i] + min( self.maximumAmountHelper(arr, left_i, right_i-2), \
                                        self.maximumAmountHelper(arr, left_i+1, right_i-1) )
        
        best_move = max(take_left, take_right)
                                        
        if self.memorize[left_i][right_i] == -1:
            self.memorize[left_i][right_i] = best_move
        
        return best_move


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(n,arr))

# } Driver Code Ends