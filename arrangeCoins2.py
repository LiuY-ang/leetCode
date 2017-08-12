class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        while low<=high:
            mid=(low+high)/2
            s=mid*(mid+1)/2.0
            print 'mid=',mid,'s=',s
            if s==n:
                return mid
            elif s>n:
                high=mid-1
            else: #s<n
                low=mid+1
        return low-1
so=Solution()
print so.arrangeCoins(8)
