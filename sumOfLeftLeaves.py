# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s=[0]
        self.postOrder(root,s,False)
        return s[0]
    def postOrder(self,root,s,isLeft):
        if root!=None:
            self.postOrder(root.left,s,True) #左节点的isLeft为True
            self.postOrder(root.right,s,False)#右节点的isLeft为false
            if root.left==None and root.right==None and isLeft==True:
                #如果为左叶子节点
                s[0]+=root.val
t=TreeNode(3)
t1=TreeNode(9)
t2=TreeNode(20)
t3=TreeNode(15)
t4=TreeNode(7)
t.left=t1
t.right=t2
t2.left=t3
t2.right=t4
so=Solution()
print so.sumOfLeftLeaves(t)
