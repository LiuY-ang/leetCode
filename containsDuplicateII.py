class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        di={}
        for index in range(len(nums)):
            if di.get(nums[index],-1)==-1:#不存在nums[index]的键
                di[nums[index]]=index #那么添加
            else:#nums[index]在前边已经出现过了
                j=di.get(nums[index])#取出该值
                if abs(index-j)<=k: #比较两个值是否小于等于k
                    return True #是的话就放回true
                di[nums[index]]=index #如果不是，把nums[index]对应的值改为最新的index
        return False
so=Solution()
print so.containsNearbyDuplicate([1,0,1,1],1)
