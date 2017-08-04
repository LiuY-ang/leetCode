class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp="{0:032b}".format(n)
        count=0
        for element in temp:
            if element=='1':
                count+=1
        return count
so=Solution()
print so.hammingWeight(2)
