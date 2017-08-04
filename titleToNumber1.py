class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        for i in range(len(s)):
            num=num*26
            num=num+(ord(s[i])-64)
        return num
so=Solution()
print so.titleToNumber("ZZ")
