# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(t1, t2):
            if not t1 and not t2:
                return True
            if t1 and t2 and t1.val == t2.val:
                return isSametree(t1.right, t2.right) and isSametree(t1.left, t2.left)
            else:
                return False
            
        if not root:
            return False
        
        if isSametree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)