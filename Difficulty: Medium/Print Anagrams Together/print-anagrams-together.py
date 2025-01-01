#User function Template for python3


from collections import defaultdict


class Solution:
    # Function to find all anagrams in a given list of strings.
    def anagrams(self, s):
        # Creating a defaultdict to store anagrams.
        d = defaultdict(list)

        # Iterating over the given list of strings.
        for i, e in enumerate(s):
            # Sorting each string to form a key for grouping anagrams.
            e = str(sorted(e))
            # Appending the current string to its corresponding group.
            d[e].append(s[i])

        # Creating a list to store the groups of anagrams.
        res = []
        # Iterating over the values of the defaultdict.
        # Each value represents a group of anagrams.
        for l in d.values():
            # Appending the group of anagrams to the result list.
            res.append(l)

        # Returning the final list of groups of anagrams.
        return res
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends