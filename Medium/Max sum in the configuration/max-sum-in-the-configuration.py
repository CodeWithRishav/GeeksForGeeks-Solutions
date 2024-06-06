#User function Template for python3

def max_sum(a,n):
    #code here
    total_sum=sum(a)
    max_sum=0
    for i in range(n):
        max_sum+=(i*a[i])
    
    first_ele=a[0]
    last_ele=a[n-1]
    curr_sum=max_sum
    for i in range(1,n):
        curr_sum+=first_ele
        curr_sum-=(last_ele*(n-1))
        curr_sum+=(total_sum-(first_ele+last_ele))
        max_sum=max(curr_sum,max_sum)
        first_ele=last_ele
        last_ele=a[n-i-1]
    return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends