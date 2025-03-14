# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root):
        return max(self.helper(root.right, True, 0), self.helper(root.left, False, 0))

    def helper(self, node, isRight, depth):
        if not node:
            return depth
        
        if isRight:
            return max(
                depth,
                self.helper(node.left, False, depth+1),
                self.helper(node.right, True, 0)
            )
        else:
            return max(
                depth,
                self.helper(node.right, True, depth+1),
                self.helper(node.left, False, 0)
            )
            
        