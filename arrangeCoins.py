class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        for i in range(n):
            if n>=(i+1):
                s=s+1
                n-=(i+1)
                print "n=",n,"s=",s
            else:
                break
        return s
so=Solution()
print so.arrangeCoins(1804289383)
