# -*- coding:utf-8 -*-
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length=len(set(s))
        if len(s)==1 or length==len(s):#字符串s中没有重复，则直接结束
            return False
        if length==1 :#如果只有一个元素,且有重复该字符串
            return True
        lastChar=s[-1]#取得字符串s的最后一个元素
        subStr=""#保存可能的字符串
        i=0
        while s[i]!=lastChar:#该循环取到可能的字符串
            subStr+=s[i]
            i+=1
        subStr+=s[i] #subStr不一定是真正的子串，只是可能的字符串
        i+=1
        print subStr
        temp=None
        while i<len(s):
            print i,i+len(subStr)
            temp=s[i:i+len(subStr)]#取到重复的子串
            print "temp=",temp,"subStr=",subStr
            if temp==subStr:#如果子串subStr和temp相等
                i=i+len(subStr)#则继续检查temp的下一个长度为len(subStr)的子串
            else: #temp!=subStr，即如果不相等
                n=len(subStr) #准备添加s的第n个元素，以便检查s[0,n]是否为真正的子串
                if n>len(s)/2:#添加之前，检查一下。如果子串的长度已经大于s的长度的一半了，
                    break#说明已经不能取到下一个长度相等的子串了，直接结束
                subStr+=s[n] #一个一个的往下试探
                i=n+1
        if temp==subStr:#最后检查的长度为len(subStr)的temp和subStr相等，说明subStr为重复的子串
            return True#则返回真值
        return False#否则返回假值
so=Solution()
print so.repeatedSubstringPattern("abaababaab")
