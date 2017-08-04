# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
            return None
        while head.val==val:
            head=head.next
            if head==None:
                return head
        p=head.next
        q=head
        while p!=None:
            if p.val==val:
                q.next=p.next
                p=p.next
            else:
                q=p
                p=p.next
        return head
