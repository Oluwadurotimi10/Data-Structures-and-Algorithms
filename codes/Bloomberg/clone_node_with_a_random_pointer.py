# Leetcode 138

# Approach 1, TC: O(n), SC: O(n)

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    curr = head
    old_to_new = {None: None}

    while curr:
        copy = Node(curr.val)
        old_to_new[curr] = copy
        curr = curr.next

    curr = head
    while curr:
        copy = old_to_new[curr]
        copy.next = old_to_new[curr.next]
        copy.random = old_to_new[curr.random]
        curr = curr.next
    return old_to_new[head]


# Approach 2, TC: O(n), SC: O(1)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # tweaking the originial LL by linking old node to new node
        curr = head
        while curr:
            next_node = curr.next
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = next_node

        # linking the new old o its random val using the old node
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # obtaining only the new nodes from the linked list
        curr = head
        dummy = clone = Node(0)
        while curr:
            next_node = curr.next.next
            copy = curr.next
            clone.next = copy
            clone = clone.next
            curr = next_node

        return dummy.next