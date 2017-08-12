class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        i=1
        print n
        while s<=n:
            s+=i
            i+=1
            #print 's=',s,'i=',i
        # if s==n:
        #     return i-1
        return i-2
so=Solution()
n=1804289383
print so.arrangeCoins(1)
