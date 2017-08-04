class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numsLenght=len(nums)
        k=k%numsLenght #这是后来加上的，一开始没有意识到k有可能大于numsLength
        if k==0: #如果k==0，那么直接返回
            print nums
            return
        diff=numsLenght-k #得到前边有多少元素需要往后移
        temp=nums[diff:numsLenght] #把后边的元素，存储下来
        i=diff-1 #因为下标从0开始，一共有diff个元素需要移动，最后一个元素为diff-1
        while i>=0:#先将前边的元素往后移动
            nums[i+k]=nums[i]
            i-=1
        i=0
        while i<k: #再将后边的元素移动前边
            nums[i]=temp[i]
            i=i+1
        print nums
so=Solution()
so.rotate([-1],2)
