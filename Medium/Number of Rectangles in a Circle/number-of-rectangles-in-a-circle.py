#User function template for Python

class Solution:
    def rectanglesInCircle(self,radius):
        #code here
        rectangles=0
        diameter = 2 * radius
        diameterSquare = diameter * diameter
        
        for l in range(1,2 * radius):
            for w in range(1,2 * radius):
                
                diagonalLengthSquare =(l * l + w * w)
                
                if (diagonalLengthSquare <= diameterSquare):
                    rectangles +=1
        return rectangles

#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends