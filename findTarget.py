# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.orders=[]
        self.inOrder(root)#中序遍历结果为有序的
        i,j=0,len(self.orders)-1#i从前往后，j从后往前
        #print self.orders
        while i<j:
            s=self.orders[i]+self.orders[j]
            if s==k:
                return True
            elif s>k:
                j=j-1
            elif s<k:
                i=i+1
        return False#执行到这说明没有相等的
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            self.orders.append(root.val)
            self.inOrder(root.right)
