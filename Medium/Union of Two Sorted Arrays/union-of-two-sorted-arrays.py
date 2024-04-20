#User function Template for python3

class Solution:
    def findUnion(self,arr1,arr2,n,m):
        
        set_arr1 = set(arr1)
        set_arr2 = set(arr2)
        
        merged_set = set_arr1.union(set_arr2)
        
        merged_arr = list(merged_set)
        
        merged_arr.sort()
        
        return merged_arr
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends