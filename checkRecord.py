# -*- coding:utf-8 -*-
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.find("LLL")!=-1: #如果没有找到会返回-1。连续三次迟到
            return False
        if s.count("A")>1:#缺席的次数大于1次
            return False
        return True#其余情况返回true
so=Solution()
print so.checkRecord("PPALLPLL")
