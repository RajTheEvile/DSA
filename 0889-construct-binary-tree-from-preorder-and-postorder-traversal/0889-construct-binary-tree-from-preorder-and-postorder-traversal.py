# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not postorder:
            return None
        
        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root
        
        leftV = preorder[1]
        leffn = postorder.index(leftV) + 1
        
        root.left = self.constructFromPrePost(preorder[1:leffn+1], postorder[:leffn])
        root.right = self.constructFromPrePost(preorder[leffn+1:], postorder[leffn:-1])
        
        return root
