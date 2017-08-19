# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d={}
        result=[]
        Max=0
        self.postOrder(root,d)
        print d
        for k in d:#挑选出出现次数最多的值
            if d[k]>Max:
                Max=d[k]
                result=[k]
            elif d[k]==Max:
                result.append(k)
        return result
    def postOrder(self,root,d):
        if root:
            self.postOrder(root.left,d)
            self.postOrder(root.right,d)
            d[root.val]=d.get(root.val,0)+1#统计值出现的次数
