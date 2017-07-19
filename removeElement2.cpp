int removeElement(int* nums, int numsSize, int val)
{
  int i=0,n=numsSize;
  while(i<n)
  {
    if( nums[i] == val )
    {
      nums[i] = nums[n-1];
      --n;
    }
    else
    {
      ++i;
    }
  }
  return i;
}
int main()
{
  int nums[2];
  nums[0]=nums[1]=3;
  int len = removeElement(nums,2,5);
  // nums[1]=nums[2]=2;
  // nums[0]=nums[3]=3;
  //int length = removeElement(nums,4,3);
  printf("%d\n",len);
  for (int i = 0; i < len; i++) {
    if(i==len-1)
      printf("%d\n",nums[i]);
    else
      printf("%d ",nums[i]);
  }
}
