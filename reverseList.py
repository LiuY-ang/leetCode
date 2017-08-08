# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #逆序建立单链表
        tail=None
        nHead=ListNode(0)
        #head=head.next
        while head!=None:
            p=head.next
            head.next=nHead.next
            nHead.next=head
            head=p
        return nHead.next
