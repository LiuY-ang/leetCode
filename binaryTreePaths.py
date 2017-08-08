# Definition for a binary tree node.
#
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths=[]
        path=""
        self.preOrder(root,paths,path)
        print paths
    def preOrder(self,root,paths,path):
        if root:
            if root.left==None and root.right==None:
                paths.append(path+str(root.val))
                return
            self.preOrder(root.left,paths,path+str(root.val)+"->")
            self.preOrder(root.right,paths,path+str(root.val)+"->")
so=Solution()
t=TreeNode(1)
t1=TreeNode(2)
t2=TreeNode(3)
t3=TreeNode(5)
t.left=t1
t.right=t2
t1.right=t3
so.binaryTreePaths(t)
