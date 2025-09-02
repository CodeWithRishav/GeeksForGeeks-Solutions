class Solution:

    def swapKth(self, head, k):
        if not head:
            return head

        # Count length
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next

        # if k is more than length, no swap
        if k > n:
            return head

        # if kth from start and end are same, no swap
        if 2 * k - 1 == n:
            return head

        # find kth node from start and its prev
        prevX = None
        x = head
        for i in range(1, k):
            prevX = x
            x = x.next

        # find kth node from end and its prev
        prevY = None
        y = head
        for i in range(1, n - k + 1):
            prevY = y
            y = y.next

        # adjust previous pointers
        if prevX:
            prevX.next = y
        if prevY:
            prevY.next = x

        # swap next pointers
        tempNext = x.next
        x.next = y.next
        y.next = tempNext

        # change head if needed
        if k == 1:
            head = y
        if k == n:
            head = x

        return head