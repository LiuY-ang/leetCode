class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=1
        for i in range(2,n+1):
            s=s*i
        length=0
        print s
        while s%10==0:
            length=length+1
            s=s/10
        return length
so=Solution()
print so.trailingZeroes(30)
