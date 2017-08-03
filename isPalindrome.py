class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0 #初始化为s的第一个元素的下标
        j=len(s)-1#初始化为s最后一个元素的下标
        s=s.lower()#全部变为小写字母
        while i<=j:
            if (s[i]<'a' or s[i]>'z') and (s[i]<'0' or s[i]>'9'):
                i+=1 #s[i]不在[a,z]或[0,9]之间，则为其他字符，将i加1比较下一个元素
            elif (s[j]<'a' or s[j]>'z') and (s[j]<'0' or s[j]>'9'):
                j-=1 #s[j]不在[a,z]和[0,9]之间，则为其他字符，将j减1比较下一个元素
            elif s[i]==s[j]: #当前位置上的元素相等，则将i加1，j减1，继续进行比较
                i=i+1
                j=j-1
            elif s[i]!=s[j]: #若s[i],s[j]同时在[a,z]或[0,9]之间，它们还不相等
                break#则不是回文，直接结束
        if i<j:
            return False
        else:
            return True
so=Solution()
print so.isPalindrome("0p")
