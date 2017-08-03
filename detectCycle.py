# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        step=1
        while True:
            if fast==None or fast.next==None:
                return None
            slow=slow.next#能进行到这一步，说明fast！=none且fast.next!=None
            fast=fast.next.next
            if slow==fast: #第一次相遇的地点
                break
        slow=head #slow从头开始遍历，fast从第一次相遇的地点遍历
        while slow!=fast:#当他们相遇的时候就是进入环的第一个节点
            slow=slow.next
            fast=fast.next
        return slow
