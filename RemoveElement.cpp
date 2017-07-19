int removeElement(int* nums, int numsSize, int val)
{
  int i=0,j=numsSize-1,length=0;
  while( i<=j )
  {
    while (nums[i] != val && i<numsSize )
      ++i;
    while (nums[j] == val && j>=0 )
      --j;
    if( i-1 <= j )
    {
      int temp = nums[i];
      nums[i] = nums[j];
      nums[j] = temp;
      ++length;
    }
  }
  return length+1;
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
