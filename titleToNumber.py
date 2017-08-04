class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s[::-1]
        num=0
        for i in range(len(s)):
            num=num+pow(26,i)*(ord(s[i])-64)
        return num
so=Solution()
print so.titleToNumber("AAA")
