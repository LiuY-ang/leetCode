# -*- coding:utf-8 -*-
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low=1
        high=num
        while low<=high:
            mid=(low+high)/2 #取得中点元素
            s=mid*mid #中点的平方
            if s==num: #如果相等
                return True #返回该mid
            if s>num: #mid*mid>num，需要减小值
                high=mid-1 #故将high赋值为mid-1
            else: #mid*mid<num,需要增大值
                low=mid+1
        return False
so=Solution()
print so.isPerfectSquare(9)
