int mySqrt(int x) {
  if(x==0) return 0;
  double n=2;  #n用于保存计算得到的切线横坐标
  double last=0; #last用于保存上一次计算得到的切线横坐标
  while(last!=n){ #如果last和n，即当前切线横坐标和上一次的切线的横坐标，相差的不足够小
    last=n;       #就会一直求切线的横坐标，直到两者之差足够小停止
    n=(n+x/n)/2;
  }
  return (int)n; #取整数返回
}
int main()
{
  double b=0.1;
  double a=0.1;
  bool result=false;
  if(a==b)
    result=true;
  printf("%d\n",result );
  printf("%d\n",mySqrt(1) );
}
