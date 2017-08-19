# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# brute force Solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root!=None:
            #self.find_paths(root,sum)是以root为树的根节点遍历树
            #self.pathSum(root.left,sum)以root.left作为根节点，然后遍历
            #self.pathSum(root.right,sum)以root.right作为根节点，然后遍历
            #在递归的过程又会以各个节点，即以root为根节点的树中，每个节点都会以根节点的身份遍历，以该节点为根节点的树
            return self.find_paths(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
        return 0
    def find_paths(self,root,target):
        if root!=None:
            #root.val==target,返回True，int(True)返回1；int(False)返回0
            #self.find_paths(root.left,target-root.val),访问左孩子，target-root.val表示要路径和为target还需要(target-root.val)
            #self.find_paths(root.right,target-root.val),访问右孩子，target-root.val表示要路径和为target还需要(target-root.val)
            #返回的值由三部分组成，当前的路径和是否等于target，左子树的路径和等于target的条数，右子树上路径和等于target的条数
            return int(root.val==target)+self.find_paths(root.left,target-root.val)+self.find_paths(root.right,target-root.val)
        return 0

t=TreeNode(5)
t1=TreeNode(3)
t2=TreeNode(3)
t3=TreeNode(8)
t.left=t1
t.right=t2
t1.left=t3
so=Solution()
print so.pathSum(t,8)
