# -*- coding:utf-8 -*-
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return self.uglyNumber(num)
    def uglyNumber(self,num):
        if num==1:
            return True
        elif num<1:
            return False
        #下面的if...else只会执行其中的一个
        if num%2==0: #能被2整除，那么除以2递归
            return self.uglyNumber(num/2)
        elif num%3==0: #能被3整除
            return self.uglyNumber(num/3)
        elif num%5==0: #能被5整除
            return self.uglyNumber(num/5)
        else: #不能被2，3，5整除，返回false
            return False

so=Solution()
print so.isUgly(214797179)
