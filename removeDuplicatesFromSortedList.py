# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        1->1->2->3->3    1->2->3
        """
        i=head
        while i != None: #循环到末尾停止
            j=i.next
            while j!=None and j.val == i.val: #当到达链表尾或者j.val>i.val
                j=j.next  #的时候就停止循环
            i.next=j #去掉重复元素，只需要改变地址即可
            i=i.next
        return head
head=ListNode(1)
listNode1=ListNode(1)
listNode2=ListNode(2)
head.next=listNode1
listNode1.next=listNode2
so=Solution()
i=so.deleteDuplicates(head)
while i!= None:
    if i.next == None:
        print i.val
    else:
        print i.val,
    i=i.next
