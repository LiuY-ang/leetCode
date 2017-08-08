# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#本题是Binary Search Tree，一开始做的时候，忘记这个条件了
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        mini=min(q.val,p.val)
        maxm=max(q.val,p.val)
        return self.findout(root,mini,maxm)
    def findout(self,root,mini,maxm):
        if root:
            if root.val>=mini and root.val<=maxm: #待查找的两个节点分别位于某个节点的左右子树上
                return root #则该节点就是要找的节点
            #代码执行到此，那么上面的条件必有一个不满足，则逐个判断
            elif root.val>maxm:#如果待查找节点中的最大值比当前节点的值小
                return self.findout(root.left,mini,maxm)#那么需要取该节点的左子树寻找
            elif root.val<mini:#如果待查找节点中的最小值比当前节点的值大
                return self.findout(root.right,mini,maxm)#向该节点的右子树上查找


t=TreeNode(6)
t1=TreeNode(2)
t2=TreeNode(8)
t3=TreeNode(0)
t4=TreeNode(4)
t5=TreeNode(7)
t6=TreeNode(9)
t7=TreeNode(3)
t8=TreeNode(5)
t.left=t1
t.right=t2
t1.left=t3
t1.right=t4
t4.left=t7
t4.right=t8
t2.left=t5
t2.right=t6
so=Solution()
print so.lowestCommonAncestor(t,t1,t7).val
