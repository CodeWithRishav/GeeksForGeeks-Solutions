#{ 
 # Driver Code Starts

# } Driver Code Ends

class Solution:
    def rearrange(self, arr):
        n = len(arr)
        
        for i in range(n):
            if arr[i] >= n or arr[i] < 0:
                arr[i] = -1
                
        
        i = 0
        while i < n:
            if arr[i] != -1 and arr[i] != i:
                temp = arr[arr[i]]
                arr[arr[i]] = arr[i]
                arr[i] = temp 
            else:
                i += 1
                
        return arr
        #Code here

#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    for _ in range(t):
        input_str = input()
        arr = list(map(int, input_str.split()))
        solution = Solution()
        ans = solution.rearrange(arr)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
# } Driver Code Ends