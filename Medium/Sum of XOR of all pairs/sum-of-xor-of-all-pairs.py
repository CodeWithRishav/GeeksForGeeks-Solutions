class Solution:
    def sumXOR(self, arr, n):
        sum_val = 0
        n = len(arr)
        for i in range(32):
            zc = 0  # Count of zeros
            oc = 0  # Count of ones

            # Individual sum at each bit position
            id_sum = 0

            for j in range(n):
                if arr[j] % 2 == 0:
                    zc += 1
                else:
                    oc += 1
                arr[j] //= 2

            # Calculating individual bit sum
            id_sum = oc * zc * (1 << i)

            # Final sum
            sum_val += id_sum

        return sum_val
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends