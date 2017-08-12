import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        low=0
        high=int(math.sqrt(c)) #得到c开方后的整数部分，high*high<=c
        while low<=high:#循环判断条件
            square=low*low+high*high#得到平方和
            print low,high
            if square==c: #如果相等，就返回真值true
                return True
            elif square>c: #如果两数的平方和大于c，需要减少两数的平方和，high减1
                high-=1
            elif square<c:#如果两数的平方和小于c，那么需要增大两数的平方和，low加1
                low+=1
        return False #执行到这里，说明没有符合条件的数
so=Solution()
print so.judgeSquareSum(6)
