# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        if root is None:
            return None

        q = collections.deque()
        q.append(root)
        

        extra = None
        while q:
            curr_node = q.popleft()

            #swap pointers
            extra = curr_node.right 
            curr_node.right  = curr_node.left
            curr_node.left = extra

            if curr_node.right is not None:
                q.append(curr_node.right)

            if curr_node.left is not None:
                q.append(curr_node.left)

        return root
