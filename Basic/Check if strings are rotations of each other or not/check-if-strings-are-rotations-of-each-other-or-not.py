class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        
        #we concatenate first string to itself and check if other 
        #string occurs in it as substring. If yes, then it 
        #is rotated version and we return true else false.
        s=s1+s1
        if(len(s1)==len(s2) and s2 in s):
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s1=str(input())
        s2=str(input())
        if(Solution().areRotations(s1,s2)):
            print(1)
        else:
            print(0)
    
        
# } Driver Code Ends