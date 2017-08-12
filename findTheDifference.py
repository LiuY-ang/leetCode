class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in t:
            if t.count(i) > s.count(i): #某个字符的t中的个数较多
                return i #那么返回该字符
so=Solution()
print so.findTheDifference("a","aa")
