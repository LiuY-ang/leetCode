class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length=0
        i=len(a)-1
        j=len(b)-1
        s=""
        #循环之前主要对进位标志carry进行初始化
        if int(a[i])+int(b[j])>=2:#若最后一位相加大于2，
            s=str(int(a[i])+int(b[j])-2)+s#则本位置为str(int(a[i])+int(b[j])-2)
            carry=1#并标记 进位位为1
        else:#若最后一位相加小于2
            s=str(int(a[i])+int(b[j]))+s
            carry=0#carry代表没有进位
        i=i-1
        j=j-1
        while i>=0 and j>=0: #从倒数第二位开始
            if int(a[i])+int(b[j])+carry>=2:#某位次上的数和进位位相加大于等于2
                s=str(int(a[i])+int(b[j])+carry-2)+s#则依次置本位为str(int(a[i])+int(b[j])+carry-2)
                carry=1#并拼接字符串，然后置进位位标志为1
            else:#int(a[i])+int(b[j])+carry<2,z则本位置为str(int(a[i])+int(b[j])+carry)
                s=str(int(a[i])+int(b[j])+carry)+s#并拼接字符串
                carry=0 #置进位位标志为0
            lenght=length+1
            i=i-1#下标依次减1
            j=j-1
        if( i != -1):#如果a的位数较多，则继续进行循环，把多余的位数相加
            while(i>=0 ):
                if int(a[i])+carry>=2:
                    s=str(int(a[i])+carry-2)+s
                    carry=1
                else:
                    s=str(int(a[i])+carry)+s
                    carry=0
                i=i-1
        if( j != -1):#如果b的位数较多，处理过程相似
            while(j>=0 ):
                if int(b[j])+carry>=2:
                    s=str(int(b[j])+carry-2)+s
                    carry=1
                else:
                    s=str(int(b[j])+carry)+s
                    carry=0
                j=j-1
        if( carry == 1):#如果carry为1，则说明有进位，在结果的最前边加1
            s="1"+s
        return s
a="110010"
b="100"
so=Solution()
print so.addBinary(a,b)
