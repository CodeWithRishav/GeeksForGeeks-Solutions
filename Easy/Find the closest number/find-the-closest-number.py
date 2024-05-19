
from typing import List


class Solution:
    def findClosest(self, n, target, arr):
        # Method to compare which one is the more close.
        # We find the closest by taking the difference between the target and both values. 
        # It assumes that val2 is greater than val1 and target lies between these two.
        def getClosest(val1, val2, target):
         
            if (target - val1 >= val2 - target):
                return val2
            else:
                return val1
        # Corner cases
        if (target <= arr[0]):
            return arr[0]
        if (target >= arr[n - 1]):
            return arr[n - 1]
     
        # Doing binary search
        i = 0; j = n; mid = 0
        while (i < j): 
            mid = (i + j) // 2
     
            if (arr[mid] == target):
                return arr[mid]
     
            # If target is less than array element, then search in left
            if (target < arr[mid]) :
     
                # If target is greater than previous to mid, return closest of two
                if (mid > 0 and target > arr[mid - 1]):
                    return getClosest(arr[mid - 1], arr[mid], target)
     
                # Repeat for left half 
                j = mid
             
            # If target is greater than mid
            else :
                if (mid < n - 1 and target < arr[mid + 1]):
                    return getClosest(arr[mid], arr[mid + 1], target)
                     
                # update i
                i = mid + 1
             
        # Only single element left after search
        return arr[mid]
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends