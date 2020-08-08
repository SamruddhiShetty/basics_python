# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
            maxi=0
            def samepath(root):
                if root:
                    left=samepath(root.left)
                    right=samepath(root.right)
                
                    left_length=left+1 if root.left and root.val==root.left.val else 0
                    right_length=right+1 if root.right and root.val==root.right.val else 0
                    nonlocal maxi
                    maxi=max(maxi, left_length+right_length)
                
                    return max(left_length, right_length)
                
                
                else:
                    return 0
            samepath(root)
            return maxi
        
