#User function Template for python3

import math
class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        arr_sum = sum(arr)
        square_sum = 0
        for num in arr:
            square_sum+=num*num
        elements_sum = arr_sum - (n*(n+1))//2
        elements_sum_square = elements_sum**2
        square_sum-= (n*(n+1)*(2*n+1))//6
        elements_product = (elements_sum_square-square_sum)
        elements_difference_square = square_sum-elements_product
        elements_difference = int(math.sqrt(elements_difference_square))
        first_element = (elements_sum+elements_difference)//2
        second_element = (elements_sum-elements_difference)//2
        # print(first_element, second_element)
        ans = []
        for i in range(n+1,-1,-1):
            if arr[i] == first_element:
                ans.append(second_element)
                ans.append(first_element)
                break
            if arr[i] == second_element:
                ans.append(first_element)
                ans.append(second_element)
                break
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends