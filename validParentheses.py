class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for char in s:
            if(char=='(' or char=='[' or char=='{'):
                stack.append(char)
            elif char==')' and stack[-1]=='(':
                stack.pop()
            elif char==']' and stack[-1]==']':
                stack.pop()
            elif char=='}' and stack[-1]=='{':
                stack.pop()
        if len(stack)==0:
            return True
        else:
            return False
