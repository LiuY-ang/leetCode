# -*- coding:utf-8 -*-
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        isNegative=False #标记是否为负数
        if num<0:#如果num是负数
            isNegative=True#标记为负数
            num=-num#将num转化为正数
        result="" #存储结果
        while num>=7:
            result=str(num%7)+result #取余数
            num=num/7 #num对7取整数
        result=str(num)+result #将最后小于7的num添加到result的最前边
        if isNegative==True:#如果是负数的话
            result="-"+result#再将结果变为负数
        return result
so=Solution()
print so.convertToBase7(-7)
