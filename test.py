def function(s):
    st=""
    for index in range(0,len(s)):
         if ( index == 0):
             st=st+s[index].upper()
         else:
             st=st+s[index].lower()
         index = index+1
    return st
print map(function,['adam', 'LISA', 'barT'])
