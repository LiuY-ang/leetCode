int maxCrossingSubarray(int a[],int low,int mid,int high)
{
  //4-13行为左半部分处理过程
  int leftSum=0x80000000; //初始化为int类型的最小值，保存目前找到的最大和
  int sum=0;//sum保存每次循环a[i...mid]的值，即每个子数组的值
  for( int i=mid;i>=low;--i )//求出左半部a[low...mid]的最大子数组
  {  //此子数组必须包含a[mid],循环考查每个子数组a[i...mid]的形式从而找到最大值
    sum=sum+a[i];
    if(sum > leftSum)  //当前的最大和与本次循环的子数组相比较，若本次循环的子数组较大
    {
      leftSum=sum; //把目前的最大和更新
    }
  }

  int rightSum=0x80000000;  //右半部分的处理过程和左半部分相似
  sum=0;
  for(int i=mid+1;i<=high;++i)
  {
    sum=sum+a[i];
    if( sum > rightSum)
    {
      rightSum=sum;
    }
  }
  // 将左半部分，右半部分的最大子数组和相加，即为跨越中点的最大子数组和
  return leftSum+rightSum;
}


int findMaximumSubarray(int a[],int low,int high)
{
  if( low == high )   //当只有一个元素的时候，即集合中的只有一个数
    return a[low]; //这个时候最大的子串就是本身
  else
  {
    int mid=(low+high)/2;
    int leftSum=findMaximumSubarray(a,low,mid); //左半区间，一直递归
    int rightSum=findMaximumSubarray(a,mid+1,high);//右半区间，递归
    int crossSum=maxCrossingSubarray(a,low,mid,high);//寻找跨越中点的最大和
    // 将左半部分，右半部分，中间部分找到的最大子数组和进行比较，并返回最大值
    if ( (leftSum>=rightSum) && (leftSum >= crossSum) )
    {
      return leftSum;
    }
    if ((rightSum>=leftSum) && (rightSum>=crossSum))
    {
      return rightSum;
    }
    else
    {
      return crossSum;
    }
  }
}


int main(  )
{
  // int nums[9]={-2,1,-3,4,-1,2,1,-5,4};
  int nums[3]={-3,-3,-3};
  int result = findMaximumSubarray(nums,0,2);
  printf("%d\n",result );
  return 0;
}
