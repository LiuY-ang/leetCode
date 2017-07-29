class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getDepth(root)
    def getDepth(self,root):
        if root == None:
            return 0
        else:
            leftDepth=self.getDepth(root.left)
            rightDepth=self.getDepth(root.right)
            return leftDepth+1 if leftDepth>rightDepth else rightDepth+1
