# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return (0, True)

            left, lunb = dfs(node.left)
            right, rung = dfs(node.right)

            subt = abs(left - right)
            balanced = subt <= 1

            h = 1 + max(left, right)

            return (h, (balanced and lunb) and (balanced and rung))

        
        res = dfs(root)
        return res[1]




























        result = [True]
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                result[0] = False

            return 1 + max(left, right)
    
        dfs(root)
        return result[0]
            
        