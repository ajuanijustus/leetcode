# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        layer = 0
        
        def bfs(root, layer):
            nonlocal ans
                        
            if not root:
                return 0
            try:
                ans[layer].append(root.val)
            except:
                ans.append([root.val])

            bfs(root.left, layer+1)
            bfs(root.right, layer+1)
            
        bfs(root, 0)
        return ans