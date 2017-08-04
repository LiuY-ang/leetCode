class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        li=[]
        while n!=1 :
            s=0
            while n!=0:
                s=s+pow(n%10,2)
                n=n/10
            if s in li:
                return False
            li.append(s)
            n=s
        return n==1
so=Solution()
print so.isHappy(19)
