# -*- coding:utf-8 -*-
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()#用空格分离字符
        if len(words)==0:
            return ""
        ans=""
        for e in words:#依次取出分离出来的字符串
            ans=ans+e[::-1]+" " #逆置
        return ans[0:len(s)] #最后多加了一个空格，把空格去掉
so=Solution()
print so.reverseWords("liu yang")
