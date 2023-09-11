# Leetcode 148

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        slow.next = None

        left, right = self.sortList(head), self.sortList(start)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = l = ListNode(0)
        while left and right:
            if left.val < right.val:
                l.next = left
                left = left.next

            else:
                l.next = right
                right = right.next
            l = l.next
        l.next = left or right
        return dummy.next