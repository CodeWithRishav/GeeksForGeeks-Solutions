from collections import Counter
# Solution 1
class Solution1:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        times=len(arr)//3
        freq=Counter(arr)
        ans=[]
        
        for key, value in freq.items():
            if value > times:
                ans.append(key)
        if not ans:
            return []
        
        ans.sort()
        return ans
 
 
# Solution 2
class Solution:      
    def findMajority(self, arr):
        n=len(arr)
        uniq=set(arr)
        new_arr=[]
        
        for i in uniq:
            count=0
            for j in range(n):
                if i == arr[j]:
                    count +=1
            if count > n/3:
                new_arr.append(i)
                
        new_arr.sort()
        if new_arr:
            return new_arr
        else:
            return []
        








#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends