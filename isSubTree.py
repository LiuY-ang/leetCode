# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s and t:
            return self.compareTrees(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        else: #一定不会同时为空的，因为题目给出的条件就是两个不为空的树
            return False
    def compareTrees(self,root1,root2):#比较以root1为根节点的树，以root2为根节点的树是否相同
        if root1 and root2:#root1和root2都不为空
            if root1.val==root2.val:#如果root1.val和root2.val相等，那么继续比较它们的左右子树
                return self.compareTrees(root1.left,root2.left) and self.compareTrees(root1.right,root2.right)
            else:#root1.val和root2.val不相等，那么返回假值
                return False
        elif root1==None and root2==None:#root1和root2都为空
            return True
        else:#一个为空，另一个不为空
            return False
