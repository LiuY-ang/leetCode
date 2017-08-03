# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head#初始为第一个节点
        while True:
            if fast==None or fast.next==None:#如果遇到空值，说明没有环
                return False#环只能在最后一个节点又指向前边的某一个节点，不一定是第一个节点
            slow=slow.next#代码运行到这，说明slow不为空
            fast=fast.next.next#fast.next不为空
            if slow==fast:#如果slow==fast，说明相遇
                return True #返回真值
# 后来找到了复杂度O(n)的方法，使用两个指针slow,fast。两个指针都从表头开始走，
# slow每次走一步，fast每次走两步，如果fast遇到null，则说明没有环，返回false；
# 如果slow==fast，说明有环，并且此时fast超了slow一圈，返回true。

# 为什么有环的情况下二者一定会相遇呢？因为fast先进入环，在slow进入之后，
# 如果把slow看作在前面，fast在后面每次循环都向slow靠近1，所以一定会相遇，
# 而不会出现fast直接跳过slow的情况。
