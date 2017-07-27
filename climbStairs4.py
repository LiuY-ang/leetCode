class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
      	base=[[1,1],[1,0]]
        s=self.power(base,n)
        return s[0][0]

    def power(self,matrix,n):
        li=[[1,0],[0,1]] #2价单位矩阵，应该是叫这个名，相当于整数的1，任何整数和此举证相乘，都为原矩阵
        while n >0 :
            if n%2 ==1 : #这个判断最为重要了，主要是为了若n为奇数，再乘base一遍，实现奇数价
                li=self.multiply(li,matrix)
            n=n/2
            matrix=self.multiply(matrix,matrix)
        return li

    def multiply(self,m1,m2):  #2价矩阵乘法
        temp=[[-1,-1],[-1,-1]]
        for i in range(0,2):
            for j in range(0,2):
                temp[i][j]=m1[i][0]*m2[0][j]+m1[i][1]*m2[1][j]
        return temp
so= Solution()
print so.climbStairs(5)
