# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #二分法查找
        low=1
        high=n
        while low<high:
            mid=(low+high)/2
            if isBadVersion(mid)==False:#中间的元素不是坏的版本，第一个坏的版本在最后边
                low=mid+1
            elif isBadVersion(mid)==True:
                high=mid #这里不是high=mid-1
        return left
