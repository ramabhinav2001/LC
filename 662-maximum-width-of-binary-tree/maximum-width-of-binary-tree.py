# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        ans=0
        q=deque([(root,0)])
        while q:
            level_length=len(q)
            _,level_start=q[0]

            for i in range(level_length):
                node,ind=q.popleft()
                if node.left:
                    q.append((node.left,2*ind))
                if node.right:
                    q.append((node.right,2*ind+1))
            ans=max(ans,ind - level_start+1)
        return ans
            
        