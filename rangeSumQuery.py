class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums=[0]*(len(nums)+1)
        for i in range(len(nums)):#不存储数组中的具体的数值，存储从0到i元素值的和
            self.sums[i+1]=self.sums[i]+nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1]-self.sums[i] #相减直接得到i到j的和



# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,2)
print param_1
