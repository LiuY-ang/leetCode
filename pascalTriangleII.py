#-*- coding: UTF-8 -*-
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        li=[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] #pascal三角的请5行（包括第5行）
        if rowIndex<=4:#如果小于等于则直接返回
            return li[rowIndex]
        for i in range(5,rowIndex+1):
            temp=[1] #建立list，该list的每一行的第一个数都是1
            for j in range(1,i+1):
                if j==len(li[i-1]):#如果到达最后，则直接赋值为上一行的最后一个数
                    temp.append(li[i-1][j-1]+0)
                else: #其余情况，则将上一行的第j和j-1个数相加
                    temp.append(li[i-1][j]+li[i-1][j-1])
            li.append(temp)
        return li[rowIndex]
so=Solution()
print so.getRow(6)
