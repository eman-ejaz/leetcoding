# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        
        dfs(root)

        return self.res






























        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.res



















        # maxi = [0]

        # def find_longest(node):
        #     if not node:
        #         return 0

        #     left = find_longest(node.left)
        #     right = find_longest(node.right)

        #     return 1 + max(left,  right)

        # def dfs(node):
        #     if not node:
        #         return

        #     left = find_longest(node.left)
        #     right = find_longest(node.right)
        #     maxi[0] = max(maxi[0], left + right)

        #     dfs(node.left)
        #     dfs(node.right)

        
        # dfs(root)
        # return maxi[0]





























        maxi = [0]
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            d = left + right

            maxi[0] = max(maxi[0], left + right)

            height = 1 + max(left, right)


            return height

        dfs(root)
        return maxi[0]


 