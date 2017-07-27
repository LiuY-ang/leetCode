class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
      	li=[]
        li.append(1)
        li.append(2)
        for i in range(2,n):
            r=li[i-1]+li[i-2]
            li.append(r)
        return li[n-1]
so = Solution()
print so.climbStairs(4)
