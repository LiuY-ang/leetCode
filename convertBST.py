# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.so_far=0
        self.rightAndLeft(root)#先遍历右子树，在遍历根节点，后遍历左子树。这样遍历的结果为倒序的
        return root
    def rightAndLeft(self,root):
        if root:
            self.rightAndLeft(root.right)
            #将节点中val变为self.so_far+root.val,即所有比root.val大的节点值与root.val的和
            #更新self.so_far的值
            root.val,self.so_far=self.so_far+root.val,self.so_far+root.val
            self.rightAndLeft(root.left)
root=TreeNode(5)
t1=TreeNode(2)
t2=TreeNode(13)
root.left=t1
root.right=t2
so=Solution()
print so.convertBST(root).val,t1.val,t2.val
