class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n!=1 and n!=4:
            s=0
            while n!=0:
                s=s+pow(n%10,2)
                n=n/10
            n=s
        return n==1
so=Solution()
print so.isHappy(11)
