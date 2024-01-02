class Solution():
    def maxSumWithK(self, arr, n, k):
            # Code here
            def kadanes(arr):
                ans = []
                sumi = 0
                for i in range(n):
                    sumi += arr[i]
                    if sumi < 0:
                        ans.append(0)
                        sumi = 0 
                    else:
                        ans.append(sumi)
                return ans
                
            nums = kadanes(arr)
            # print(nums)
            currsum = 0
            j = 0
            for i in range(k):
                currsum += arr[i]
                j+=1
            maxsum = float("-inf")
            maxsum = max(currsum, maxsum)
            # print(maxsum)
            i = 0
            while(j < n) :
                currsum -= arr[i]
                currsum += arr[j]
                # currsum += nums[i] 
                maxsum = max(maxsum, currsum + nums[i])
                j+=1
                i+=1
            return maxsum
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends