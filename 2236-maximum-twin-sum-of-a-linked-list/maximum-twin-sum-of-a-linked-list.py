# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        max_val = 0
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur, prev = slow, None

        while cur:
           cur.next, prev, cur  =prev, cur, cur.next

        while prev:
            max_val = max(max_val, prev.val+head.val)
            prev = prev.next
            head = head.next
        return max_val