#User function Template for python3

# design the class in the most optimal way

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.pre = None


class LRUCache:
    hsmap = dict()
    capacity = count = 0
    head = tail = None

    #Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        self.hsmap = dict()
        self.capacity = cap
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.head.pre = None
        self.tail.next = None
        self.tail.pre = self.head
        count = 0

    def addToHead(self, node):
        node.next = self.head.next
        node.next.pre = node
        node.pre = self.head
        self.head.next = node

    #Function to delete a node.
    def deleteNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    #Function to return value corresponding to the key.
    def get(self, key):

        #if element is present in map,
        if key in self.hsmap:

            node = self.hsmap[key]
            result = node.value
            self.deleteNode(node)
            self.addToHead(node)

            #returning the value.
            return result

        #else we return -1.
        else:
            return -1

    #Function for storing key-value pair.
    def put(self, key, value):

        if key in self.hsmap:

            node = self.hsmap[key]
            node.value = value
            self.deleteNode(node)
            self.addToHead(node)
        else:
            node = Node(key, value)
            self.hsmap[key] = node

            if self.count < self.capacity:
                self.count += 1
                self.addToHead(node)
            else:
                self.hsmap.pop(self.tail.pre.key)
                self.deleteNode(self.tail.pre)
                self.addToHead(node)




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends