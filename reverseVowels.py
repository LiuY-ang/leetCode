class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels="aeiouAEIOU"
        s=list(s)
        length=len(s)
        low=0#从前往后扫描，遇到元音就停止，然后交换。
        high=length-1#从后往前扫描
        while low<high:
            while s[low] not in vowels and low<high:
                low+=1
            while s[high] not in vowels and low<high:
                high-=1
            #交换元素的值
            s[high],s[low]=s[low],s[high]
            #分别将high减1，low加1
            high=high-1
            low=low+1
        return "".join(s)
so=Solution()
print so.reverseVowels("loveleetcode")
#"leotcede"
