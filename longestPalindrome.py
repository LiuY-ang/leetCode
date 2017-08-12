# -*- coding:utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in s:
            d[i]=d.get(i,0)+1 #统计字符出现的个数
        result=0 #存储结果
        isSingle=False #存储是否有单个的字符出现
        for k in d: #依次取出d中的键
            result+=d[k]/2 #长度加d[k]/2
            d[k]=d[k]%2#更新d[k]
            if d[k]==1: #标记是否有单个字符单独出现
                isSingle=True
        print d
        if isSingle:#如果有单独出现的字符，那么最长的回文串为result*2+1,单独出现的字符在中间的位置
            return result*2+1
        return result*2

so=Solution()
print so.longestPalindrome("ccc")
