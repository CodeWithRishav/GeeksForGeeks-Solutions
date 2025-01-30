#User function Template for python3

class Solution:

    def __init__(self):
        self.result = []
        self.row = [0] * 10

    # Function to check if it is safe to place a queen at position (r, c)
    def place(self, r, c):
        for prev in range(c):
            # Check if there is any queen already present in the same row or same diagonal
            if self.row[prev] == r or abs(self.row[prev] - r) == abs(prev - c):
                return False
        return True

    # Backtracking function to find all possible solutions
    def bt(self, c, n):
        # No solutions possible for n = 2 or n = 3
        if n == 2 or n == 3:
            return
        if c == n:
            # Storing the positions of queens in the current solution
            self.result.append([self.row[i] + 1 for i in range(n)])
            return

        for i in range(n):
            if self.place(i, c):
                # Placing the queen at position (i, c)
                self.row[c] = i

                # Recursively solving for the next column
                self.bt(c + 1, n)

    # Function to solve the N-Queen problem
    def nQueen(self, n):
        self.result = []
        self.bt(0, n)
        return self.result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends