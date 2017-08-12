class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: #n<=0直接返回
            return False
        while n!=1 and n%3==0:#n>1并且n整除3，那么就已知循环
            n/=3
        #循环不满足的条件为：n==1，或者 n%3!=0
        #n==1是3的幂，其余情况不是
        if n>1:
            return False
        else:
            return True
so=Solution()
print so.isPowerOfThree(9)
