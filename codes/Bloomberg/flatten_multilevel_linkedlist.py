# Leetcode 430

# TC - O(
def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
    curr = head
    stack = []

    while curr:
        # checking if the current node has a child
        if curr.child:
            if curr.next:
                # adding the next of node with child to a stack, to come back to it later
                stack.append(curr.next)
                curr.next.prev = None
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
        if curr.next:
            curr = curr.next
        else:
            break

    while stack:
        curr.next = stack.pop()
        curr.next.prev = curr

        while curr and curr.next:
            curr = curr.next
    return head
