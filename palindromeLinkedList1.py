# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #设置快慢指针，慢指针每次只走一步，快指针每次走两步，等快指针走完的时候，慢指针的位置
        #就是中点。
        slow,fast=head,head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next

        #对后半部分的链表进行逆序建表
        p=slow.next
        slow.next=None
        while p:
            temp=p.next
            p.next=slow.next
            slow.next=p
            p=temp
        #ph的值为head，ps的值为slow.next
        #偶数个节点，奇数个节点，slow都会停在待比较节点的上一个节点
        ph,ps=head,slow.next
        while ph and ps:
            if ps.val != ph.val:
                return False
            ph=ph.next
            ps=ps.next
        return True
