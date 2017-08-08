# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.postOrder(root) #后序遍历

    def postOrder(self,root):
        if root :
            self.postOrder(root.left)
            self.postOrder(root.right)
            temp=root.left #在最后遍历节点的时候，交换左右子树
            root.left=root.right
            root.right=temp
