# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []

        l2r = True
        q = deque()
        q.append(root)

        while q:
            l = deque()
            size = len(q)

            for _ in range(size):
                node = q.popleft()

                if l2r:
                    l.append(node.val)
                else:
                    l.appendleft(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(list(l))
            l2r = not l2r

        return result
        