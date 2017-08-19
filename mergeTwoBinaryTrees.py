# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.preOrder(t1,t2)#用先序遍历进行合并
    def preOrder(self,t1,t2):
        if t1 and t2:#如果t1和t2都不为空
            root=TreeNode(t1.val+t2.val)#建立两个节点值之和的节点
            root.left=preOrder(t1.left,t2.left)#建立左子树
            root.right=preOrder(t1.right,t2.right)#建立右子树
            return root
        elif t1 and t2==None:#t1不空，t2为空
            root=TreeNode(t1.val)#建立只有t1值的节点
            root.left=preOrder(t1.left,None)#建立左子树
            root.right=preOrder(t1.right,None)#建立右子树
            return root
        elif t1==None and t2:#t1为空，t2不为空
            root=TreeNode(t2.val)#建立只有t2值的节点
            root.left=preOrder(None,t2.left)#建立左子树
            root.right=preOrder(None,t2.right)#建立右子树
            return root
        else: #t1==None and t2==None，即都为空
            return None#返回空值
