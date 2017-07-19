x = input()
digits = 0
t = x
while( t != 0 ):
    t = t / 10
    digits = digits+1
print digits
left = 0
right = pow(10,digits-1)
leftNumber,rightNumber = x,x
while ( digits > 0 ):
    if( rightNumber/right != leftNumber%10 ):
        return False
    else:
        rightNumber=rightNumber%right
        leftNumber=leftNumber/10
        right = right/10
        digits = digits-1
return True
