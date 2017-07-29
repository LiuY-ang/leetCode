#-*- coding: UTF-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if  root == None:
            return []
        #到循环之前都是进行初始化
        levelOrder=[] #存储节点的层次遍历节点值
        listTree=[root] #存储层次遍历的节点，模拟队列
        level=[1] #存储节点的层次
        front=0
        while front != len(listTree):
            temp=listTree[front]#取的队列中的front指向的值
            #level[front]表示当前的节点层次
            #len(levelOrder)表示levelOrder的长度
            if level[front] > len(levelOrder): #如果层次大于levelOrder的长度
                li=[temp.val]#那么代表着levelOrder中没有该二叉树该层次的数据
                levelOrder.insert(0,li)#建立该层次的list，并添加到levelOrder中
            else: #level[front]<=len(levelOrder)。levelOrder中二叉树该层次的数据
                levelOrder[0].append(temp.val)#直接添加即可
            if temp.left!=None:#左子树非空，那么添加到队列中
                listTree.append(temp.left)
                level.append(level[front]+1)
            if temp.right!=None:#右子树非空，那么添加到队列中
                listTree.append(temp.right)
                level.append(level[front]+1)
            front=front+1#最后将front加1，指向下一个待访问的节点
        return levelOrder
