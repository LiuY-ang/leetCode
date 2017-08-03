# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthA=self.getLength(headA)#得到链表headA的长度
        lengthB=self.getLength(headB)#得到链表headB的长度
        print lengthA,lengthB #打印两者的长度
        #headA和headB遍历链表
        if lengthA>lengthB: #如果headA的长度较长，则headA先遍历lengthA-lengthB个节点
            diff=lengthA-lengthB
            for i in range(0,diff):
                headA=headA.next
        else:#如果lengthA<=lengthB,那么headB先走lengthB-lengthA个节点
            diff=lengthB-lengthA
            for i in range(0,diff):
                headB=headB.next
        while headA!=headB: #然后headA和headB在同时遍历，只要不相等就执行循环
            headA=headA.next
            headB=headB.next
        return headA
    def getLength(self,head): #得到链表的长度
        length=0
        while head!=None:
            head=head.next
            length+=1
        return length
a1=ListNode('a1')
a2=ListNode('a2')
a1.next=a2
b1=ListNode('b1')
b2=ListNode('b2')
b3=ListNode('b3')
b1.next=b2
b2.next=b3
c1=ListNode('c1')
c2=ListNode('c2')
c3=ListNode('c3')
c1.next=c2
c2.next=c3

a2.next=c1
b3.next=c1
so=Solution()
print so.getIntersectionNode(a1,b1).val
