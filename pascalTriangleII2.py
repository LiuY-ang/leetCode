#-*- coding: UTF-8 -*-
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        ans=[1,1]
        for i in range(1,rowIndex):
            temp=[1]
            for j in range(1,len(ans)):
                temp.append(ans[j]+ans[j-1])
            temp.append(1)
            ans=temp[:]
        return ans
so=Solution()
print so.getRow(4)
