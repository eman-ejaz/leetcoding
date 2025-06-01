# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if (p.val != q.val):
                return False
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        
        def dfs(p):
            if not p:
                return False

            tempP = p
            tempQ = subRoot

            res = sameTree(tempP, tempQ)

            if res:
                return True

            return dfs(p.left) or dfs(p.right)

        
        return dfs(root)
