int maxSubArray(int* nums, int numsSize)
{
    int largest=0;
    int now=0;
    for(int i=0;i<numsSize;++i)
    {
      now=now+nums[i];
      if (now > largest)
        largest=now;

      if (now<0) //该条if语句最重要了,如果当前的now小于0，那么就将now置为0
        now=0; //若now<0,那么下次循环执行now=now+nums[i]后nums[i]会减少
    }        //只有数值增大才会找到最大值,前边的累加和小于0，往下累加影响到其他的比较
    return largest;
}
int main()
{
  int nums[9]={-2,1,-3,4,-1,2,1,-5,4};
  // int nums[4]={4,1,2,-3};
  int result = maxSubArray(nums,9);
  printf("%d\n",result );
}
