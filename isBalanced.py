# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        flag=[0]
        self.getDepth(root,flag)
        if flag[0]==0:
            return True
        else:
            return False
    def getDepth(self,root,flag):
        if root==None:
            return 0
        else:
            leftDepth=self.getDepth(root.left,flag)
            rightDepth=self.getDepth(root.right,flag)
            result=leftDepth-rightDepth
            if result>1 or result<-1:
                flag[0]=1
            print result
            return leftDepth+1 if leftDepth>rightDepth else rightDepth+1
