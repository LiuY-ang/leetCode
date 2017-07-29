class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length=len(nums)
        if length==0: #长度为0，即数组为kong
            return None #直接返回
        if length==1: #长度为1，即只有一个元素
            return TreeNode(nums[0]) #则返回该元素
        else:
            half=(length-1)/2 #取得中点元素
            root=TreeNode(nums[half]) #建立新的节点，该节点的值为数组的中点值
            #取得中点以左的元素，并递归建立树
            root.left=self.sortedArrayToBST(nums[:half])
            #取得中点以右的元素，递归建立树
            root.right=self.sortedArrayToBST(nums[half+1:])
            return root
