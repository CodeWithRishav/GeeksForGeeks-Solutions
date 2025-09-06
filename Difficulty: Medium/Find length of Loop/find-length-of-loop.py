class Solution:
    # Returns count of nodes present in loop.
    def countNodes(self, node):
        res = 1
        curr = node
        while curr.next != node:
            res += 1
            curr = curr.next
        return res

    def lengthOfLoop(self, head):
        slow = head
        fast = head

        while slow is not None and fast is not None \
              and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            # If slow and fast meet at
            # some point then there is a loop
            if slow == fast:
                return self.countNodes(slow)

        # Return 0 to indicate that
        # there is no loop
        return 0