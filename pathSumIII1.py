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
        so_far=0#存储从根节点到某个节点的路径的和
        self.ans=0#存储答案
        d={0:1}#存储路径和
        self.inOrder(root,so_far,sum,d)#中序遍历
        return self.ans#返回结果
    def inOrder(self,root,so_far,target,d):
        if root:
            #如果complement为负数，表示so_far+root.val还差abs(complement),需要将当前的so_far+root.val往下加上abs(complement)
            #或者将前边加上的某个负数减掉，以使so_far+root.val变大，以使so_far+root.val==target。因为d中保存了前边路径中的和，如果
            #complement等于前从根节点到某个节点的路径和，那么只需要减掉该段路径和即可，然后从该节点到目前访问的节点就为target的值
            #如果complement为正数，那么表示多了abs(complement)，处理过程和上边类似
            complement=so_far+root.val-target#到从根节点和该节点的路径和与target和的差，并存储在complement中
            if complement in d and d[complement]!=0:#查看complement是否在在d中
                print root.val,d
                self.ans+=d[complement]#则将结果加上d[complement]
            #以下的语句主要用于存储路径和
            d.setdefault(so_far+root.val,0)#如果路径和不存在，将会添加键并将值设为默认值；如果存在返回以前有过的值，不存在的话返回默认的值
            d[so_far+root.val]+=1#将d[so_far+root.val]的值加1，表示路径和为so_far+root.val的路径又多了一条
            self.inOrder(root.left,so_far+root.val,target,d)#遍历左节点
            self.inOrder(root.right,so_far+root.val,target,d)#遍历右节点
            d[so_far+root.val]-=1#即将结束遍历该节点，路径和为so_far+root.val的路径条数减少1，所以d[so_far+root.val]的值减1
        return


t=TreeNode(5)
t1=TreeNode(3)
t2=TreeNode(3)
t3=TreeNode(8)
t.left=t1
t.right=t2
t1.left=t3
so=Solution()
print so.pathSum(t,8)
