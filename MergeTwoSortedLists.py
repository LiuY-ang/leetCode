# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return []
        li=[]
        i1,i2=0,0
        while i1<len(l1) and i2<len(l2):
            if l1[i1] < l2[i2]:
                li.append(l2[i2])
                i2=i2+1
            else:  #l1[i1]>=l2[i2]
                li.append(l1[i1])
                i1=i1+1
        if i1 != len(l1):
            li=li+l1[i1:]
        if i2 != len(l2):
            li=li+l2[i2:]
