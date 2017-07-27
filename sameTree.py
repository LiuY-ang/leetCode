# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.checkout(p,q)
    def checkout(self,p,q): #需要递归,故单独写一个函数
        if p!=None and q!=None: #p和q都不空
            if p.val==q.val:#则比较它们的值，如果相等
                left=self.checkout(p.left,q.left)#比较它们的左子树
                right=self.checkout(p.right,q.right)#再比较它们的右子树
                return left and right #左右子树都相等，才返回真值
            else:
                return False
        elif p==None and q==None: #如果节点为空，则返回真值
            return True
        else:  #p和q一空一不空，则返回假值
            return False
