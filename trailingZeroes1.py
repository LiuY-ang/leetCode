class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        while n>=5:
            s+=n/5
            n=n/5
        return s
so=Solution()
print so.trailingZeroes(25)
