# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root] if root else [])
        depth = 0

        res = []


        while q:
            size = len(q)
            depth += 1
            for i in range(size):
                node = q.popleft()

                # if depth > 1 and i == size - 1 and node:
                #     res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)
        return res
        