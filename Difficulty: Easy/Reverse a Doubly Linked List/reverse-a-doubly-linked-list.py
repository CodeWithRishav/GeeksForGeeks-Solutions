class Solution:

    def reverse(self, head):
        # If the list is empty or has only one node,
        # return the head as is
        if head is None or head.next is None:
            return head

        prevNode = None
        currNode = head

        # Traverse the list and reverse the links
        while currNode is not None:
            # Swap the next and prev pointers
            prevNode = currNode.prev
            currNode.prev = currNode.next
            currNode.next = prevNode

            # Move to the next node in the original list
            # (which is now previous due to reversal)
            currNode = currNode.prev

        # The final node in the original list
        # becomes the new head after reversal
        return prevNode.prev