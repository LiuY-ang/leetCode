class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1') #异或之后，返回字符串，统计1的个数
so=Solution()
print so.hammingDistance(4,1)
