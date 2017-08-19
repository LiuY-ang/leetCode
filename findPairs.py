# -*- coding:utf-8 -*-
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()#排序
        print nums
        ans,i,j,length={},0,0,len(nums)
        while i<length:
            j=i+1
            while j<length:
                if nums[j]-nums[i]==k:#两者之差等于k
                    ans[nums[i]]=nums[j]#存下来
                elif nums[j]-nums[i]>k:#如果两者之差大于k，说明后边差值就没有等于k的了
                    break#结束
                j=j+1
            i=i+1
        return len(ans)
so=Solution()
print so.findPairs([1,3,2,5,4],1)
