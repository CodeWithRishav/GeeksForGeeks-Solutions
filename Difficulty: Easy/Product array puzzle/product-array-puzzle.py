#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        c0 = nums.count(0)
        if (c0 == 1):
            p = 1
            for i in nums:
                if i != 0:
                    p = p*i
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = p
            return nums
        elif c0==len(nums):
            return nums
        elif c0>1:
            for i in range(len(nums)):
                nums[i] = 0
            return nums
        else:
            p = 1
            for i in nums:
                p = p*i
            for i in range(len(nums)):
                nums[i] = p//nums[i]
            return nums


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends