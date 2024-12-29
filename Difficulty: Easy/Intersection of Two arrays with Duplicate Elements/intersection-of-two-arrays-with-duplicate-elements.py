
class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        hash_map = {}
        for num in a:
            hash_map[num] = True
            
        res = set()
        for num in b:
            if num in hash_map:
                res.add(num)
        
        return list(res) 


#{ 
 # Driver Code Starts
#Position this line where user code will be pasted.
t = int(input().strip())
while t > 0:
    t -= 1
    # Read first array
    a = list(map(int, input().strip().split()))

    # Read second array
    b = list(map(int, input().strip().split()))

    #input()  # to consume the empty line

    # ADD Solution initialization
    sln = Solution()

    # Assuming numberofElementsInIntersection function is defined in Solution
    res = sln.intersectionWithDuplicates(a, b)

    # Sort the result
    res.sort()

    # Print the result
    if not res:
        print("[]")
    else:
        print(" ".join(map(str, res)))

    print("~")

# } Driver Code Ends