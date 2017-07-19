class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        s = strs[0]
        for index in range(1,len(strs)):
            ix,iy=0,0
            temp=""
            while ix<len(s) and iy<len(strs[index]):
                if s[ix]==strs[index][iy]:
                    temp=temp+s[ix]
                    ix=ix+1
                    iy=iy+1
                else:
                    break
            s = list(temp)
        return s
