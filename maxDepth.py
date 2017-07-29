# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getDepth(root)
    def getDepth(self,root):
        if root != None:
            if root.left==None and root.right==None:#如果为叶子节点
                return 1 #则返回1
            leftDepth=self.getDepth(root.left)
            rightDepth=self.getDepth(root.right)
            return leftDepth+1 if leftDepth>rightDepth else rightDepth+1
        return 0
