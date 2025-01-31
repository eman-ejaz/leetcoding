# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)


        return






























        

        def dfs (node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            return 1 + max(left, right)

        return dfs(root)
























        def dfs1(node):
            if not node:
                return 0

            left = dfs1(node.left)
            right = dfs1(node.right)

            return 1 + max(left, right)

            # return 1 + max(dfs1(node.left), dfs1(node.right))

        return dfs1(root)



        if not root:
            return 0

        max_depth = [float('-inf')]

        def dfs(node, depth):
            if not node:
                return 0
            
            if not node.left and not node.right:
                max_depth[0] = max(depth + 1, max_depth[0])
                return
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return max_depth[0]
        