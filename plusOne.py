class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        while(digits[i]+1 > 9 and i >= 0): #从后往前扫描，
            digits[i]=0   #直到遇到某位数加1<=9停止
            i=i-1
        if i==-1 : #若循环结束之后，i==-1,说明digits的各位数字都为9
            digits.insert(0,1)#需要在第一位之前插入1即可
        else:#若i！=-1说明循环在中间的某位数上就停止了，该位数digits[i]+1<=9
            digits[i]=digits[i]+1 #只需要将该位数置为digits[i]=digits[i]+1
        return digits

li=[2,9]
s = Solution()
print s.plusOne(li)
