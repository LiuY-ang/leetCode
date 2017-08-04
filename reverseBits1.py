class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n="{0:032b}".format(n)
        return int(n[::-1],2)

so=Solution()
print so.reverseBits(43261596)
