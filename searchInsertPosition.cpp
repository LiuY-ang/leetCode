int searchInsert(int* nums, int numsSize, int target)
{
  int i=0;
  for(;i<numsSize;++i)
  {
    if ( target <= nums[i]) //如果在某一个位置nums[i]>=target
    {  //则就是要插入的位置，直接返回
      return i;
    }
  } //数组遍历完，则说明应该插入到数组的末尾
  return numsSize;
}
int main()
{
  int nums[4]={1,3,5,6};
  printf("%d\n",searchInsert(nums,4,0));
}
