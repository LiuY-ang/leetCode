# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        self.ans=""
        self.preOrder(t)
        return self.ans
    def preOrder(self,root):
        if root:
            self.ans=self.ans+str(root.val)
            if root.left:
                self.ans=self.ans+"("
                self.preOrder(root.left)
                self.ans=self.ans+")"
            elif root.left==None and root.right:
                self.ans=self.ans+"()"
            if root.right:
                self.ans=self.ans+"("
                self.preOrder(root.right)
                self.ans=self.ans+")"

t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t4=TreeNode(4)
t1.left=t2
t1.right=t3
t2.left=t4
so=Solution()
print so.tree2str(t1)
# 1(2(4)())(3()())
# 1(2(4()())())(3()())
