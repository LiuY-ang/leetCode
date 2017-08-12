class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i,j=len(num1)-1,len(num2)-1 #字符串的最后一个元素的下标
        flag,result=0,""#flag用来表示进位位，result存储结果
        while i>=0 and j>=0:
            n=int(num1[i])+int(num2[j])+flag #本位之和
            result=str(n%10)+result #把本位的结果写入字符串中
            flag=n/10 #进位位
            i=i-1
            j=j-1
        #循环结束之后，有一个或者两个不符合条件
        if i>=0:#如果num1的位数较多，继续将num1中多出来的位数和进位位相加
            while i>=0:
                n=int(num1[i])+flag
                result=str(n%10)+result
                flag=n/10
                i=i-1
        if j>=0:#如果num2的位数较多
            while j>=0:
                n=int(num2[j])+flag
                result=str(n%10)+result
                flag=n/10
                j=j-1
        if flag==1:#有可能最后进位位为1，比如'1'+'9',最后就有一个进位位
            result="1"+result
        return result
so=Solution()
print so.addStrings("21","9")
