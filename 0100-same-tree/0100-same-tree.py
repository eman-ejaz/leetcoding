# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)












        def dfs(p, q):
            if not p and not q:
                return True


            if not p and q:
                return False
            
            if not q and p:
                return False

            if (not p.left and not p.right) and (not q.left and not q.right):
                return p.val == q.val

            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            return left and right and (q.val == p.val)

        return dfs(p, q)
































        if not p and not q:
            return True

        if (p and not q) or (q and not p):
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))


























        if not p and not q:
            return True

        if (not p and q) or (not q and p):
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))