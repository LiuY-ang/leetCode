s = raw_input()
d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
num = 0
for index in range(0,len(s)-1):
    if( d.get(s[index]) < d.get(s[index+1]) ):
        num = num+d[s[index+1]]-d[s[index]]
        index=index+1
    else:
        num=num+d[s[index]]
#        index=index+1
#    if index < len(s)-1:
print index
if( index == len(s)-2 ):
    num=num+d[s[index+1]]
print num
