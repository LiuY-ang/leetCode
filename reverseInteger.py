x = input()
maxInt = 2147483647
minInt = -2147483648
if x>maxInt or x < minInt:
    print 0
reserve = []
flag = 1
if x < 0:
    x = -x
    flag = -1
while x > 0:
    reserve.append(x%10)
    x = x/10
print reserve
index,s= 0,0
while index < len(reserve):
    s = s*10+reserve[index]
    index = index + 1
if flag == -1:
    s = -s
print s
