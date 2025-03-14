# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        cur_node = head

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_node
        return prev