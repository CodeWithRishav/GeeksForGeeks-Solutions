"""
Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.val=x
        self.next=None

"""

class Solution:

    def findPrimes(self, n):
        primes = [1] * (n + 1)
        primes[0] = 0
        primes[1] = 0
        i = 2
        while i * i <= n:
            if primes[i]:
                j = i * i
                while j <= n:
                    primes[j] = 0
                    j += i
            i += 1
        return primes

    # Function to find the closest prime numbers for each node in a linked list
    def primeList(self, head):
        maxNum = 0
        temp = head
        while temp is not None:
            maxNum = max(maxNum, temp.val)
            temp = temp.next

        primes = self.findPrimes(2 * maxNum)

        temp = head
        while temp is not None:
            num = temp.val

            if num == 1:
                temp.val = 2
            else:
                num1, num2 = num, num
                while not primes[num1]:
                    num1 -= 1
                while not primes[num2]:
                    num2 += 1

                if num - num1 > num2 - num:
                    temp.val = num2
                else:
                    temp.val = num1

            temp = temp.next

        return head
        



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.val = x
        self.next = None


def printList(node):
    while (node != None):
        print(node.val, end=" ")
        node = node.next
    print()


def inputList():

    val = [int(i) for i in input().strip().split()
           ]  #all data of linked list in a line
    head = Node(val[0])
    tail = head
    for i in range(1, len(val)):
        tail.next = Node(val[i])
        tail = tail.next
    return head


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        head = inputList()

        obj = Solution()
        res = obj.primeList(head)

        printList(res)

        print("~")

# } Driver Code Ends