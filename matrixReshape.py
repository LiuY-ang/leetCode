class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ans,temp=[],[]
        for r1 in nums:
            for c1 in r1:
                temp.append(c1)#将原矩阵中的元素依次加入temp中
                if len(temp)==c:#如果temp的长度等于c，
                    ans.append(temp)#那么将temp添加到结果集中
                    temp=[]#并将temp清空
        if len(temp)==0 and len(ans)==r:#如果最后依次的temp已经添加到ans，并且新矩阵ans的行数等于给定的行数r
            return ans
        return nums
so=Solution()
nums = [[1,2],[3,4]]
r = 2
c = 4
print so.matrixReshape(nums,r,c)
