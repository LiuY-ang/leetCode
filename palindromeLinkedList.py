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
        nums=[]
        p=head
        while p!=None:
            nums.append(p.val)#添加到list
            p=p.next
        temp=nums[::-1] #取反
        return temp==nums #比较是否相等
