class Solution:

    def mergeKLists(self, arr):
        pq = []

        # Insert the head nodes of k lists
        for i in range(0, len(arr)):
            head = arr[i]
            if head is not None:
                heapq.heappush(pq, (head.data, i, head))

        # Initialize a dummy head
        dummy = Node(-1)
        tail = dummy

        while pq:

            # Pop the min node
            _, index, top = heapq.heappop(pq)

            # Append the node into list
            tail.next = top
            tail = top

            # If top node has next node,
            # add it to the heap.
            if top.next is not None:
                heapq.heappush(pq, (top.next.data, index, top.next))

        return dummy.next