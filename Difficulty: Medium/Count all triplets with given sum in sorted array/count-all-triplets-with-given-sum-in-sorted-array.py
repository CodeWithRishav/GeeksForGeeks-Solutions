
class Solution:
    def countTriplets(self, arr, target):
        n=len(arr)
        ans=0
        for i in range(n-2):
            l,h=i+1,n-1
            val=target-arr[i]
            while l<h:
                curr=arr[l]+arr[h]
                if curr==val:
                    if arr[l]==arr[h]:
                        ans+=((h-l)*(h-l+1))//2
                        break
                    else:
                        temp1,temp2=1,1
                        while l<h and arr[l]==arr[l+1]:
                            temp1+=1
                            l+=1
                        l+=1
                        while l<h and arr[h]==arr[h-1]:
                            temp2+=1
                            h-=1
                        h-=1
                        ans+=temp1*temp2
                elif curr>val:
                    h-=1
                else:
                    l+=1
        return ans



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends