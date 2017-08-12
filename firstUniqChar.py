# -*- coding:utf-8 -*-
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in s:
            d[i]=d.get(i,0)+1 #统计出现的字符个数
        for i in range(len(s)): #遍历d
            if d[s[i]]==1: #某个字符只出现了一次
                return i #返回该字符在字符串中位置
        return -1
so=Solution()
print so.firstUniqChar("loveleetcode")
