#User function Template for python3
class TrieNode:

    def __init__(self):
        # Array to store child nodes for each character ('a' to 'z')
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        current = self.root
        for c in word:
            index = ord(c) - ord('a')

            # If character doesn't exist, create a new node
            if current.children[index] is None:
                current.children[index] = TrieNode()
            current = current.children[index]

        # Mark the end of the word
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')

            # If character doesn't exist, return false
            if current.children[index] is None:
                return False
            current = current.children[index]

        return current.isEndOfWord

    def isPrefix(self, word: str) -> bool:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')

            # If character doesn't exist, return false
            if current.children[index] is None:
                return False
            current = current.children[index]

        return True


#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        q = int(input())
        ans = []
        trie = Trie()

        for _ in range(q):
            x, s = input().split()
            x = int(x)

            if x == 1:
                trie.insert(s)
            elif x == 2:
                ans.append(trie.search(s))
            elif x == 3:
                ans.append(trie.isPrefix(s))

        # Print results as lowercase true/false
        print(" ".join(["true" if res else "false" for res in ans]))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends