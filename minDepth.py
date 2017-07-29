#-*- coding: UTF-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: #若根节点为空，则直接返回0
            return 0
        mini=sys.maxint#设置为整数的最大值
        return self.getDepth(root,1,mini)
    def getDepth(self,root,now,mini):
        if root!=None:#节点不为空
            if root.left==None and root.right==None and now<mini:
                mini=now#若节点为叶子节点，且该叶子节点的深度较小的时候，把该值赋给mini
            else:
                mini=self.getDepth(root.left,now+1,mini)#递归左子树
                mini=self.getDepth(root.right,now+1,mini)#递归右子树
            return mini#最后返回mini
        return mini#若节点为空，则直接返回mini
