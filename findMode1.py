# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:#为空直接返回
            return []
        #preNode存储上一个访问的节点，result存储结果
        #count用以计数，某个数字出现的次数，m为已知的某个数出现的最大次数
        preNode,result,count,m=[None],[],[1],[0]
        self.inOrder(root,preNode,result,count,m)
        i=len(result)-1
        while result[i]!=":":
            i-=1
        return result[i+1:]
    def inOrder(self,root,preNode,result,count,m):
        if root!=None:
            self.inOrder(root.left,preNode,result,count,m)
            #该判断主要用于count计数
            if preNode[0]!=None:#如果前一个节点不为None
                if preNode[0].val==root.val:#前一个节点和本节点的值相等
                    count[0]+=1#那么将count[0]的值加1
                else:#如果前一个节点的值和本节点的值不相等，说明是新的一个数
                    count[0]=1#则重新计该数出现的次数
            if count[0]>=m[0]:
                if count[0]>m[0]:#如果某个数出现的次数较多
                    result.append(":")#加上个标记。不为什么不写为result=[],因为这样result的地址就变了
                result.append(root.val)#添加该数
                m[0]=count[0]#更新出现的最大的次数
            preNode[0]=root#更新访问过的前一个节点信息
            self.inOrder(root.right,preNode,result,count,m)
t=TreeNode(1)
t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(2)
t.left=t1
t.right=t2
t2.left=t3
so=Solution()
print so.findMode(t)
