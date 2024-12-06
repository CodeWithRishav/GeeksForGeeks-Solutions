#User function Template for python3
class Solution:

    #Function to calculate h-index based on given citations.
    def hIndex(self, citations):
        papers = len(citations)
        citation_buckets = [0] * (papers + 1)

        #Creating buckets to store count of citations.
        for citation in citations:
            citation_buckets[min(citation, papers)] += 1

        cumulative_papers = 0

        #Iterating from maximum citations to 0 to find h-index.
        for h_index in range(papers, -1, -1):
            cumulative_papers += citation_buckets[h_index]

            #Checking if cumulative papers are greater than or equal to h-index.
            if cumulative_papers >= h_index:
                return h_index
        return 0

#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends