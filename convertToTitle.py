class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s=''
        while n>26:
            m=n%26
            n=n/26
            print m,n
            if m==0: #为0的情况需要特殊处理，借位处理
                s='Z'+s #向前借一位
                n=n-1#相应的前一位减1
            elif chr(64+m)>='A':
                s=chr(64+m)+s
        return chr(64+n)+s
n=24568 #zz
print n/26
print n%26
so=Solution()
print so.convertToTitle(n)
