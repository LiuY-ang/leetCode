# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodes=[root] #用以存储节点
        averageLevel=[] #存储结果
        levels=[1] #用以存储节点的层次
        front=0 #模拟队列的前指针
        while front<len(nodes):
            node=nodes[front] #取出front指向的元素
            if node.left!=None: #如果该元素的左节点
                nodes.append(node.left) #存储当前节点
                levels.append(levels[front]+1) #存储当前节点的层次号，由当前节点的层次加1得到
            if node.right!=None:
                nodes.append(node.right)
                levels.append(levels[front]+1)
            front+=1#访问队列中下一个元素
        i,count,s=1,1,nodes[0].val #用以计数
        while i<len(nodes):
            if levels[i-1]<levels[i]: #有问题
                averageLevel.append(1.0*s/count)
                s=0
                count=0
            s+=nodes[i].val #和加1
            count+=1#计数变量加1
            i+=1 #下标变量加1
        averageLevel.append(1.0*s/count)#添加最后一个层次的节点的平均值
        return averageLevel
so=Solution()
t=TreeNode(3)
t1=TreeNode(9)
t2=TreeNode(20)
t3=TreeNode(15)
t4=TreeNode(7)
t.left=t1
t.right=t2
t2.left=t3
t2.right=t4
print so.averageOfLevels(t)
