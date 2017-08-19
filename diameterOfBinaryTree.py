# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
        This path may or may not pass through the root.
        二叉树的直径为树中最长的路径，该路径可以不用经过根节点
        '''
        if root==None:
            return 0
        self.diameter=0
        self.getDepth(root)
        return self.diameter
    def getDepth(self,root):#利用求树的高度的变形
        if root:
            leftDepth=self.getDepth(root.left)#求左子树的高度
            rightDepth=self.getDepth(root.right)#求右子树的高度
            diameter=leftDepth+rightDepth#获得以root为根节点的树的直径
            if diameter>self.diameter:#如果该直径大于已知的最大的直径
                self.diameter=diameter#更新最大直径的值
            return (leftDepth if leftDepth>rightDepth else rightDepth)+1#返回以root为根节点的树的高度
        return 0#如果节点为空，返回0
root=TreeNode(2)
t1=TreeNode(4)
t2=TreeNode(5)
root.left,root.right=t1,t2
so=Solution()
print so.diameterOfBinaryTree(root)
