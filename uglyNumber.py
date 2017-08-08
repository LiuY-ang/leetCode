class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return self.uglyNumber(num,1)
    def uglyNumber(self,num,n): #完全是一步一步的去模拟是否等于num
        if n==num:   #会超时
            return True
        elif n>num:
            return False
        return self.uglyNumber(num,n*2) or self.uglyNumber(num,n*3) or self.uglyNumber(num,n*5)
so=Solution()
print so.isUgly(10000000000)
