# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumTilt=0
        self.postOrder(root)
        return self.sumTilt
    def postOrder(self,root):
        if root:
            leftTilt=self.postOrder(root.left)
            rightTilt=self.postOrder(root.right)
            #本节点的tilt
            self.sumTilt+=abs(leftTilt-rightTilt)
            #返回root及左、右子树的总和
            return root.val+leftTilt+rightTilt
        return 0
