# -*- coding:utf-8 -*-
# Definition for a binary tree node.
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        题目给出的是BST，那么中序遍历的结果是有序的，最小的差值只能是相邻的元素才有可能是最小的
        '''
        self.mini=sys.maxint#存储最小的差值
        self.preNode=None#存储前一个节点
        self.inOrder(root)#中序遍历
        return self.mini#返回结果
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            if self.preNode!=None:#如果前一个节点不为空
                #如果前一个节点和本节点的差值比已知的最小差值较大，那么已知的差值，否则返回前一个节点和本节点的差值
                self.mini=( self.mini if root.val-self.preNode.val>=self.mini else root.val-self.preNode.val )
            self.preNode=root#更新preNode，对于下一个待访问的节点，本节点为前一个节点
            self.inOrder(root.right)
root=TreeNode(1)
t1=TreeNode(3)
t2=TreeNode(2)
root.right=t1
t1.left=t2
so=Solution()
print so.getMinimumDifference(root)
