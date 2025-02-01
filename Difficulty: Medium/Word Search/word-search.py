class Solution:
    def isWordExist(self, mat, word):
        #Code here
        
        ROW = len(mat)
        COL = len(mat[0])
        n = len(word)
        visit = set()
        def valid(r,c):
            if r >= 0 and c >= 0 and r < ROW and c < COL:
                return True
            return False
        
        def fun(r,c,index):
            if index == len(word)-1:
                return True
            
            pos = [[r-1,c], [r+1,c], [r,c-1],[r,c+1]]
            visit.add((r,c))
            for nr,nc in pos:
                if valid(nr,nc) and index +1 < n and  mat[nr][nc] == word[index+1] and (nr,nc) not in visit and fun(nr,nc,index+1):
                    return True
            visit.remove((r,c))
            return False
        
        for r in range(ROW):
            
            for c in range(COL):
                
                if mat[r][c] == word[0] and fun(r,c,0):
                    return True
        return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends