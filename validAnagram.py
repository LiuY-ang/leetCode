class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slength=len(s)
        tlength=len(t)
        sdict={}
        tdict={}
        if slength!=tlength:
            return False
        i=0
        while i<slength:
            if sdict.get(s[i],-1)==-1:
                sdict[s[i]]=1
            else:
                sdict[s[i]]=sdict[s[i]]+1
            if tdict.get(t[i],-1)==-1:
                tdict[t[i]]=1
            else:
                tdict[t[i]]=tdict[t[i]]+1
            i+=1
        return sdict==tdict
so=Solution()
print so.isAnagram("carr","caar")
