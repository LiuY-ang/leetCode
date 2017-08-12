class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0: #小于等于0
            return False #直接返回
        n=1
        while n<num:
            n=n<<2 #将n扩大四倍
        #循环结束的情况为n>num 或者n==num
        if n==num:
            return True
        else:
            return False
so=Solution()
print so.isPowerOfFour(-9)
